---
title: Design Dimensions
description: 
published: true
date: 2025-05-21T23:38:34.646Z
tags: util
editor: markdown
dateCreated: 2024-11-13T00:40:19.306Z
---

# Design Dimensions

## SHCS - DIN912 ISO4672

This is the most common screw type we use.

![din912-reference.png](/din912-reference.png)

Screw diameter and head diameter are always equal.
Length is measured from head bottom to screw end. 

| Type | Diameter (d1) | Head diameter (d2) | Head height (k) | Hex Key (s) |
| --   | -- | -- | - |  - |
| __M2__   | 2 | 3.8 | 2 |  1.5 |
| __M3__   | 3 | 5.5 | 3 |  2.5 |
| __M4__   | 4 | 7 | 4 | 3 |
| __M5__   | 5 | 8.5 | 5 | 4 |
| __M6__   | 6 | 10 | 6 | 5 |
| __M8__   | 8 | 13 | 8 | 6 |

## FHCS - DIN7991 ISO10642

We use this screw when we want to hide the head inside the part and the part is not think enough to dig the whole SHCS head in and still maintain resistance. They have a very shallow head but it is much wider that SHCS.

![din7991-reference.png](/din7991-reference.png)

Head angle (a) is always 90 degrees.
Length is measured for the whole screw, head included.

| Type | Diameter (d1) | Head diameter (d2) | Head height (k) | Hex Key (s) |
| --   | -- | -- | - |  - |
| __M2__   | 2 | 4 | 1.2 |  1.3 |
| __M3__   | 3 | 6 | 1.7 |  2 |
| __M4__   | 4 | 8 | 2.3 | 2.5 |
| __M5__   | 5 | 10 | 2.8 | 3 |
| __M6__   | 6 | 12 | 3.3 | 4 |
| __M8__   | 8 | 16 | 4.4 | 5 |


## Printed hole screw tolerances

When printing a hole it often comes out a different (smaller) diameter than specified in the CAD software. Here is a table to help with diameters for screw holes.

Ideally we should be able to have the same values across all printers and materials and the tuning must be done on a per-material/printer basis in the slicer's hole compensation algorithm.
Until then, we shall keep separate tables. 

### Prusa MK3S+

| Material | Type        | M2 | M3 | M4 | M5 | M6 | M8 |
| --       |          -- | -- | -- | -- | -- | -- | -- |
| ABS      | Pass-trough |
| ^^       | Threaded    | 
| ASA      | Pass-trough |
| ^^       | Threaded    | 
| Prusa PC | Pass-trough |
| ^^       | Threaded    | 
| PETG     | Pass-trough |
| ^^       | Threaded    | 
| PLA      | Pass-trough |
| ^^       | Threaded    | 

### Voron (Dragon HF)

| Material | Type        | M2 | M3 | M4 | M5 | M6 | M8 |
| --       |          -- | -- | -- | -- | -- | -- | -- |
| ABS      | Pass-trough |
| ^^       | Threaded    | 
| ASA      | Pass-trough |
| ^^       | Threaded    | 
| Prusa PC | Pass-trough |
| ^^       | Threaded    | 
| PETG     | Pass-trough |
| ^^       | Threaded    | 
| PLA      | Pass-trough | Not able to print |||||||
| ^^       | Threaded    | ^^                |||||||


# Flexible materials:

[Shore A 18-20](https://mathaus.ro/p/silicon-sanitar-bison-transparent-280-ml/000000000011105095)

[Shore A 10](https://mathaus.ro/p/silicon-acril-bison-alb-300-ml/000000000011105107)

