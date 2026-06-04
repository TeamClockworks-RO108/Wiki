---
title: BOB linear stepper system
description: A linear closed loop stepper system used as XY motion system on a 3D printer
published: true
date: 2026-06-04T01:08:29.526Z
tags: 
editor: markdown
dateCreated: 2026-05-28T11:35:58.532Z
---

> Documentation is not complete and needs to go through revision after testing
{.is-warning}

# Description

BOB (binary opearated bridge) stepper system is an augmentation brought to the [Therion](https://wiki.teamclockworks.ro/en/Projects/therion) metal plating project. It consists of a hybrid linear stepper system consisting of a directly magnetically actuated motion system, converting electric energy directly into linear motion. Thus, rotary to linear motion conversion is unnecessary, such as belt systems or screw shafts.

## Advantages

- Speeds of up to 2 m/s are possible
- Power efficiency
- Vacuum compatibility
- Friction is reduced
- Lubricating the system is optional, but not essential

# Technical description 
The stepper system looks similiar to a default, rotary stepper system, rolled on one linear axis. Both the hybrid approach and the rotary stepper system are variable reluctance devices, meaning they modify the magnetic path resitance ([reluctance](https://en.wikipedia.org/wiki/Magnetic_reluctance)) through which field lines pass in order to steer them. 

A "platen" (representing the stator) of electric steel contains small, sub-milimeter pitch teeth which have the purpose of providing a small reluctance path for magnetic field lines to cling to. 

The rotor is composed out of three electromagnet modules, stacked in series, making for a three-phase stepper motor system. Each Module is offset by one third of teeth pitch distance from one another. Alternatively activating the modules (one at a time) creats motion (diagram 1).

![screenshot_2026-05-28_144836.png](/Projects/screenshot_2026-05-28_144836.png)|
|Diagram 1 - three-phase linear closed loop stepper rotor and platen (stator). Diagram taken from [Loránd SZABÓ](https://www.researchgate.net/publication/272481795_Researches_in_the_field_of_variable_reluctance_electrical_machines_in_Technical_University_of_Cluj)|
|--|

Individual modules are made from permanent magnet/solenoid pairing, the strong permanent magnet providing a permanent magnetic bias which helps with energy efficiency and field lines distribution inside the steel core block.

The command coil is wound around a steel piece which bridges the two core (silicone steel laminated cores, for both the platen and rotor, which increases efficiency and heat dissipation) halves, and thus the two magnet poles, providing a small reluctance path for force lines to pass thorugh and reach each pole. By activating the command coil, the permanent magnet is mirrored (at a lower field intensity), thus the resulting solenoid field lines opposing the ones created by the permanent magnet (Diagram 2).

|![screenshot_2026-05-28_151158.png](/Projects/screenshot_2026-05-28_151158.png)|
|Diagram 2 - field lines passing through the module steel core a-solenoid is not active; b-solenoid is energised ([Loránd SZABÓ - RESEARCHES IN THE FIELD OF VARIABLE RELUCTANCE ELECTRICAL MACHINES IN TECHNICAL UNIVERSITY OF CLUJ](https://www.researchgate.net/publication/272481795_Researches_in_the_field_of_variable_reluctance_electrical_machines_in_Technical_University_of_Cluj)|
|--|
Thus, the low reluctance path becomes a high reluctance one, field lines being obliged to pass and joing through the steel platen, reaching for the closest teeth pair available to that module. As magnetic field force is inversely proportional to distance squared, small micron gap spacing between rotor teeth and stator teeth means higher field density passing through the platen teeth, and higher overall torque. Field lines will flow through the steel core, and continue through the platen in order close their path and connect the two poles, basically making for a high density, high strength, closed magnetic field toroid.

Linear stepper closed-loop modules are not widely spread, most of them being advertised as vacuum grade thanks to their lower heat dissipation, and lower particulate contamination caused by mechanical wear. Ceramic bearings can be used instead of steel ones in order to mount the rotor to the platen rail, which are also vacuum grade, have low wear, don't require lubing and contamination is kept at a minimum. 

## Timeline

A prototype will be built using a custom 3D printed rotor housing, in which black iron oxide (magnetite) will be placed, acting as a high permeability core for the permanent magnet and solenoid pair, as well as a higher efficiency alternative to solid cores. Custom CNC machined steel panels will be screwed on the ends of the rotor housing (as well as the magnet mounts) for increased permeability and field continuity. Variable height hand cut steel panels bolted together can also be used as alternatives for the ends of the rotor, making for a cheaper option to be used on the prototype. 

Steel bearings will be used to mount the rotor to the rail. A CNC machined platen, or hand cut variable height steel strips bolted together will also be used as the stator (platen), possibly welded on a thicker base steel strip, used for increased pemeability and lower magnetic resistance. Higher pitch teeth will be used on the prototype. Steel strips fixed on a 3D printed platen with an underlying thick base steel strip is also considered as an alternative. Tolerance between the rotor and stator will initially be set to 0, following lubing and grinding to eliminate mechanical friction between the two components, so that the air gap between the platen and rotor is kept low. 

After the first set of testing and prototyping is done, A full XY motion system will be tested. Cores made out of stacked and isolated electric steel and high iron steel sheets will be used instead, both on the stator and rotor for increased efficiency (lower [Foucault currents](https://www.voltech.com/resources/technical-articles/transformer-basics/)).

Later, the XY system will be integrated inside the Therion project, and possibly other future Voron printers.
