---
title: Pulumi
description: 
published: true
date: 2026-06-04T01:08:12.413Z
tags: 
editor: markdown
dateCreated: 2026-04-06T23:26:42.076Z
---

# Wipe all pulumi resources by a prefix

Can happen that pulumi loses connection details and resources need to be wiped en-masse. In this example `A-` is the prefix we're searching for.


```bash
export PULUMI_CONFIG_PASSPHRASE=...
pulumi stack --show-urns | grep URN | grep A- | awk '{print $3}' | xargs -I {} pulumi state delete {}
```

