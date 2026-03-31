---
title: Alacrity Wiki
description: 
published: true
date: 2026-03-31T21:52:32.616Z
tags: 
editor: markdown
dateCreated: 2026-03-31T21:52:32.616Z
---

# Alacrity Education — Mixed Wiki Platform Architecture

## Summary

This document describes the architecture for **Alacrity Education's public/private wiki platform**, hosted at [wiki.alacrity.ro](https://wiki.alacrity.ro). The platform is a [Wiki.js](https://js.wiki) instance backed by a centralised identity provider ([Authentik](https://goauthentik.io)), reverse-proxied through [Caddy](https://caddyserver.com), and running on a single on-premise server at the Alacrity lab.

### User Experience at a Glance

From a visitor's perspective the wiki behaves as a **mixed public/private knowledge base**:

- **Unauthenticated visitors** (Guests) can browse every page the editors have chosen to make public — project write-ups, guides, event recaps, and general information about Alacrity Education.
- **Authenticated users** log in via a single *"Sign in with Alacrity"* button, which redirects to `auth.alacrity.ro`. From there they can authenticate with a password, a magic e-mail link, or — if they have linked their accounts — with Discord or GitHub. Members of the Clockworks organisation can sign in directly through their existing LucaciResearch Authentik account.
- Once signed in, users land in the **Editor** role inside Wiki.js, gaining access to private pages (internal procedures, meeting notes, drafts) and the ability to create and edit content according to their permissions.

The identity layer is designed to scale: the same Authentik instance can serve as the SSO provider for any future Alacrity service, not just the wiki.

---

## 1 · Physical Infrastructure

### 1.1 Hardware

| Component | Specification |
|---|---|
| **Machine** | Dell OptiPlex 3060 |
| **CPU** | Intel Core i3 (8th gen) |
| **RAM** | 16 GB |
| **Storage** | 500 GB PCIe SSD |
| **Hostname** | `eros` |
| **Internal DNS** | `eros.lr` |

The server is rack-mounted in the Alacrity lab alongside the existing networking equipment.

### 1.2 Network

| Parameter | Value |
|---|---|
| **VLAN** | 30 |
| **Subnet** | `10.12.3.0/24` |
| **Server address** | `10.12.3.3` |

A port-forwarding rule on the MikroTik edge router exposes TCP ports **80** and **443** from `10.12.3.3` to the public internet, allowing Caddy to terminate TLS and serve both `wiki.alacrity.ro` and `auth.alacrity.ro`.

### 1.3 Operating System

