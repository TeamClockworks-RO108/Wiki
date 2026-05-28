---
title: BOB linear stepper system
description: A linear closed loop stepper system used as XY motion system on a 3D printer
published: true
date: 2026-05-28T12:01:04.099Z
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

The rotor is composed out of three electromagnet modules, stacked in series, making for a three-phase stepper motor system. Each Module is offset by one third of teeth pitch distance from one another. Alternatively activating the modules (one at a time) creats motion.

![screenshot_2026-05-28_144836.png](/screenshot_2026-05-28_144836.png)|
|Diagram 1 - three-phase linear closed loop stepper rotor and platen (stator). Diagram taken from [Loránd SZABÓ](https://www.researchgate.net/publication/272481795_Researches_in_the_field_of_variable_reluctance_electrical_machines_in_Technical_University_of_Cluj)|
|--|
