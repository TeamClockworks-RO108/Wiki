---
title: MiloEx CNC
description: 
published: true
date: 2026-03-16T03:10:31.543Z
tags: 
editor: markdown
dateCreated: 2026-03-16T02:47:38.339Z
---

# Movement system

Movment controller will be PlanetCNC MK3/9.

## Classic stepper solution
 * DO-57STH56-2804AC
 * DM556 drivers
 * 48 V PSU
 
# Integrated servo
 * ClearPath-SDSK-23
 * 75V, 1500W PSU (RSP-1500-72)
 * 24V, 100W auxiliary PSU
 * Separate PSU for other electronics
 
TODO: Validate required torque
 


# Milling

For cutting CFRP, AI reccommends:
```
Spindle: 18,000 RPM
Tool: 3 mm composite-specific cutter, ideally diamond-cut / burr / compression / straight-flute composite geometry, not a normal aluminum end mill
Axial DOC: 0.3–0.8 mm per pass
Radial WOC for pocketing: 10–25% of tool diameter = about 0.3–0.75 mm
Feed: start around 600–1200 mm/min, then tune by edge quality and spindle load


Diamond-pattern / burr / composite cutters are meant for abrasive composites and can plunge, which helps for pockets. One Amana composite cutter page explicitly says these tools are for highly abrasive materials including carbon-fiber-based composites and lists a maximum RPM of 28,000.

Downcut / compression / straight-flute composite tools are useful when you care a lot about top/bottom edge quality and delamination control. Harvey’s tooling guidance notes that straight-flute and compression geometries are used to reduce delamination and fiber pullout in layered composites.

So my practical recommendation is:

Rough pocketing: diamond-cut 3 mm, about 18k RPM, 0.5 mm DOC, 0.5 mm stepover, 800–1000 mm/min

Finish pass: same RPM, 0.1–0.2 mm radial stock left, then a light finish pass at 600–800 mm/min

If the edges fuzz, delaminate, or get hot:

reduce RPM a bit toward 16k

increase feed slightly so it cuts instead of rubs

reduce depth/stepover

use a sharper composite cutter

If everything is clean and spindle load is low:

move upward toward 20k–22k RPM

then increase feed gradually
```