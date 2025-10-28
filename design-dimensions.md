---
title: Design Dimensions
description: 
published: true
date: 2025-10-28T16:13:06.526Z
tags: util
editor: markdown
dateCreated: 2024-11-13T00:40:19.306Z
---

# Design Dimensions
| Size | Socket Head | DIN 912 | ISO 4762 | Button Head | DIN 7380 | ISO 7380 | Flat Head | DIN 7991 | ISO 10642 |
| | ![screenshot_20251028_174458.png](/screenshot_20251028_174458.png) ||| ![screenshot_20251028_174518.png](/screenshot_20251028_174518.png) ||| ![screenshot_20251028_174506.png](/screenshot_20251028_174506.png)  |||
|  | Diameter (D) | Head diameter (dk) | Head height (k) | Diameter (D) | Head diameter (dk) | Head height (k) | Diameter (D) | Head diameter (dk) | Head height (k) |  
| -- |
| **M2** | 2 | 3.8 | 2 | 2 | ? | ? | 2 | 4 | 1.2 |
| **M2.5** | | ? | ? |  
| **M3** | 3 | 5.5 | 3 | 3 | 5.7 | 1.7 | 3 | 6 | 1.7 |
| **M4** | 4 | 7 | 4 | 4 | 7.6 | 2.2 | 4 | 8 | 2.3 |
| **M5** | 5 | 8.5 | 5 | 5 |10.5 | 3.3 | 5 | 10 | 2.8 |
| **M6** | 6 | 10 | 6 | 6 | 10.5 | 3.3 | 6 | 12 | 3.3 |
| **M8** | 8 | 13 | 8 | 8 | 14 | 4.4 | 8 | 16 | 4.4 |
| Comments | Standard-issue hex key screw. ||| Flatter head ||| Countersunk head that can be completely hidden inside the part. Length is measured for the whole screw! |||

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

