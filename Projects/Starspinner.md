---
title: Planetary Starspinner
description: 
published: true
date: 2025-10-13T01:32:34.861Z
tags: 
editor: markdown
dateCreated: 2025-10-12T12:35:21.952Z
---

# Description
Planetary Starspinner is a project that allows to modify the 84 RPM goBILDA Yellow Jacket Planetary motor to create either 4200 RPM or 8000 RPM. The entire conversion happens inside the planetary housing, allowing you to mount the motor as you would with a standard goBILDA motor.

From our prototyping and testing we found that 2700-3500 RPM is the ideal speed for launching elements, so we set out to find an elegant way to obtain this speed while maintaining maximum torque (and speedup time). After analysis, we found that the planetary stages could be reversed, opening a new world of possibilities. We can produce 4200, 8000 and even unreal speeds of 22200 and 31200 (at extremely low torques)!

The CAD is licensed under [GNU General Public License Version 3](https://www.gnu.org/licenses/gpl-3.0.en.html). This means, among others, that distributing either STL, printed parts or assemblies containing Starspinner, you must also make the modified CAD available to users. 

Source (CAD) files are available on our [Github repository](https://github.com/TeamClockworks-RO108/PlanetaryStarspinner).

# Design philosophy

When we set out to work on this project, it was imperative that the entirety of modifications happen inside the factory enclosure. We wanted to prove that it is possible to obtain an intermediate ratio between 1620 and 6000 while looking identical to stock motors.

Starspinner works by inserting a custom connector that binds the planets of two stages together. 

This way, all the subsequent stages of after the connector are reversed (instead of reducing, they amplify speed). 

Even though 3D printing is our *magna carta*, we realized that sitting in the confines of the stock motor is not possible with plastic parts. Therefore, we settled on custom metal part that can be both milled and turned.

This project includes a bit of parts machining, so it's best to read it twice before starting to build.

# Parts list

For this project, you will need two fabricate two different parts: `SPx` and `SPc`

 * The `SPx` part has a single variant and it is called `SPx1117`.

 * The `SPc` part has a few variants that will be described below.



## SPx1117

`SPx1117` is the connector that reverses the planetary ratio. Its ending comes from it connecting 17-teeth center planetary stage to 11-teeth center planetary stage.

| ![screenshot_20251012_162845.png](/screenshot_20251012_162845.png) | ![whatsapp_image_2025-10-12_at_4.34.04_pm.jpeg](/whatsapp_image_2025-10-12_at_4.34.04_pm.jpeg) |
| --- | --- |

We strongly advise to machine this part out of aluminium or better. The dimensions are modelled after goBILDA carriers, so the gears should fit nicely on the prongs.

For fabrication, please refer to the CAD file and [technical drawing]( https://github.com/TeamClockworks-RO108/PlanetaryStarspinner/blob/master/CAD/SPx1117%20Drawing.pdf) in the repository. 

Extra care should be taken to machine this part with precise tolerances. The prongs diameters are exactly 4mm and the holes of goBILDA gears are slightly bit larger. Concentricity of the top and bottom side is very important for smooth operation.

If you decide to mill this part on a CNC mill, take into condiferation the capabilities of the machine. It is very important the the diameter of the prongs do not exceed 4mm. It might be beneficial to resize the prongs in the CAD to about 3.95mm.

We got this part fabricated by making all the segments (6 pins and the base) on a precision lathe and then asembling by press-fitting. You can see the additional chamfers in the photo above that aided in press assembly. 


## SPc

`SPc` parts connect the output prongs of two different planetary motors together in a 1:1 ratio. They server to connect the output shaft of the motor to the reversed amplification stages created by `SPx1117`.
The number of teeth in the naming scheme represent the count of the associated **center** gear that would fit in between the planetary stage.

The `SPc` parts should be fabricated by 3D printing. Extra care should be taken to ensure that the prongs fit tight within the holes.  To ensure tolarance, use the horizontal expansion (often also called XY compensation) setting in your slicer to adjust the fit. 

| Part number | Image | Description | 
| --- | --- | --- |
| `SPc1111` | ![spc1111.png](/spc1111.png) | Connect 11-teeth prongs to 11-teeth prongs | 
| `SPc1117` | ![spc1117.png](/spc1117.png) | Connect 11-teeth prongs to 17-teeth prongs | 
| `SPc1717` | ![spc1717.png](/spc1717.png) | Connect 17-teeth prongs to 17-teeth prongs | 

# Assembly

The gearboxes from goBILDA come factory packed with grease. After disassembly of the motors, it is recommended to clean the old grease. We have had success to clean old grease a nylon brush (toothbrush is ok) and adequate solvent like WD-40 or brake cleaner fluid.

After reassembly, it is very important to lubricate the entire gearbox with thick, tacky grease. Thin lubricating oils (or dry lubricants) are not suitable for planetary gearboxes. Lubricate both the teeth and the prongs interface of the planets. Our grease of choice is the **LiquiMoly LM47**.

> Do ***NOT*** use WD-40 as a grease replacement in any mechanism. WD-40 is meant to be used as a penerating agent in rusty mechanism and can also be used as degreasing solvent.
{.is-warning}


# Assembling 4200 RPM

To make this configuration, we will combine a 84 RPM motor with a 1150 RPM motor to produce 4200 RPM and 1620 RPM. I will use superscript on this page to mark where each part is coming from.

You will find the following components in the motors:

| `D17T`^84^ | 6x `P14T`^84^ | 3x `P17T`^84^ | `P17G11`^84^ | `P11G17`^84^ | `O17`^84^ |
| --- | --- | 
| 17T Motor D gear | 14T Planet gears (17T Sun) | 17T Planet gears (11T Sun) | 11T-Sun to 17T Carrier | 17T-Sun to 11T Carrier | 17T Output carrier |


| `D11T`^1150^ | 3x `P17T`^1150^ | `O11`^1150^ |
| --- |
| 11T Motor D gear | 17T Planet gears (11T Sun) | 11T Output carrier |

The 4200 RPM configuration is assembled as follows:



| ![staspinner-4200-annotated.png](/staspinner-4200-annotated.png) ||||||||
| Motor base | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
| ---        | - | - | - | - | - | - | - |
| Any motor | `D11T`^1150^ | 3x `P17T`^84^ | `SPx1117` | 3x `P14T`^84^ | `P11G17`^84^ | `SPc1117` | `O11`^1150^ |

You will be left with the following components:
 * `D17T`^84^
 * 3x `P14T`^84^
 * 3x `P17T`^1150^
 * `P17G11`^84^
 * `O17`^84^
 
Using the spare motor and a few of the left components (`D17T`^84^, 3x `P14T`^84^, `O17`^84^) you can easily assemble another 1620 RPM Motor from the 1150 RPM we sacrificed. 

# Assembling 8000 RPM

To make 8000 RPM, we will only need a 84 RPM motor. We achieve this by leaving the 17T Sun stage unchanged and reversing the 11T stage. The last 11T stage is completely removed.

You will find the following components in the 84 RPM motor:

| `D17T` | 6x `P14T` | 3x `P17T` | `P17G11` | `P11G17` | `O17` |
| --- | --- | 
| 17T Motor D gear | 14T Planet gears (17T Sun) | 17T Planet gears (11T Sun) | 11T-Sun to 17T Carrier | 17T-Sun to 11T Carrier | 17T Output carrier |

The 8000 RPM configuration is assembled as follows:

| ![staspinner-4200-annotated.png](/staspinner-8000-annotated.png) ||||||||
| Motor base | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
| ---        | - | - | - | - | - | - | - |
| Any motor | `D17T` | 3x `P14T` | `SPx1117` | 3x `P17T` | `P17G11` | `SPc1717` | `O17` |

You will be left with the following parts:
 * 3x `P14T`
 * `P17G11`

