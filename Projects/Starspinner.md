---
title: Planetary Starspinner
description: 
published: true
date: 2025-10-12T13:44:35.955Z
tags: 
editor: markdown
dateCreated: 2025-10-12T12:35:21.952Z
---

# Description
Planetary Starspinner is a project that allows to modify the 84 RPM goBILDA Yellow Jacket Planetary motor to create either 4200 RPM or 8000 RPM. The entire conversion happens inside the planetary housing, allowing you to mount the motor as you would with a standard goBILDA motor.

Starspinner works by inserting a part that connects the planets of two stages together. This way, all the subsequent stages of the planetary reducer are reversed (instead of reducing, they amplify speed). This project includes a bit of parts machining, so it's best to read it twice before starting to build.

From our prototyping and testing we found that 2700-3500 RPM is the ideal speed for launching elements, so we set out to find an elegant way to obtain this speed while maintaining maximum torque (and speedup time). After designing, we found that the same motor can be assembled a bit differently to yield 8000 RPM (and also 31200 RPM and 22200 RPM at extremely low torques). We think 8000 RPM would be suitable for launchers with small diameter flywheels.

# Parts list

For this project, you will need two fabricate two different parts: `SPx` and `SPc`

 * The `SPx` part has a single variant and it is called `SPx1117`.

 * The `SPc` part has a few variants that will be described below.



# SPx1117

`SPx1117` is the connector that reverses the planetary ratio. Its ending comes from it connecting 17-teeth center planetary stage to 11-teeth center planetary stage.

| ![screenshot_20251012_162845.png](/screenshot_20251012_162845.png) | ![whatsapp_image_2025-10-12_at_4.34.04_pm.jpeg](/whatsapp_image_2025-10-12_at_4.34.04_pm.jpeg) |
| --- | --- |

We strongly advise to machine this part out of aluminium or better. The dimensions are modelled after goBILDA carriers, so the gears should fit nicely on the prongs.

Extra care should be taken to machine this part with precise tolerances. The prongs diameters are exactly 4mm and the holes of goBILDA gears are slightly bit larger.

If you decide to mill this part on a CNC mill, take into condiferation the capabilities of the machine. It is very important the the diameter of the prongs do not exceed 4mm. It might be beneficial to resize the prongs in the CAD to about 3.95mm.

We got this part fabricated by making all the segments (6 pins and the base) on a precision lathe and then asembling by press-fitting. You can see the additional chamfers in the photo above that aided in press assembly. 


# SPc

`SPc` parts connect the output prongs of two different planetary motors together in a 1:1 ratio. They server to connect the output shaft of the motor to the reversed amplification stages created by `SPx1117`.
The number of teeth in the naming scheme represent the count of the associated **center** gear that would fit in between the planetary stage.

The `SPc` parts should be fabricated by 3D printing. Extra care should be taken to ensure that the prongs fit tight within the holes.  To ensure tolarance, use the horizontal expansion (often also called XY compensation) setting in your slicer to adjust the fit. 

| Part number | Image | Description | 
| --- | --- | --- |
| `SPc1111` | ![spc1111.png](/spc1111.png) | Connect 11-teeth prongs to 11-teeth prongs | 
| `SPc1117` | ![spc1117.png](/spc1117.png) | Connect 11-teeth prongs to 17-teeth prongs | 
| `SPc1717` | ![spc1717.png](/spc1717.png) | Connect 17-teeth prongs to 17-teeth prongs | 


# Assembling 4200 RPM






