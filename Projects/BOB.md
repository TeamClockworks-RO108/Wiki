---
title: BOB linear stepper system
description: A linear closed loop stepper system used as XY motion system on a 3D printer
published: true
date: 2026-09-13T14:41:09.745Z
tags: 
editor: markdown
dateCreated: 2026-05-28T11:35:58.532Z
---

> Documentation is not complete and needs to go through revision after testing
{.is-warning}

# Description

BOB (binary operated bridge) linear closed loop stepper motion system is an augmentation brought to the [Therion](https://wiki.teamclockworks.ro/en/Projects/therion) metal plating project. It consists of a hybrid linear stepper system consisting of an electromagnetically actuated motion system, converting electric energy directly into linear motion. Thus, rotary to linear motion conversion is unnecessary, such as belt systems or screw shafts.

## Project ethos

The BOB linear stepper project was created to aid the aforementioned Therion project, an experimental additive manufacturing printer, implementing experimental motion systems (amongst others) with the purpose of improving quality, performance and user experience as well as cost, based on each printers requirements, a core value best represented by the belief that a system should best fit its purpose and user - not its designer and industrial "get a  quote" limitations.

Thus, this project aims to offer an open source close alternative to industry standard linear stepper systems, offering continuous updates which aim to improve performance and reduce cost. The project can also aid other open source projects (such as [Voron](https://vorondesign.com/)) in building experimental printers (and new "proto" [printers](https://docs.cartographer3d.com/linear-motor/coming-soon)).

> 100% made by humans
{.is-info}


## Advantages

- High speed motion system
- Higher overall power efficiency compared to classic motion systems
- Vacuum compatibility
- Friction is reduced
- Lubricating the system is optional, but not essential (based on the project design)
- higher achievable precision (for CNC systems, 3D printers or high precision machines)
- significant reduction of VFAs (Vertical Fine Artifacts) in 3D prints, caused by finite belt tooth pitch

# Technical description 
The linear closed-loop stepper acts as a 3-phase synchronous motor, rolled over a flat, straight magnet "tooth" rail, using command pulses to precisely control positional precision of a 3 electromagnet carriage, which implements a form of magnetic (and potentially optical) incremental encoder control system, composed of one linear magnetic/optical strip, and one readout head mounted on the carriage.

Compared to a classic stepper motion system, linear steppers have tooth pitches ranging from couple mm to over 10mm. a tradeoff between cost, magnet type, total magnet holding force as well as aspect rati and area/volume have to all be considered when selecting the type of magnet tooth used. Neodymium magnets have high holding force compared to their volume and mass, as well as  high commercial availability (even strong N52 types). On the other hand, they are mechanically brittle, can be expensive and they lose their holding force rapidly, experiencing maximum force at around 0C (273,15K), and dropping at a minimum around 80C (353,15K). Heat resistant types exist, but are harder to find. We found the best option for our application to be an N52 Neodymium magnet, with 10x20mm surface and 2-5mm thickness. They have a holding force ranging from 2-to 5kg per magnet.

Following the inverse cube law applied to magnetic fields (B ∝ 1/d^3 ; where d - distance and B - magnetic field), we conclude that the distance between the carriage electromagnets and the platen has to be kept at a minimum (within about 1mm or less) so that torque is maintained high enough. Carriage structural rigidity needs to be maintained in order to prevent buckling caused by the attraction between the electromagnets and the permanent magnets as well as stalling (friction between the electromagnet core and the platen).

Each electromagnet tooth pitchb is approximately equal to its twin platen magnet teeth. A slight offset is applied for the spacing of the electromagnet teeth, assuring that one magnet is always perfectly aligned to one platen magnet (corresponding to one full step), while the other two teeth are both either left hand biased (closer to the platen tooth to its left) or right hand biased (closer to the platen tooth to its right). Thus, by alternating the control signal in each electromagnet, motion is achieved. Each signal is offset by about 120 electrical degrees from eachother, making for high efficiency. Field oriented control (FOC) will be used to ensure proper control of the positional accuracy, as well as speed and torque of the stepper at all times.

![linearmotorprinzip.png](/linearmotorprinzip.png)

Two types of encoder types will be tested, both optical and magnetic, and compared in different conditions and levels of dust, use, speeds, light, precision etc. Thus, quality will be compared against total cost and the best system will be selected and integrated. The two chips will be [AS5304B TSSOP20 LF T&RDP](https://www.digikey.at/en/products/detail/ams-osram-usa-inc/AS5304B-TSSOP20-LF-T-RDP/18769154) (magnetic) and a variant of the [AEDR-8300-1W2](https://ro.farnell.com/broadcom/aedr-8300-1w2/photointerrupter-reflective/dp/1735258) (optical). Different strips will also be tested.

For the prototype, self-lubricating [IGLIDUR polymer linear bushing](https://www.igus.eu/plain-bearing) inserts will be used, thanks to their low maintanance requirements, high chemical resistance, optimal lubrication in all kinds of environments as well as cost and availability. These inserts will also be tested for future use in different systems and projects. In the future, custom teflon linear bearings compatible with the 2020/3030/4040 V-slot aluminum extrusions  might be implemented for use in 3D printers and other systems.



## Timeline

A prototype will be built using a custom 3D printed rotor housing, in which black iron oxide (magnetite) will be placed, acting as a high permeability core for the permanent magnet and solenoid pair, as well as a higher efficiency alternative to solid cores. Custom CNC machined steel panels will be screwed on the ends of the rotor housing (as well as the magnet mounts) for increased permeability and field continuity. Variable height hand cut steel panels bolted together can also be used as alternatives for the ends of the rotor, making for a cheaper option to be used on the prototype. 

Steel bearings will be used to mount the rotor to the rail. A CNC machined platen, or hand cut variable height steel strips bolted together will also be used as the stator (platen), possibly welded on a thicker base steel strip, used for increased pemeability and lower magnetic resistance. Higher pitch teeth will be used on the prototype. Steel strips fixed on a 3D printed platen with an underlying thick base steel strip is also considered as an alternative. Tolerance between the rotor and stator will initially be set to 0, following lubing and grinding to eliminate mechanical friction between the two components, so that the air gap between the platen and rotor is kept low. 

After the first set of testing and prototyping is done, A full XY motion system will be tested. Cores made out of stacked and isolated electric steel and high iron steel sheets will be used instead, both on the stator and rotor for increased efficiency (lower [Foucault currents](https://www.voltech.com/resources/technical-articles/transformer-basics/)).

Later, the XY system will be integrated inside the Therion project, and possibly other future Voron printers.
