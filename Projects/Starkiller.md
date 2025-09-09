---
title: Planetary Starkiller
description: Gobilda planetary transformer
published: true
date: 2025-09-09T20:50:37.880Z
tags: 
editor: markdown
dateCreated: 2025-09-09T01:20:59.160Z
---

# Description

Starkiller is a 3D printed file that allows a Gobilda Yellow Jacket 84 RPM motor to transform to any of the following speeds: 6000 RPM, 1620 RPM, 1150 RPM, 435 RPM, 312 RPM. It works by replacing parts of the planetary gearbox with fixed stages. 

The CAD is licensed under [GNU General Public License Version 3](https://www.gnu.org/licenses/gpl-3.0.en.html). This means, among others, that distributing either STL, printed parts or assemblies containing Starkiller, you must also make the modified CAD available to users. In the case of assemblies (derivative works), the whole assembly must be also licensed under the same license of Starkiller.  

# Part types

The Starkiller parts use the follosing maning scheme: `SK{N}{T}{B}`
Variables `N` `T` and `B` configure the different options:

| Name variable | Meaning | Possible values |
| --- | --- | --- |
| N | Number of stages to replace | 1-3 |
| T | Number of teeth of the sun gear of the **top** stage (towards the **output**) | 11, 17 |
| B | Number of teeth of the sun gear of the **bottom** (towards the **motor**) | 11, 17 |

> If N is 1, then B and T must be the same as we are replacing a single planetary stage. It is not possible to have, for example, part SK11117 or SK11711.
{.is-warning}


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
| Stage 3 (Shaft) | :ballot_box_with_check: | :ballot_box_with_check: | :ballot_box_with_check: | :hammer_and_wrench: Replace with `SK11717` | :ballot_box_with_check: | :stop_sign: Remove |
| Stage 2 | :ballot_box_with_check: | :ballot_box_with_check: | :hammer_and_wrench: Replace with `SK11111` | :ballot_box_with_check: | :stop_sign: Remove | :stop_sign: Remove |
| Stage 1 (Motor)| :ballot_box_with_check: | :hammer_and_wrench: Replace with `SK11717` | :ballot_box_with_check: | :hammer_and_wrench: Replace with `SK11717` | :hammer_and_wrench: Replace with `SK21117` | :hammer_and_wrench: Replace with `SK31717` |

# Configuring the CAD

We recomend that you grab the CAD file from our [github repository](https://github.com/TeamClockworks-RO108/PlanetaryStarkiller). Even though we also provide STL files, the tolerances might not fit well depending on your printer and you might have to re-configure the CAD for your specific setup. 

The CAD file contains lots of parameters that can be configured. The most important are set to favourites and should be configured to your setup:

![screenshot_20250909_043537.png](/screenshot_20250909_043537.png)

| Parameter | Meaning |
| --- | --- |
| `stages` | Number of stages to replace (`N` variable) |
| `bottomStageTeeth` | Number of teeth on the bottom stage sun gear (`B` variable) |
| `topStageTeeth` | Number of teeth on the bottom stage sun gear (`T` variable) |
| `bottomStageHoleRadiusOffset` | A radius offset added to bottom gear hole, to aid with tolerance and part fir |
| `prongHoleRadiusOffset` | A radius offset added to top prongs hole, to aid with tolerance and part fit |
| `bottomStageHoleSmallGearRadiusOffsetComp` | A radius offset added to bottom gear hole only for the 11T variant |
| `bridgeExtraRoom` | Amount of material to remove at the end of holes to compensate bridge sag |
| `gearInsertHeight` | Height of the tooth making contact with the bottom gear |
| `gearInsertPcOfAngle` | How thick the tooth making contact with the bottom gear should be. Must be between 0 and 1. |

> Fusion360 will show warnings and errors when switching from `N=1` to `N=2|3` and back. These warnings and errors are safe to ignore. They happen because various features are present only in one of the configurations, and the CAD file is designed to produce all of the configurations.
{.is-info}


## Example CAD configurations

| `SK11111` | `SK11717` | `SK21117` | `SK21711` | `SK31111` | `SK31717` |
| -- |
| ![sk11111.png](/sk11111.png) | ![sk11717.png](/sk11717.png) | ![sk21117.png](/sk21117.png) | ![sk21711.png](/sk21711.png) | ![sk31111.png](/sk31111.png) | ![sk31717.png](/sk31717.png) |

## Print settings

To properly assemble, we must tailor the tolerances to your printer. We want a good contact with the gears without any backlask or too much tightness. 
Having the print too tight around the gear can cause the gear to "dig" into one side of the print and sit off-center. Backlash will cause the fit to wear over time and become loose. 

You should first calibrate your 17T gear fit. Print the `SK11717`, adjusting the `bottomStageHoleRadiusOffset` CAD parameter until it fits. After you get a good fit (relatively tight, not require hammer or power tools to assemble, no play) you can move on to calibrate the 11T gear fit using the `SK11111` configuration and adjusting `bottomStageHoleSmallGearRadiusOffsetComp`.

While calibrating the 17T and 11T gears, you can also adjust `prongHoleRadiusOffset` to calibrate the planetary prongs hole size. Same rules apply here: no play, easy to assemble by hand.

## Print orientation

ABS is strongly recommended for this application. It has both wear and temperature resistance. It is not unusual for FTC motors to get hot, and we fear that PLA might soften and fail.

The `SK1` series parts cand be printed flat on the bed on nearly any orientation. We prefer to print them exactly as in CAD, as the first layer squish can be compensated by the chamfer of the bottom gear.

The `SK2` and `SK3` series must be printed upside-down due to having a hole at the center. The hole makes it easy to remove the gear when dissasembling the modded gearbox by pushing with a M4 screw. 

A high (5-6) number of walls is recommended. To ensure stability at high RPM's, the infill should be as uniform as possible. We suggest going for Gyroid 30% with a small line width (105% of nozzle size). No supports are required for any configuration.

Set the seam placing mode to aligned. This will place the seam in the teardrop shape of the prongs hole and improve tolerances for prong contact. 

# Example modded motor

Here we have modded a 84 RPM motor to provide 435 RPM by replacing the center planetary stage with `SK11111`. The motor is shown without the planetary jacket.

![whatsapp_image_2025-09-09_at_11.41.19_pm.jpeg](/whatsapp_image_2025-09-09_at_11.41.19_pm.jpeg)


