---
title: Planetary Starkiller
description: Gobilda planetary transformer
published: true
date: 2025-09-10T00:59:26.321Z
tags: 
editor: markdown
dateCreated: 2025-09-09T01:20:59.160Z
---

# Description

Starkiller is a 3D printed file that allows a Gobilda Yellow Jacket 84 RPM motor to transform to any of the following speeds: 6000 RPM, 1620 RPM, 1150 RPM, 435 RPM, 312 RPM. It works by replacing parts of the planetary gearbox with fixed stages. 

The system also fits any other planetary gearbox from gobilda (not neccessarily the 84 RPM one) but we have selected the 84 RPM motor as the main focus because its planetary configuration can produce most of the other options.

The CAD is licensed under [GNU General Public License Version 3](https://www.gnu.org/licenses/gpl-3.0.en.html). This means, among others, that distributing either STL, printed parts or assemblies containing Starkiller, you must also make the modified CAD available to users. In the case of assemblies (derivative works), the whole assembly must be also licensed under the same license of Starkiller.  

The repository for this project can be found [:github: here](https://github.com/TeamClockworks-RO108/PlanetaryStarkiller). 

# Part types

The Starkiller parts use the follosing maning scheme: `SK{N}{T}{B}`
Variables `N` `T` and `B` configure the different options:

| Name variable | Meaning | Possible values |
| --- | --- | --- |
| N | Number of stages to replace | 1-3 |
| T | Number of teeth of the sun gear of the **top** stage (towards the **shaft**) | 11, 17 |
| B | Number of teeth of the sun gear of the **bottom** (towards the **motor**) | 11, 17 |

> If N is 1, then B and T must be the same as we are replacing a single planetary stage. It is not possible to have, for example, part SK11117 or SK11711.
{.is-info}


# Motor Modding and Configuration

To obtain different configuration, we can lock one or more of the planetary stages to 1:1 ratio.

## 84 RPM Motor

| Output RPM | 84  | 312  | 435  | 1150  | 1620  | 6000  |
| --- | --- | --- | --- | --- | --- | --- | 
| Stage 3 (Shaft) <br> 17T 3.7:1 | :ballot_box_with_check: | :ballot_box_with_check: | :ballot_box_with_check: | :hammer_and_wrench: Replace with `SK11717` | :ballot_box_with_check: | :stop_sign: Remove |
| Stage 2 <br> 11T 5.2:1 | :ballot_box_with_check: | :ballot_box_with_check: | :hammer_and_wrench: Replace with `SK11111` | :ballot_box_with_check: | :stop_sign: Remove | :stop_sign: Remove |
| Stage 1 (Motor) <br> 17T 3.7:1 | :ballot_box_with_check: | :hammer_and_wrench: Replace with `SK11717` | :ballot_box_with_check: | :hammer_and_wrench: Replace with `SK11717` | :hammer_and_wrench: Replace with `SK21117` | :hammer_and_wrench: Replace with `SK31717` |

## 117 RPM Motor

| Output RPM | 117  | 435  | 1620  |  6000  |
| --- | --- | --- | --- | --- | 
| Stage 3 (Shaft) <br> 17T 3.7:1 | :ballot_box_with_check: | :ballot_box_with_check: | :ballot_box_with_check: | :stop_sign: Remove |
| Stage 2 <br> 17T 3.7:1 | :ballot_box_with_check: | :ballot_box_with_check: | :stop_sign: Remove | :stop_sign: Remove |
| Stage 1 (Motor) <br> 17T 3.7:1 | :ballot_box_with_check: | :hammer_and_wrench: Replace with `SK11717` | :hammer_and_wrench: Replace with `SK21717` | :hammer_and_wrench: Replace with `SK31717` | 


## 223 RPM Motor

| Output RPM | 223 | 1150 | 6000 | 
| --- | --- | --- | --- |
| Stage 2 (Shaft) <br> 11T 5.1:1 | :ballot_box_with_check: | :ballot_box_with_check: | :stop_sign: Remove |
| Stage 1 (Motor) <br> 11T 5.2:1 | :ballot_box_with_check: | :hammer_and_wrench: Replace with `SK11111` | :hammer_and_wrench: Replace with `SK21111` |

## 312 RPM Motor

| Output RPM | 312 | 1150 | 1620 | 6000 | 
| --- | --- | --- | --- | --- |
| Stage 2 (Shaft) <br> 17T 3.7:1 | :ballot_box_with_check: | :hammer_and_wrench: Replace with `SK11717` | :ballot_box_with_check: | :stop_sign: Remove |
| Stage 1 (Motor) <br> 11T 5.2:1 | :ballot_box_with_check: | :ballot_box_with_check: | :hammer_and_wrench: Replace with `SK11111` | :hammer_and_wrench: Replace with `SK21711` |


## 435 RPM Motor

| Output RPM | 435 | 1620 | 6000 |
| --- | --- | --- | --- |
| Stage 2 (Shaft) <br> 17T 3.7:1 | :ballot_box_with_check: | :ballot_box_with_check: | :stop_sign: Remove |
| Stage 1 (Motor) <br> 17T 3.7:1 | :ballot_box_with_check: | :hammer_and_wrench: Replace with `SK11717` | :hammer_and_wrench: Replace with `SK21717` |

## 1150 RPM Motor
| Output RPM | 1150 | 6000 |
| --- | --- | --- |
| Stage 1 <br> 11T 5.2:1 | :ballot_box_with_check: | :hammer_and_wrench: Replace with `SK11111` |

## 1620 RPM Motor
| Output RPM | 1620 | 6000 |
| --- | --- | --- |
| Stage 1 <br> 17T 3.7:1 | :ballot_box_with_check: | :hammer_and_wrench: Replace with `SK11717` |

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

You do not need to set the N, T and B variables manually in the Parameters window. You can use the Configuration menu to switch between part profiles. This setting only changes the first three parameters described above and is a shortcut to switch between the different part numbers.

| ![screenshot_20250910_033509.png](/screenshot_20250910_033509.png) |
| --- |

## Example CAD configurations

| `SK11111` | `SK11717` | `SK21117` | `SK21711` | `SK31111` | `SK31717` |
| -- |
| ![sk11111.png](/sk11111.png) | ![sk11717.png](/sk11717.png) | ![sk21117.png](/sk21117.png) | ![sk21711.png](/sk21711.png) | ![sk31111.png](/sk31111.png) | ![sk31717.png](/sk31717.png) |

## Print settings

> We **STRONGLY** recommend that you tune your tolerances by modifying the CAD parameters. If you **MUST** use the pre-exported STL files to print, use the horizontal expansion (often also called XY compensation) setting in your slicer to adjust the fit. Prioritize getting a good fit for the bottom gear. Loose prongs are OK (will just introduce play) but a loose gear will not work. 
> In the future, we will provide STL's with oversized prong holes for cases where a good gear fit will mean the prong holes are much to small. 
{.is-warning}


To properly assemble, we must tailor the tolerances to your printer. We want a good contact with the gears without any backlask or too much tightness. 
Having the print too tight around the gear can cause the gear to "dig" into one side of the print and sit off-center. Backlash on the gear will cause the fit to wear over time and become loose. 

You should first calibrate your 17T gear fit. Print the `SK11717`, adjusting the `bottomStageHoleRadiusOffset` CAD parameter until it fits. After you get a good fit (relatively tight, not require hammer or power tools to assemble, no play) you can move on to calibrate the 11T gear fit using the `SK11111` configuration and adjusting `bottomStageHoleSmallGearRadiusOffsetComp`.

While calibrating the 17T and 11T gears, you can also adjust `prongHoleRadiusOffset` to calibrate the planetary prongs hole size. Same rules apply here: no play, easy to assemble by hand.

If your printer has very aggressive smoothing due to input shapers, you can decrease `gearInsertPcOfAngle` to about 0.7 to get sharper teeth in the internal gear. 

## Print orientation

ABS is strongly recommended for this application. It has both wear and temperature resistance. It is not unusual for FTC motors to get hot, and we fear that PLA might soften and fail.

The `SK1` series parts cand be printed flat on the bed on nearly any orientation. We prefer to print them exactly as in CAD, as the first layer squish can be compensated by the chamfer of the bottom gear.

The `SK2` and `SK3` series must be printed upside-down due to having a hole at the center. The hole makes it easy to remove the gear when dissasembling the modded gearbox by pushing with a M4 screw. 

A high (5-6) number of walls is recommended. To ensure stability at high RPM's, the infill should be as uniform as possible. We suggest going for Gyroid 30% with a small line width (105% of nozzle size). No supports are required for any configuration.

Set the seam placing mode to aligned. This will place the seam in the teardrop shape of the prongs hole and improve tolerances for prong contact. 

# Example modded motor

| Conversion from 84 RPM to 435 RPM by replacing the center planetary with `SK11111` | Conversion from 84 RPM to 6000 RPM by replacing all the stages with `SK31717` |
| --- | --- |
| ![whatsapp_image_2025-09-09_at_11.41.19_pm.jpeg](/whatsapp_image_2025-09-09_at_11.41.19_pm.jpeg) | ![a621a223-65ee-466a-a40c-f7464d2646ec.jpeg](/a621a223-65ee-466a-a40c-f7464d2646ec.jpeg) |


