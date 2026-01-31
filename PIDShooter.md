---
title: PID Shooter
description: 
published: true
date: 2026-01-31T02:41:52.584Z
tags: programming
editor: markdown
dateCreated: 2025-10-21T17:08:28.136Z
---

# Overview

This page provides an overview of how to tune a PID for a shooter. 

Below are a few graphs showcasing different situations that you might encounter.

The process we use for flywheels is as follows:
 * Start with all coefficients at 0
 * Raise `Kf` until the motor starts moving on its own, then back it off just below the threshold point. This parameter compensates static friction and stiction. For a relatively frictionless flywheel, this is 0.
 * Raise `Kp` until the system correctly follows the target in desired time. Oscillations are acceptable.
 * Raise `Kd` (small values) until oscillations are compensated for and the system is not too damped.
 * If the system suffers from steady-state error, Raise `Ki` until the error dissapears in a time equivalent with twice the settling time with only `Kp` and `Kd`. Keeping this value low can help avoid systematic instability.
 
The result of this procedure is often an overcompensated PID. If the system does not tolerate aggressiveness well, back off all values by about 15-30%.

Systems with higher inertia (mass) can tolerate too high `Kd` values. Low-inertia and overlapped control values can cause unwanted vibrations at high frequencies. 

The tests are done using a 4200 RPM motor attached to a AndyMark 4inch 30A compliant wheel. 

# Undercompensated Kp
![screenshot_20251021_193423.png](/screenshot_20251021_193423.png)

# Too small Ki (steady state error)
![screenshot_20251021_194026.png](/screenshot_20251021_194026.png)
![screenshot_20251021_193759.png](/screenshot_20251021_193759.png)

# Better Ki but not enough
![screenshot_20251021_193655.png](/screenshot_20251021_193655.png)

# Ki, Kd induced oscillations
![screenshot_20251021_195024.png](/screenshot_20251021_195024.png)

# Perfect
![screenshot_20251021_194141.png](/screenshot_20251021_194141.png)