Eros runs **Arch Linux** and acts primarily as a Docker host. All application services are deployed as Docker Compose stacks, with the sole exception of Caddy, which runs bare-metal (see [§4](#4--caddy-reverse-proxy)).

---

## 2 · DNS

### 2.1 Record Layout

Digi provides the dynamic/static hostname **`alacrityhub.go.ro`**, which resolves to the lab's public IP. Both service domains are `CNAME` records pointing at this hostname:

```
wiki.alacrity.ro.   CNAME   alacrityhub.go.ro.   TTL 300
auth.alacrity.ro.   CNAME   alacrityhub.go.ro.   TTL 300
```

A **TTL of 300 seconds (5 minutes)** is recommended. This is low enough to allow reasonably fast failover or IP changes (common with consumer-grade uplinks) while still being high enough to avoid excessive DNS query volume. If the upstream IP is fully static, the TTL can be raised to 3600 (1 h) later.

### 2.2 Disabling Cloudflare CNAME Flattening

By default, Cloudflare flattens `CNAME` records at the zone apex and may also flatten non-apex records when the orange-cloud proxy is enabled. Since `wiki` and `auth` are subdomains (not the apex), the main action required is:

1. Log in to the [Cloudflare Dashboard](https://dash.cloudflare.com) and select the `alacrity.ro` zone.
2. Navigate to **DNS → Records**.
3. For each `CNAME` record (`wiki`, `auth`), ensure the **Proxy status** toggle is set to **DNS only** (grey cloud), not **Proxied** (orange cloud). When the record is DNS-only, Cloudflare returns the raw `CNAME` without flattening or proxying.
4. If the zone is on a plan that exposes the *CNAME Flattening* setting (Business or Enterprise), go to **DNS → Settings** and set CNAME flattening to **Flatten at the zone apex only** (the default). This has no effect on subdomain records but is good hygiene.

> **Why disable the proxy?** Caddy handles TLS termination and certificate management via ACME (Let's Encrypt). If Cloudflare's proxy is active, it will present its own certificate and interfere with Caddy's ACME HTTP-01 challenges, potentially causing certificate issuance failures or double-encryption overhead.

---

## 3 · Application Services

Each service is deployed as a standalone `docker-compose.yaml` stack on Eros.

### 3.1 Authentik — Identity Provider

| | |
|---|---|
| **URL** | `https://auth.alacrity.ro` |
| **Containers** | `authentik-server`, `authentik-worker`, `authentik-postgres` |
| **Purpose** | Centralised authentication and authorisation for all Alacrity services |

#### 3.1.1 Authentication Sources

Account **self-registration is disabled**. All accounts are provisioned by the Alacrity Board. The following authentication methods are supported:

| # | Method | Self-Registration | Notes |
|---|---|---|---|
| **A** | Password (local) | ✗ | Board pre-creates the account *without* a password. The user receives a magic e-mail link to sign in for the first time and is then prompted to set a password. |
| **B** | Discord (social login) | ✗ | Cannot be used to create new accounts. Users link their Discord account from the Authentik *Account Settings* page after initial sign-in, and can then use *Login with Discord* on subsequent visits. |
| **C** | GitHub (social login) | ✗ | Same linking flow as Discord. Particularly convenient for developers. |
| **D** | LucaciResearch Authentik (OAuth2 federation) | ✓ | An existing remote Authentik instance that serves as the directory for **Clockworks** members. Self-registration *is* enabled for this source so that the Alacrity Board does not need to manually synchronise Clockworks account operations. Users arriving through this provider are automatically placed in the **Clockworks Members** group. |

> Methods **B** and **C** are especially useful for **mobile sign-in**, where typing long passwords is inconvenient.

#### 3.1.2 Account Creation Flow

```
Board creates user (no password)
        │
        ▼
User receives magic link via e-mail
        │
        ▼
User clicks link → signed in
        │
        ▼
Prompted to set a password (optional but recommended)
        │
        ▼
User may link Discord / GitHub from Account Settings
```

#### 3.1.3 Groups

Authentik groups partition users for role-based access control:

| Group | Population | Purpose |
|---|---|---|
| **Volunteer** | Alacrity volunteers (post contract signing) | Base access tier for all active volunteers |
| **Board** | Alacrity Board members | Administrative access |
| **Clockworks Members** | Auto-populated via LucaciResearch federation | Access rights specific to Clockworks collaborators |
| **Service** | API accounts (tokens & app passwords) | Machine-to-machine access to protected applications |

#### 3.1.4 Roles & RBAC

Authentik provides a full **Role-Based Access Control** system. Roles are the component that actually grants access: a role encapsulates a set of permissions for a given application, and is then *assigned to one or more groups*. Users never receive permissions directly — they inherit them through their group memberships.

Concrete role definitions for each application are **to be determined** during the deployment phase, once the full set of applications and their permission models are known.

#### 3.1.5 Docker Compose — Reference Structure

```yaml
# /opt/stacks/authentik/docker-compose.yaml
version: "3.8"

services:
  postgresql:
    image: docker.io/library/postgres:16-alpine
    restart: unless-stopped
    volumes:
      - database:/var/lib/postgresql/data
    environment:
      POSTGRES_PASSWORD: ${PG_PASS}
      POSTGRES_USER: authentik
      POSTGRES_DB: authentik

  server:
    image: ghcr.io/goauthentik/server:latest
    restart: unless-stopped
    command: server
    environment:
      AUTHENTIK_REDIS__HOST: redis
      AUTHENTIK_POSTGRESQL__HOST: postgresql
      AUTHENTIK_POSTGRESQL__USER: authentik
      AUTHENTIK_POSTGRESQL__NAME: authentik
      AUTHENTIK_POSTGRESQL__PASSWORD: ${PG_PASS}
      AUTHENTIK_SECRET_KEY: ${AUTHENTIK_SECRET_KEY}
    ports:
      - "127.0.0.1:9000:9000"   # HTTP (proxied by Caddy)
      - "127.0.0.1:9443:9443"   # HTTPS (unused, Caddy terminates TLS)
    depends_on:
      - postgresql
      - redis

  worker:
    image: ghcr.io/goauthentik/server:latest
    restart: unless-stopped
    command: worker
    environment:
      AUTHENTIK_REDIS__HOST: redis
      AUTHENTIK_POSTGRESQL__HOST: postgresql
      AUTHENTIK_POSTGRESQL__USER: authentik
      AUTHENTIK_POSTGRESQL__NAME: authentik
      AUTHENTIK_POSTGRESQL__PASSWORD: ${PG_PASS}
      AUTHENTIK_SECRET_KEY: ${AUTHENTIK_SECRET_KEY}
    depends_on:
      - postgresql
      - redis

  redis:
    image: docker.io/library/redis:alpine
    restart: unless-stopped
    volumes:
      - redis:/data

volumes:
  database:
  redis:
```

> **Note:** Authentik requires a Redis instance alongside PostgreSQL. The Redis container is included in this stack. Environment variables (`PG_PASS`, `AUTHENTIK_SECRET_KEY`) should be defined in a `.env` file alongside the compose file with strict file permissions (`chmod 600`).

---

### 3.2 Wiki.js — Knowledge Base

| | |
|---|---|
| **URL** | `https://wiki.alacrity.ro` |
| **Containers** | `wikijs`, `wikijs-postgres` |
| **Purpose** | Public/private wiki for Alacrity Education |

#### 3.2.1 Authentication

- **Local authentication and password login are disabled.** The only sign-in method is OAuth2, redirecting to `auth.alacrity.ro`.
- Every user who successfully authenticates through Alacrity Authentik is automatically added to the Wiki.js **Editor** group (this is a Wiki.js-internal group, not an Authentik group).

#### 3.2.2 Page Visibility Model

Wiki.js supports granular per-page and per-folder permissions. The two primary audiences are:

| Audience | Wiki.js Group | Capabilities |
|---|---|---|
| **Public visitors** | `Guest` (unauthenticated) | Read public pages only |
| **Signed-in users** | `Editor` | Read all pages; create and edit pages (per their assigned permissions) |

Content authors control visibility at page creation time: a page can be marked as visible to Guests (public) or restricted to Editors only (private). This is the mechanism that makes the wiki a *mixed* public/private knowledge base.

#### 3.2.3 Analytics

Page interactions can optionally be tracked using an external analytics provider such as [Statcounter](https://statcounter.com), [Plausible](https://plausible.io), or [Umami](https://umami.is). Wiki.js supports injecting custom HTML/JS into page headers or footers, which is sufficient for any tag-based analytics solution.

#### 3.2.4 Search & Comments

The deployment will use Wiki.js's **built-in database search engine** and **default comment system**. No external search or comment backends are required at this stage.

#### 3.2.5 Future: Authentik-to-Wiki.js Group Mapping

In the initial deployment, all authenticated users share a single Wiki.js group (Editor). In the future, we will research whether it is possible to map **Authentik roles** (passed as claims in the OAuth2 token) to **Wiki.js groups**, enabling more fine-grained permissions — for example, restricting certain page trees to Board members only, without requiring manual group management inside Wiki.js.

#### 3.2.6 Docker Compose — Reference Structure

```yaml
# /opt/stacks/wikijs/docker-compose.yaml
version: "3.8"

services:
  wikijs:
    image: ghcr.io/requarks/wiki:2
    restart: unless-stopped
    environment:
      DB_TYPE: postgres
      DB_HOST: db
      DB_PORT: 5432
      DB_USER: wikijs
      DB_PASS: ${WIKI_DB_PASS}
      DB_NAME: wikijs
    ports:
      - "127.0.0.1:3000:3000"
    depends_on:
      - db

  db:
    image: docker.io/library/postgres:16-alpine
    restart: unless-stopped
    environment:
      POSTGRES_DB: wikijs
      POSTGRES_USER: wikijs
      POSTGRES_PASSWORD: ${WIKI_DB_PASS}
    volumes:
      - db-data:/var/lib/postgresql/data

volumes:
  db-data:
```

---

## 4 · Caddy Reverse Proxy

Caddy runs **bare-metal** on Eros (not inside Docker). It listens on ports **80** and **443**, automatically obtains and renews TLS certificates from Let's Encrypt via the ACME HTTP-01 challenge, and reverse-proxies requests to the appropriate Docker service based on the `Host` header.

### 4.1 Installation (Arch Linux)

```bash
sudo pacman -S caddy
sudo systemctl enable --now caddy
```

### 4.2 Caddyfile

```caddyfile
# /etc/caddy/Caddyfile

auth.alacrity.ro {
    reverse_proxy 127.0.0.1:9000
}

wiki.alacrity.ro {
    reverse_proxy 127.0.0.1:3000
}
```

This is the complete configuration. Caddy infers HTTPS, provisions certificates, and handles HTTP→HTTPS redirection automatically.

---

## 5 · Architecture Diagram

```kroki
blockdiag {
  orientation = portrait;

  Internet [label = "Internet"];
  Cloudflare [label = "Cloudflare DNS\n(DNS-only, no proxy)"];
  MikroTik [label = "MikroTik Router\nPort Fwd 80/443"];
  Caddy [label = "Caddy\n(bare-metal)\n:80 / :443"];
  Authentik [label = "Authentik\n:9000"];
  WikiJS [label = "Wiki.js\n:3000"];
  AuthPG [label = "Postgres\n(Authentik)"];
  WikiPG [label = "Postgres\n(Wiki.js)"];
  Redis [label = "Redis\n(Authentik)"];
  LR [label = "LucaciResearch\nAuthentik\n(remote)"];

  Internet -> Cloudflare -> MikroTik -> Caddy;
  Caddy -> Authentik;
  Caddy -> WikiJS;
  Authentik -> AuthPG;
  Authentik -> Redis;
  WikiJS -> WikiPG;
  WikiJS -> Authentik [label = "OAuth2"];
  Authentik -> LR [label = "OAuth2\nFederation"];
}
```

> *If your Wiki.js instance does not have the Kroki renderer enabled, the diagram above can be replaced with a Mermaid block or a static image.*

**Simplified Mermaid alternative:**

```mermaid
flowchart TD
    A[Internet] --> B[Cloudflare DNS — DNS only]
    B --> C[MikroTik Router — Port Fwd 80/443]
    C --> D[Caddy — bare-metal on Eros — :80/:443]
    D -->|auth.alacrity.ro| E[Authentik :9000]
    D -->|wiki.alacrity.ro| F[Wiki.js :3000]
    E --> G[(Postgres — Authentik)]
    E --> H[(Redis)]
    F --> I[(Postgres — Wiki.js)]
    F -.->|OAuth2| E
    E -.->|OAuth2 Federation| J[LucaciResearch Authentik — remote]
```

---

## 6 · Scalability to More Services

The Authentik instance deployed on Eros is not limited to the wiki — it is designed to serve as the **single sign-on (SSO) provider for all Alacrity Education services**, current and future.

### 6.1 Supported Protocols

Authentik supports a wide range of authentication and authorisation protocols out of the box:

- **OAuth2 / OpenID Connect** — used by Wiki.js and most modern web applications.
- **SAML 2.0** — for enterprise or legacy applications that require SAML assertions.
- **LDAP** — Authentik can expose an LDAP interface, useful for services that only support directory-based authentication (e.g., Gitea, Portainer, some network appliances).
- **RADIUS** — for network access control (802.1X, VPN).
- **SCIM** — for automated user provisioning and de-provisioning in supported applications.
- **Forward Auth / Proxy Authentication** — Authentik can act as an authentication middleware in front of any HTTP service (see below).

### 6.2 Protected Reverse Proxy

For applications that have no built-in SSO support, Authentik's **Proxy Provider** can be placed in front of the service. In this mode, Caddy forwards the authentication decision to Authentik, and only passes the request through to the upstream service if the user has a valid session. This means virtually *any* web application can be protected with Alacrity SSO, even if it has no authentication system of its own.

### 6.3 Hosting Additional Services

Eros has sufficient headroom (i3-8100, 16 GB RAM, 500 GB SSD) to host additional lightweight services alongside Authentik and Wiki.js. Each new service would follow the same pattern:

1. Deploy as a new Docker Compose stack under `/opt/stacks/<service>/`.
2. Register an OAuth2/OIDC (or SAML/LDAP) application in Authentik.
3. Create a DNS `CNAME` record (`<service>.alacrity.ro → alacrityhub.go.ro`).
4. Add a `reverse_proxy` directive to the Caddyfile.
5. Assign appropriate Authentik roles to the relevant groups.

This pattern keeps the operational model consistent and predictable as the platform grows.

---

## Appendix A — Port & Service Summary

| Service | Listen Address | Protocol | Exposed via Caddy |
|---|---|---|---|
| Caddy | `0.0.0.0:80`, `0.0.0.0:443` | HTTP / HTTPS | — (is the proxy) |
| Authentik Server | `127.0.0.1:9000` | HTTP | `auth.alacrity.ro` |
| Wiki.js | `127.0.0.1:3000` | HTTP | `wiki.alacrity.ro` |
| Authentik Postgres | Docker-internal | TCP/5432 | No |
| Authentik Redis | Docker-internal | TCP/6379 | No |
| Wiki.js Postgres | Docker-internal | TCP/5432 | No |

## Appendix B — Backup Considerations

At a minimum, the following data should be included in a regular backup schedule:

- **Authentik PostgreSQL database** — contains all user accounts, groups, roles, and application configurations.
- **Wiki.js PostgreSQL database** — contains all page content, permissions, and settings.
- **Docker Compose files and `.env` secrets** (`/opt/stacks/`).
- **Caddyfile** (`/etc/caddy/Caddyfile`).

A simple approach is a nightly `pg_dump` for each database, combined with a file-level backup of `/opt/stacks/` and `/etc/caddy/`, pushed to an off-site location.