---
title: Spoolman Authentication
description: 
published: true
date: 2026-01-12T02:34:33.356Z
tags: infrastructure, 3dprinting, project
editor: markdown
dateCreated: 2025-12-15T03:10:53.706Z
---

# Authentication

The spoolman instance is protected by a reverse-proxy module of Caddy/Authentik.
An api key is given inside the `X-Api-Key` header that is moved by caddy inside the `Authorization: Basic <X-Api-Key>` header that Authentik can understand.

The `X-Api-Key` contains the base64-encoded combo of `username:password` that is generated in the `Tokens and App passwords` section of Authentik.

To attach this api key, a local dns trick is used on the printer hosts to redirect the main domain to a nginx proxy that adds the required token.



### Inside the outbound proxy host

Create a secondary domain CNAME that links and redirects to the first, inside the outbound proxy host(s).

```dig
spoolman-intl.lucres.net. 86400 IN      CNAME   spoolman.lucres.net.
spoolman.lucres.net.      86400 IN      A       10.2.2.4
```

```caddy
spoolman-intl.lucres.net {                                                                           
    redir https://spoolman.lucres.net{uri} permanent                                                 
}
```


For reference, the caddy copying logic will look something like this:
```caddy
(authentik) {                                                                                       
    header Access-Control-Allow-Origin *                                                           
    forward_auth {args.0} {                                                                         
        uri /outpost.goauthentik.io/auth/caddy                                             
        trusted_proxies private_ranges                                                             
        header_up +Authorization "Basic {http.request.header.X-Api-Key}"                           
        copy_headers X-Authentik-Username X-Authentik-Groups X-Authentik-Email X-Authentik-Name X-Authentik-Uid X-Authentik-Jwt X-Authentik-Meta-Jwks X-Authentik-Meta-Outpost X-Authentik-Meta-Provide
r X-Authentik-Meta-App X-Authentik-Meta-Version
        }
    reverse_proxy /outpost.goauthentik.io/* {args.0} {
    }
}
```

### Inside the printer config

Add the dns override to `/etc/hosts`. Install and enable dnsmasq.

```diff
127.0.0.1       localhost
::1             localhost ip6-localhost ip6-loopback
ff02::1         ip6-allnodes
ff02::2         ip6-allrouters

127.0.1.1       medina
+127.0.0.1       spoolman-intl.lucres.net
```

```bash
sudo apt install dnsmasq
sudo systemctl enable --now dnsmasq
```

Create the nginx config inside `/etc/nginx/sites-available/spoolman` and enable it.

```nginx
server {
    listen 80;
    server_name spoolman-intl.lucres.net;


    location / {

        set $upt https;
        set $ust spoolman.lucres.net;
        resolver localhost;

        proxy_pass $upt://$ust;
        proxy_set_header X-Api-Key "REDACTED BASE64 ENCODED TOKEN OF USERNAME:PASSWORD";
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
        proxy_read_timeout 86400;
        proxy_send_timeout 86400;
        proxy_ssl_server_name on;
        proxy_ssl_name $ust;
        proxy_set_header Host $ust;
    }
}
```

```bash
sudo ln -s /etc/nginx/sites-available/spoolman /etc/nginx/sites-enabled/spoolman
sudo systemctl restart nginx
```

To create the base64-encoded token, use the following command:

```bash
echo -n 'username:password' | base64 --wrap=9999
```

Configure the printer to point to our fake domain inside `moonraker.conf`.

```ini
[spoolman]
server: http://spoolman-intl.lucres.net
sync_rate: 5
```

# Automation

An ansible playbook is available in our [Gtihub repository](https://github.com/TeamClockworks-RO108/KlipperScripts) that automates the printer config creation. To run it, verify the correct hosts are configured inside `inventory.yaml`.

Also ensure that the correct values are configured inside the `variables.yaml` file:

```yaml
spoolman_api_key: EXAMPLE_CHANGE_ME_LMAO
spoolman_domain: spoolman.lucres.net
spoolman_domain_secondary: spoolman-intl.lucres.net

```

Run the playbook like so:

```bash
# Run for all hosts
ansible-playbook -i inventory.yaml -e @variables.yaml configure_spoolman.yaml

# Limit to only a few
ansible-playbook -i inventory.yaml -e @variables.yaml configure_spoolman.yaml --limit iron,medina
```

> The `inventory.yaml` and `variables.yaml` files can contain sensitive credentials, so it is best to ensure that you will never be able to commit and push these files. It is possible to configure git to ignore them completely. Use this procedure after cloning: 
> ```bash
> 
> cd KlipperScripts/spoolman
> 
> # Completely ignore files
> git update-index --skip-worktree inventory.yaml variables.yaml
> 
> # Revert back to original behaviour (able to commit)
> git update-index --no-skip-worktree inventory.yaml variables.yaml
> ```
<!-- {blockquote:.is-info} -->





