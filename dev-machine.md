---
title: Dev Machine
description: 
published: true
date: 2026-01-12T02:32:33.592Z
tags: programming, infrastructure
editor: markdown
dateCreated: 2025-08-02T14:25:30.841Z
---

# Dev Machine
The dev machine is a linux server you can SSH into and do remote development from.
Access is given on a neet-to-have basis. Ask Alex to enter your SSH key into the machine if you need remote development. 

Append the below section in your `~/.ssh/config` file. 
```ssh-config
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


