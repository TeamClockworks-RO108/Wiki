---
title: Design Dimensions
description: 
published: true
date: 2025-10-28T20:30:17.536Z
tags: util
editor: markdown
dateCreated: 2024-11-13T00:40:19.306Z
---

# Design Dimensions
| Size | Socket Head | DIN 912 | ISO 4762 | Button Head | DIN 7380 | ISO 7380 | Flat Head | DIN 7991 | ISO 10642 |
| | ![screenshot_20251028_174458.png](/screenshot_20251028_174458.png) ||| ![screenshot_20251028_174518.png](/screenshot_20251028_174518.png) ||| ![screenshot_20251028_174506.png](/screenshot_20251028_174506.png)  |||
|  | Diameter (D) | Head diameter (dk) | Head height (k) | Diameter (D) | Head diameter (dk) | Head height (k) | Diameter (D) | Head diameter (dk) | Head height (k) |  
| -- |
| **M2** | 2 | 3.8 | 2 | 2 |   |   | 2 | 4 | 1.2 |
| **M2.5** | 2.5 |   |   |  2.5 |  |  | 2.5 |  |  | 
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

# Fusion hole tool

The hole tool is capable of creating more complex holes. It can do countersunks, couterbores, hole tipping and many other options.

To use, create a sketch with a point (can be a circle, diameter does not matter) where we want to drill the hole. Open the hole tool and select the placement method to `On sketch (Multiple holes)` and select all your desired hole points.  Select your distance (we recommend to use the `To Object` tool).

There are multiple hole types to choose from. You can do standard, counterbores, countersunken and specify different threads and drill point types.

We do not reccomend using the built-in thread and clearance tap types because we require specific tolerances on our printers. Just create your hole as you would normally.

| ![screenshot_20251028_220615.png](/screenshot_20251028_220615.png) | ![screenshot_20251028_221255.png](/screenshot_20251028_221255.png) |
| -- | -- |

# Screw Acquisition

Go to [tme.eu](https://tme.eu) and login with the team account. Navigate to **Elemente Mecanice** -> **Suruburi cu piulita** and select the correct type in filters **Norma DIN** or **Norma ISO**. Check **Valabile in stoc**. **KRAFTBERG** is the prefferred producer.

A2 stainless steel screws are good. Do not splurge on A4.  

# Flexible materials:

[Shore A 18-20](https://mathaus.ro/p/silicon-sanitar-bison-transparent-280-ml/000000000011105095)

[Shore A 10](https://mathaus.ro/p/silicon-acril-bison-alb-300-ml/000000000011105107)

