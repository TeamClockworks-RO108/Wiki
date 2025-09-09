---
title: Starkiller
description: Gobilda planetary transformer
published: true
date: 2025-09-09T01:53:27.037Z
tags: 
editor: markdown
dateCreated: 2025-09-09T01:20:59.160Z
---

# Description

Starkiller is a 3D printed file that allows a Gobilda Yellow Jacket 84 RPM motor to transform to any of the following speeds: 6000 RPM, 1620 RPM, 1150 RPM, 435 RPM, 312 RPM. It works by replacing parts of the planetary gearbox with fixed stages. 

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

| Stages | Motor | Stage 1 | Stage 2 | Stage 3 | Shaft |
| -- |
| **Sun gear** | | 17 | 11 | 17 | |
| **Ratio** |  | 3.7 | 5.2 | 3.7 | | 


# Motor Modding

To obtain different configuration, we can lock one or more of the planetary stages to 1:1 ratio.

| Output RPM | 84  | 312  | 435  | 1150  | 1620  | 6000  |
| --- | --- | --- | --- | --- | --- | --- | 
| Stage 3 (Shaft) | :ballot_box_with_check: | :ballot_box_with_check: | :ballot_box_with_check: | Replace with `SK11717` | :ballot_box_with_check: | :stop_sign: |
| Stage 2 | :ballot_box_with_check: | :ballot_box_with_check: | Replace with `SK11111` | :ballot_box_with_check: | :stop_sign: | :stop_sign: |
| Stage 1 (Motor)| :ballot_box_with_check: | Replace with `SK11717` | :ballot_box_with_check: | Replace with `SK11717` | Replace with `SK21117` | Replace with `SK31717` |

# Configuring the CAD

The CAD file contains lots of parameters that can be configured. The most important are set to favourites and should be configured to your setup:

![screenshot_20250909_043537.png](/screenshot_20250909_043537.png)

| Parameter | Meaning |
| --- | --- |
| `stages` | Number of stages to replace (`N` variable) |
| `bottomStageTeeth` | Number of teeth on the bottom stage sun gear (`B` variable) |
| `topStageTeeth` | Number of teeth on the bottom stage sun gear (`T` variable) |
| `bottomStageHoleRadiusOffset` | A radius offset added to bottom gear hole, to aid with tolerance and part fir |
| `prongHoleRadiusOffset` | A radius offset added to top prongs hole, to aid with tolerance and part fit |
| `bridgeExtraRoom` | Amount of material to remove at the end of holes to compensate bridge sag |
| `gearInsertHeight` | Height of the tooth making contact with the bottom gear |
| `gearInsertPcOfAngle` | How thick the tooth making contact with the bottom gear should be. Must be between 0 and 1. |

## Example CAD configurations

| `SK11111` | `SK11717` | `SK21117` | `SK21711` | `SK31717` |
| -- |
| ![sk11111.png](/sk11111.png) | ![sk11717.png](/sk11717.png) | ![sk21117.png](/sk21117.png) | ![sk21711.png](/sk21711.png) | ![sk31717.png](/sk31717.png) |



