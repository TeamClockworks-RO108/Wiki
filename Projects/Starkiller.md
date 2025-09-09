---
title: Starkiller
description: Gobilda planetary transformer
published: true
date: 2025-09-09T01:20:59.160Z
tags: 
editor: markdown
dateCreated: 2025-09-09T01:20:59.160Z
---

# Description

Starkiller is a 3D printed file that allows a Gobilda Yellow Jacket 84 RPM motor to transform to any of the following speeds: 1620 RPM, 1150 RPM, 435 RPM, 312 RPM. It works by replacing parts of the planetary gearbox with fixed stages. 

# Part types

The Starkiller parts use the follosing maning scheme: `SK{N}{T}{B}`
Variables `N` `T` and `B` configure the different options:

| Name variable | Meaning | Possible values |
| --- | --- | --- |
| N | Number of stages to replace | 1-3 |
| T | Number of teeth of the sun gear of the **top** stage (towards the **output**) | 11, 17 |
| B | Number of teeth of the sun gear of the **bottom** (towards the **motor**) | 11, 17 |

# 84 Motor Configuration

The 84 RPM motor has the following planetary configuration:

| Stage | Sun teeth | Ratio | 
| --- | --- | --- |
| Output Shaft | | |
| **3** | 17 | 3.7 | 
| **2** | 11 | 5.18 |
| **1** | 17 | 3.7 | 
| Motor | | | 

# Motor Modding

To obtain different configuration, we can lock one or more of the planetary stages to 1:1 ratio.

| Output RPM | 84  | 312  | 435  | 1150  | 1620  | 6000  |
| --- | --- | --- | --- | --- | --- | --- | 
| Stage 3 | :ballot_box_with_check: | :ballot_box_with_check: | :ballot_box_with_check: | Replace with `SK11717` | :ballot_box_with_check: | :stop_sign: |
| Stage 2 | :ballot_box_with_check: | :ballot_box_with_check: | Replace with `SK11111` | :ballot_box_with_check: | :stop_sign: | :stop_sign: |
| Stage 1 | :ballot_box_with_check: | Replace with `SK11717` | :ballot_box_with_check: | Replace with `SK11717` | Replace with `SK21117` | Replace with `SK31717` |
