---
title: Voron Mods
description: 
published: true
date: 2026-01-13T02:15:57.987Z
tags: programming, mechanics, project, voron, modding
editor: markdown
dateCreated: 2025-11-29T17:15:50.895Z
---

# KlipperScripts

[![Static Badge](https://img.shields.io/badge/github-repo-brightgreen?style=for-the-badge&logo=git&logoColor=white&logoSize=auto)](https://github.com/TeamClockworks-RO108/KlipperScripts)

All our Klipper printers are running a common set of macros. They are written to be heavily configurable for every printer model and capabilities. Some of the features covered are:
 * Print start and end procedures, together with handling of mesh, cartographer/beacon touch mode, heating, chamber heatsoaking and a very fancy purge line.
 * Basic spoolman macros.
 * Status RGB(W) LED with configurable color maps and strip selection.
 * Chamber LED handler, both for analog and boolean strips.
 * Development helpers to dump or search trough values in the `printer` object.
 
We also ship an ansible playbook that aids in mass deployment of our proxy-protected spoolman connector. A technical writeup is available on [this page](https://wiki.teamclockworks.ro/en/Infrastructure/spoolman-auth).

# FilametrixAxon

[![Static Badge](https://img.shields.io/badge/github-repo-brightgreen?style=for-the-badge&logo=git&logoColor=white&logoSize=auto)](https://github.com/TeamClockworks-RO108/FilametrixAxon) [![Static Badge](https://img.shields.io/badge/printables-click-orange?style=for-the-badge&logo=printables&logoColor=white&logoSize=auto)](https://www.printables.com/model/1452934-voron-filametrix-axon-servo-actuated-depressor)

This mod modifies the gatry-mounted servo-actuated Filametrix depressor to allow the usage of a Axon Micro servo. The original SG90/MG90 servo can break very easily in case of a toolhead crash. They also do not tolerate heat very well.

The Axon is a bit larger in size then the cheap chinese models and also comes with a B25T metal horn spline. The horn doesn't quite fit the original project's specifications, therefore we have redesigned the whole assembly. 

The cutter is much faster and silent after this change :). 

| ![frontclosed.png](/frontclosed.png) | ![frontopen.png](/frontopen.png) |
| -- | -- |


# Stepper Blobifier

[![Static Badge](https://img.shields.io/badge/github-pr%20open-brightgreen?style=for-the-badge&logo=git&logoColor=white&logoSize=auto)](https://github.com/Carrot-collective/Blobifier/pull/49) [![Static Badge](https://img.shields.io/badge/printables-click-orange?style=for-the-badge&logo=printables&logoColor=white&logoSize=auto)](https://www.printables.com/model/1484215-stepper-blobifier)

We have found that cheap MG90/SG90 servo motors can die pretty fast from bed heat, therefore we developed the option to use a pancake stepper motor instead.

This model uses a small GT2 belt as a toothed rack to move the blobifier's tray back and forth. To make room for a stepper motor, the blobifier assembly is risen by 2mm. This should not be an issue on most setups, but depending how your bottom panel sits, it might collide with the shaker arm. To solve this, a redesigned shaker arm is provided.

Extensive modidications need to be done to the blobifier configurations to a stepper motor in place of a servo. Steppers need to be homes to be accurately moved. For this purpose, tried to use sensorless homing but found it too unreliable on pancake steppers on out TMC2130 driver. Adding a second microswitch to the blobifier body would be a nice solution, but would would require extra wiring. In the end, we have settles to ram the tray against the mechanical limit, and because of the low stepper current, there is little vibration produced. 

We reccomend to browse the assembly and configuration instructions on the Github PR tree.

| ![blobifier-render.png](/blobifier-render.png =50%x50%) |
| -- |

# Parametric LED Bar

[![Static Badge](https://img.shields.io/badge/printables-click-orange?style=for-the-badge&logo=printables&logoColor=white&logoSize=auto)](https://www.printables.com/model/1554185-parametric-led-bar)

This model is a LED bar holder with integrated grate diffuser. It is designed for standard LED strips that are 10mm wide and can be cut at 25mm segments. We use it with dense strips (240 LEDs per meter).

You will need 8x 6mm M3 BHCS and appropiate channel nuts to assemble. 

The CAD is made in Fusion360 and is parametric. We have exported configuration for all standard Voron sizes and Dueling Zero. Many aspects can be customized, including LED strip width, length and grate count.

| ![voron-led-bar-1.png](/voron-led-bar-1.png =50%x50%) | ![whatsapp_image_2026-01-06_at_12.47.25_am.jpeg](/whatsapp_image_2026-01-06_at_12.47.25_am.jpeg =50%x50%) | 
| -- |


# Voron 0 Raspberry Pi Camera Mount (upside down)

[![Static Badge](https://img.shields.io/badge/printables-click-orange?style=for-the-badge&logo=printables&logoColor=white&logoSize=auto)](https://www.printables.com/model/1416745-voron-0-raspberry-pi-camera-mount-upside-down)

The mount allows the installation of the offical raspberry Pi camera both in the normal position and upside-down. This flexibility aids with the wiring of the CSI ribbon cable.

| ![pi_camera_mount_v3.png](/pi_camera_mount_v3.png) |
| -- |

# BTT HDMI5 V1.2 display mount Voron (Clicky-Clack, more space for USB)

[![Static Badge](https://img.shields.io/badge/printables-click-orange?style=for-the-badge&logo=printables&logoColor=white&logoSize=auto)](https://www.printables.com/model/1484202-btt-hdmi5-v12-display-mount-voron-clicky-clack-mor)

This mod modified a Voron 2.4 mount for BTT HDMI5 1.2 to allow more space for the HDMI and USB connections.
The mount is extended forwards by a whole extrusion width to allow for future compatibility with the Clicky-Clack door mod. 

| ![screenshot_20251117_030710.png](/screenshot_20251117_030710.png) |
| -- |

# DragonBurner Cartographer/Beacon mount

[![Static Badge](https://img.shields.io/badge/printables-click-orange?style=for-the-badge&logo=printables&logoColor=white&logoSize=auto)](https://www.printables.com/model/1479312-dragonburner-cartographerbeacon-mount-thicker/collections)

Mounting a cartographer to a DragonBurner toolhead is often an issue because the standard mount has a tendancy to slip or break during printing.

We have taken a combined mount from Printables and enhanced its rigidity by adding the top section. The top-right ear has a tendancy to break on its own in the original model. 

Our modified mount impedes the airflow a bit (there is less space) but we have not seen any creep signs yet.

This mod is a bit of a dead end for development because we are in the process of transitioning our Voron 2.4's away from DragonBurner. We found that the DragonBurner carriage for Voron 2.4 is fragile. XoL toolhead and carriage are the way forward for our printers.

| ![screenshot_20251112_235510.png](/screenshot_20251112_235510.png) |
| -- |

# Voron 2.4 157mm double spool holder (for ERCF MMU)

[![Static Badge](https://img.shields.io/badge/printables-click-orange?style=for-the-badge&logo=printables&logoColor=white&logoSize=auto)](https://www.printables.com/model/1496217-voron-157mm-double-spool-holder-for-ercf-mmu)

For our ERCF-equipped printer, we need to mount 8 spools on the side of the printer, just under the MMU unit. For this, we need a spool holder that is able to hold 2 full spools without breaking. 

We have remixed the excellent sturdy 130mm holder from Printables by cutting inside the slicer to extend with one loop.

Mount using 2x 16mm M5 BHCS and appropiate M5 channel nuts.

| ![screenshot_20251128_015935.png](/screenshot_20251128_015935.png) |
| -- |