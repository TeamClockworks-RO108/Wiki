---
title: Design Dimensions
description: 
published: true
date: 2025-10-28T14:24:30.932Z
tags: util
editor: markdown
dateCreated: 2024-11-13T00:40:19.306Z
---

# Design Dimensions

## Socket Head - SHCS - DIN912 / ISO4762

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

## Button Head - BHCS - ISO7380

Button head screws are mostly found on Voron Zero and Dueling printers.
Length is measured from head bottom to screw end.

![iso7380-reference.png](/iso7380-reference.png)

| Type | Diameter (d) | Head diameter (dk) | Head height (k) | Hex Key (s) |
| --   | -- | -- | - |  - |
| __M2__   | 2 | ? | ? |  ? |
| __M3__   | 3 | 5.7 | 1.7 |  2 |
| __M4__   | 4 | 7.6 | 2.2 | 2.5 |
| __M5__   | 5 | 9.5 | 2.8 | 3 |
| __M6__   | 6 | 10.5 | 3.3 | 4 |
| __M8__   | 8 | 14 | 4.4 | 5 |

## Flat Head - FHCS - DIN7991 

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

# Fusion fastener tool

Fusion 360 has an integrated tool to insert fasteners of any kind. Use the `Insert fastener` tool (from the **Solid** toolbar, **Insert** category) and select what kind of fastener you need. We recommend to search by DIN codes. 

Then, configure the type of screw or nut (size, length, material) and select the holes to be filled. 

The fasteners are inserted as special components under the top-level **Fasteners** directory. They will be automatically rigid jointed to the selected features. 

| ![screenshot_20251028_044242.png](/screenshot_20251028_044242.png) | ![screenshot_20251028_044632.png](/screenshot_20251028_044632.png) |
| -- | -- |



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


# Screw Acquisition

Go to [tme.eu](https://tme.eu) and login with the team account. Navigate to **Elemente Mecanice** -> **Suruburi cu piulita** and select the correct type in filters **Norma DIN** or **Norma ISO**. Check **Valabile in stoc**. **KRAFTBERG** is the prefferred producer.

A2 stainless steel screws are good. Do not splurge on A4.  

# Flexible materials:

[Shore A 18-20](https://mathaus.ro/p/silicon-sanitar-bison-transparent-280-ml/000000000011105095)

[Shore A 10](https://mathaus.ro/p/silicon-acril-bison-alb-300-ml/000000000011105107)

