---
title: Design Dimensions
description: 
published: true
date: 2025-11-17T03:22:04.375Z
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

## Choosing a fastener

For the most part, SHCS should be used for most designs that do not call for speciality fasteners. 

For FTC, M4 screws are almost all SHCS, because BHCS(button head) are much easier to strip with their smaller hex key head.

In M3 land, BHCS are sometimes preferred over SHCS because the head diameter is a bit larger and this leads to better pressure distribution on the material. This is only applicable in 3D printed parts, where SHCS can get loose over time due to plastic creep. 

FHCS screws can be used to hide the screw in the surface of the part. Take care to design the screw length **with** the head included. 

For M2 and smaller, prefer to always use SHCS. The other screw styles hav very small hex heads and will strip easily. 

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

# Fastener Availability

| Type |||| Count | Notes |
| -- |
| M2 |  | | | |  To be counted |
| ||||||
| M2.5 | SHCS |A2| 16mm | 100 | |
| M2.5 | SHCS |A2| 20mm | 100 | |
| ||||||
| M3 | FHCS |A2| 4mm | 300 | |
| M3 | FHCS |A2| 5mm | 200 | |
| M3 | FHCS |A2| 6mm | 300 | |
| M3 | FHCS |A2| 8mm | 300 | |
| M3 | FHCS |A2| 10mm | 300 | |
| M3 | FHCS |A2| 12mm | 200 | |
| M3 | FHCS |A2| 16mm | 100 | |
| M3 | FHCS |A2| 20mm | 100 | |
| ||||||
| M3 | SHCS |A2| 6mm | To be counted | |
| M3 | SHCS |A2| 8mm | 500 | |
| M3 | SHCS |A2| 10mm | 200 | |
| M3 | SHCS |A2| 12mm | 200 | |
| M3 | SHCS |A2| 14mm | 100 | |
| M3 | SHCS |A2| 16mm | 200 | |
| M3 | SHCS |A2| 20mm | 100 | |
| M3 | SHCS |A2| 25mm | 100 | |
| M3 | SHCS |A2| 30mm | 100 | |
| M3 | SHCS |A2| 35mm | To be counted | |
| M3 | SHCS |A2| 40mm | To be counted | |
| M3 | SHCS |A2| 50mm | To be counted | |
| ||||||
| M3 | BHCS |A2| 8mm | 400 | |
| M3 | BHCS |A2| 10mm | 200 | |
| M3 | BHCS |A2| 12mm | 200 | |
| M3 | BHCS |Steel| 16mm | 200 | |
| M3 | BHCS |A2| 20mm | 200 | |
| M3 | BHCS |Steel| 25mm | 200 | |
| M3 | BHCS |A2| 30mm | 200 | |
| M3 | BHCS |A2| 35mm | To be counted | |
| M3 | BHCS |A2| 40mm | To be counted | |
| ||||||
| M3 | Hex Nut ||| To be counted, 500 in makerbeam order | |
| M3 | Lock Nut ||| To be counted | |
| M3 | MakerbeamXL Nut ||| 400 | |
| M3 | Heat inerts ||| 200 | |
| M3 | 2020 Post-install nut ||| To be counted | |
| ||||||
| M4 | SHCS |A2| 6mm | 200 | |
| M4 | SHCS |A2| 8mm | 400 | |
| M4 | SHCS |A2| 10mm | 200 | |
| M4 | SHCS |A2| 12mm | 200 | |
| M4 | SHCS |A2| 16mm | 400 | |
| M4 | SHCS |A2| 20mm | 200 | |
| M4 | SHCS |A2| 25mm | 200 | |
| M4 | SHCS |A2| 30mm | 100 | |
| M4 | SHCS |A2| 35mm | 100 | |
| M4 | SHCS |A2| 40mm | 100 | |
| ||||||
| M4 | Hex Nut ||| To be counted | |
| M4 | Lock Nut ||| To be counted | |
| ||||||
| M5 | 2020 Post-install nut ||| To be counted | |
| ||||||
| M3 | Grub |A2| 5mm | 10 | |
| M4 | Grub |A2| 4mm | 800 | Check count, sounds unreasonable |
| M5 | Grub |A2| 4mm | 100 | |






# Screw Acquisition

Go to [tme.eu](https://tme.eu) and login with the team account. Navigate to **Elemente Mecanice** -> **Suruburi cu piulita** and select the correct type in filters **Norma DIN** or **Norma ISO**. Check **Valabile in stoc**. **KRAFTBERG** is the prefferred producer.

A2 stainless steel screws are good. Do not splurge on A4.  

# Flexible materials:

[Shore A 18-20](https://mathaus.ro/p/silicon-sanitar-bison-transparent-280-ml/000000000011105095)

[Shore A 10](https://mathaus.ro/p/silicon-acril-bison-alb-300-ml/000000000011105107)

