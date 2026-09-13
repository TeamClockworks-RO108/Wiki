---
title: BOB linear stepper system
description: A linear closed loop stepper system used as XY motion system on a 3D printer
published: true
date: 2026-09-13T13:02:47.317Z
tags: 
editor: markdown
dateCreated: 2026-05-28T11:35:58.532Z
---

> Documentation is not complete and needs to go through revision after testing
{.is-warning}

# Description

BOB (binary opearated bridge) linear closed loop stepper motion system is an augmentation brought to the [Therion](https://wiki.teamclockworks.ro/en/Projects/therion) metal plating project. It consists of a hybrid linear stepper system consisting of an electromagnetically actuated motion system, converting electric energy directly into linear motion. Thus, rotary to linear motion conversion is unnecessary, such as belt systems or screw shafts.

## Project ethos

The BOB linear stepper project was created to aid the aforementioned Therion project, an experimental additive manufacturing printer, implementing experimental motion systems (amongst others) with the purpose of improving quality, performance and user experience as well as cost, based on each printers requirements, a core value best represented by the belief that a system should best fit its purpose and user-not its designer and industrial "get a  quote" limitation.

Thus, this project aims to offer an open source close alternative to industry standard linear stepper systems, offering continuous updates which aim to improve performance and reduce cost.

## Advantages

- High speed motion system
- Higher overall power efficiency compared to classic motion systems
- Vacuum compatibility
- Friction is reduced
- Lubricating the system is optional, but not essential (based on the project design)
- higher achievable precision (for CNC systems, 3D printers or high precision machines)

# Technical description 
The linear stepper acts as a 3-phase synchronous motor, rolled over a flat, straight magnet "teeth" rail, using command pulses to precisely control positional precision of a 3 electromagnet carriage, which implements a form of magnetic (and potentially optical) incremental encoder control system, composed of one linear magnetic/optical strip, and one readout head mounted on the carriage.
## Timeline

A prototype will be built using a custom 3D printed rotor housing, in which black iron oxide (magnetite) will be placed, acting as a high permeability core for the permanent magnet and solenoid pair, as well as a higher efficiency alternative to solid cores. Custom CNC machined steel panels will be screwed on the ends of the rotor housing (as well as the magnet mounts) for increased permeability and field continuity. Variable height hand cut steel panels bolted together can also be used as alternatives for the ends of the rotor, making for a cheaper option to be used on the prototype. 

Steel bearings will be used to mount the rotor to the rail. A CNC machined platen, or hand cut variable height steel strips bolted together will also be used as the stator (platen), possibly welded on a thicker base steel strip, used for increased pemeability and lower magnetic resistance. Higher pitch teeth will be used on the prototype. Steel strips fixed on a 3D printed platen with an underlying thick base steel strip is also considered as an alternative. Tolerance between the rotor and stator will initially be set to 0, following lubing and grinding to eliminate mechanical friction between the two components, so that the air gap between the platen and rotor is kept low. 

After the first set of testing and prototyping is done, A full XY motion system will be tested. Cores made out of stacked and isolated electric steel and high iron steel sheets will be used instead, both on the stator and rotor for increased efficiency (lower [Foucault currents](https://www.voltech.com/resources/technical-articles/transformer-basics/)).

Later, the XY system will be integrated inside the Therion project, and possibly other future Voron printers.
