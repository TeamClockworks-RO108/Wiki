---
title: SPINSPINSPIN
description: 
published: true
date: 2026-04-02T01:51:42.621Z
tags: 
editor: markdown
dateCreated: 2026-04-01T14:27:10.307Z
---

# SPINSPINSPIN


| ![spinspinspin](/spinspinspin_1.png)  | ![spinspinspin](/spinspinspin_6.png) | ![spinspinspin](/spinspinspin_2.png) | ![spinspinspin](/spinspinspin_3.png) |
| -- | -- |


3-board assembly, each designed with 4 layers.
 * 12-18v Supply
 * 15A continous, 25A peak
 * CAN communication
 * USB communication
 * Inline current sensing on all 3 phases
 * 16k PPR Encoder with SPI
 * STM32G474CE 
 * SimpleFOC

> TODO
> Check gain for current sensing amplifier and dimension shunt resistors accordingly. 2m is ok, we might need to go for the 50x gain instead of 20x for the INA240 amplifiers.
{.is-warning}