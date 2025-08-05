---
title: Dev Machine
description: 
published: true
date: 2025-08-05T07:37:54.681Z
tags: 
editor: markdown
dateCreated: 2025-08-02T14:25:30.841Z
---

# Dev Machine
The dev machine is a linux server you can SSH into and do remote development from.

Append the below section in your `~/.ssh/config` file. 
``` SSH config
Host cdm.lucres.net
    User clock
    Hostname cdm.lucres.net
    IdentitiesOnly yes
    IdentityFile ~/.ssh/id_ed25519
```

And connect to the machine:

```
ssh cdm.lucres.net
```

You will be greeted with a terminal. If the icons appear broken, it's reccomended to install [this font pack](https://archlinux.org/groups/x86_64/nerd-fonts/):

![screenshot_20250805_103640.png](/screenshot_20250805_103640.png)