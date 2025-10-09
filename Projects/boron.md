---
title: Boron
description: 
published: true
date: 2025-10-09T19:07:02.237Z
tags: 
editor: markdown
dateCreated: 2025-10-07T00:54:49.380Z
---

# Description

Boron (Box-Voron) is an open-source light cube that can be built for relatively cheap. The sides graphics are interchangeable and allow for quick reconfiguration.

# Structure

The structure is constructed similarly to a Voron frame. There are 4 vertical beams measuring 500mm and 8 horizontal beams measuring 470mm.

The 8 smaller beams are ordered from [Makerbeam](makerbeam.com) as longer 500mm exrusions and you should add to the cart 8 cuts and specify to cut them to 470mm.

All of the extrusions should be of type MakerbeamXL.


The cube will have feet to hold it at least 20mm off the ground to allow for cables to go underneath. We must look for an option to attach a standard PC socket connector to allow cable choice flexibility. 


The center will have a continous, square coil of LED strip. We should choose standard 9mm strip and design with clearance in mind (at lease 11mm of space).

The PSU will be MeanWell, from the UHP range, but for budgeting purposes we can design to attach a cheaper LRS option. 

To prevent overheating of the wires, everyting will work at 24v. Electronics will be controlled using a Shelly Plus RGBW PM (ABSOLUTE MAX 10A, 4A per ch, 4ch)

# Parts List

| Part | P/N | Price | Notes | 
| -- | -- | -- | -- |
| Shelly controller | Shelly Plus RGBW PM | | |
| Wall socket | Gewiss GW 62 393 | | |
| Potentiometru 10k | Tayieei LA42DWG-22 | | for 22mm bore |
| 10m white neutral strip | | | At most 10A/240W |

The strip has 10m and must be divided on 5 equal sides, so each side must use up to 2m
