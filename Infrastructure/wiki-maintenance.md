---
title: Wiki Maintenance
description: 
published: true
date: 2026-04-06T23:12:50.578Z
tags: 
editor: markdown
dateCreated: 2026-02-24T19:13:23.255Z
---

# Set timezone to all users

The timezone is initialized as New York by default for all users. 
To fix this, connect to the postgres database and run SQL commands to set the timezone for everyone and then set the default to the correct timezone:

```bash
docker exec -it wiki psql -U wikijs -d wiki
```
Type the following SQL and hit enter:
```sql
ALTER TABLE users ALTER COLUMN timezone SET DEFAULT 'Europe/Bucharest';
UPDATE users SET timezone = 'Europe/Bucharest' WHERE timezone IS DISTINCT FROM 'Europe/Bucharest';
```
