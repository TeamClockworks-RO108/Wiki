---
title: Rocky
description: 
published: true
date: 2026-01-25T03:13:57.455Z
tags: 
editor: markdown
dateCreated: 2026-01-25T02:36:16.294Z
---



# ROCKY

## Stats

### Autonomous Period

* 12 artifacts + leave (36 + 3 points)
* 5 matching pattern artifacts (10 points)

### Teleoperated Period

* 30 artifacts + full (90 + 10 points)

Total: 49 + 100 = 149 points (solo)


## First Version

The first version of the robot was built during the first 16 hours of the competition, during the Kickathon, where we quickly transformed our initial ideas into functional solutions.

The robot was designed around the idea of storing up to 3 artifacts placed by a human player into a tube-shaped container. We analyzed building a classic intake or an autonomous solution, but due to time constraints we chose to implement a simple 3-artifact autonomous routine.

The launcher was built using an AndyMark silicone wheel, driven by a 6000 RPM motor. Feeding artifacts into the launcher was done with the help of a servo connected to a flap, which pushed artifacts individually into the launching mechanism, ensuring simple and repeatable control suitable for a 16-hour hackathon.


| Pros                              | Cons                              |
| --------------------------------- | --------------------------------- |
| Simplicity                        | No intake                         |
| Prototype built in under 16 hours | Inconsistent launching            |
|                                   | Autonomous limited to 3 artifacts |


| ![417c3ae7d0c822abf3e22a7568a8fd2851c27d65.jpg](/417c3ae7d0c822abf3e22a7568a8fd2851c27d65.jpg) |
| -- |


## Second Version

Analyzing our Kickathon design revealed significant development potential. We decided to address the robot’s shortcomings as follows.

* Adding an intake.
  We mounted the storage tube in a pivoting position, actuated by a servo motor with a 2:1 gearbox. This allows the intake opening to approach the ground, where we added a drum-based intake using elastic bands.

* Improved launch consistency.
  We added a manual PID-based speed control algorithm and introduced a servo-actuated barrier to better control launch sequencing.

In the picture below is only the launch and storage tube, and the intake mechanism based on rubber bands. 

| ![img-20251031-wa0029.jpg](/img-20251031-wa0029.jpg) |
| -- |


### Observed Issues

After testing, we identified several weaknesses during collection. Because the intake is relatively narrow (130 mm) and the tube is fairly short (400 mm), collecting the last artifact becomes difficult and sometimes it falls back out.

* Reduced intake error margin.
  Intake collection tube is too narrow (130mm).
* Last artifact may fall out due to lack of grip on tube.
* Unstable during aggressive gameplay .
  Collisions with other robots may cause the last artifact to fall. 

## Third Version

The third iteration of Rocky has some large improvements that allow it to be a much more robust robot. As a consequence, our OPR raised significantly when version 3 was put into play at league meets.

* Wide intake (310 mm) with gears and dual roller
  We widened the intake area to 310 mm and added a secondary, smaller elastic roller behind the main one to assist artifact transfer during fast autonomous collection. Two servo-driven gears were added on the sides to prevent the last artifact from falling out.

* Braking system
  We added two large lateral braking blocks actuated through the main parallelogram mechanism using high-torque servomotors. These blocks deploy lower than the traction wheels and are used during launching to prevent the robot from being pushed by other robots.
  The brakes were tested at **Future At High Speed** where namy of our opponents opted to play defense by pushing us. They were very effective, phisically pinning our robot into place. **No team was able to push us with our brakes lowered**.

* Automatic positioning using a video camera
  We implemented automatic navigation to the optimal launch zone using a Limelight camera and field markers. Navigation is based on sensor fusion between camera data and odometry.
  
 * Faster (435 RPM) motors on drivetrain. This change allows our driver to navigate much faster around the field, at the expense of slower accelerations and less control. In the past, we have emulated slower accelerations using FIR filters on the motors to allow our driver to get accustomed to slower controls to prepare for this change. 
  
| Gripper on intake | Brake system | 
|  |  | 
| -- |

The Limelight camera is measuring the position in respect to the AprilTag marker on the target. The robot detects how much it needs to move (in X, Y, heading) from the current position and then navigates using odometry to the correct position.

This system is superior to purely navigating based on vision information because:
 * Navigating in a close loop using information from Vision is risky without a global shutter camera because of motion blur.
 * Vision incurs a delay in navigation loop.
 * It uses the tight control loop of odometry.
 * It is unaffected by visual changes during navigation, once the camera has located the target.
 * Mitigates possible odometry drift that may happen after aggressive play.

| Camera capture | Camera positioning |
|  |  |
| -- |

## Competitions & Results

| #   | Event                    | Version | Date       | Ranking Score | NP OPR   | Rank | League Rank |
| --- | ------------------------ | ---------- | ------------- | -------- | ---- | ----------- |
| I   | 🟧 Zilele Roboticii (#4) | 2 | 29.11.2025 | 3.33          | 66.68    | 2    | **1**           |
| II  | ❄️ Snowbotz              | 2 | 07.12.2025 | 3.33          | 85.71 ↗  | **1**    | **1**           |
| III | 🟢 Unlock the Motif      | 3 | 13.12.2025 | 3.50 ↗        | 72.65 ↗  | **1**    | **1**           |
| IV  | 🏛️ Relic Rush            | 3 | 10.01.2026 | 5.50 ↗        | 134.75 ↗ | **1**    | **1**           |
| V   | 🏎️ Future at High Speed  | 3 | 24.01.2026 | **6.00** ↗        | 139.12 ↗ | **1**    | **1**           |


