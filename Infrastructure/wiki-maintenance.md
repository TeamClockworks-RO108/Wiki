---
title: Wiki Maintenance
description: 
published: true
date: 2026-02-24T19:23:29.219Z
tags: 
editor: markdown
dateCreated: 2026-02-24T19:13:23.255Z
---

# Set timezone to all users

The timezone is initialized as New York by default for all users. 
To fix this, regularly connect to the Postgres database and run the following query:

```sql
UPDATE users SET timezone = 'Europe/Bucharest' WHERE timezone IS DISTINCT FROM 'Europe/Bucharest';
```

---

Another untested solution from [Wiki.js forums](https://requarks.canny.io/wiki/p/select-date-format-and-time-zone-for-the-entire-site) would be to seet the default column type. 

```sql
ALTER TABLE users ALTER COLUMN timezone SET DEFAULT 'Europe/Bucharest';
```