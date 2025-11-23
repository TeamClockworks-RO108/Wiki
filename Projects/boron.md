---
title: Boron
description: 
published: true
date: 2025-11-23T00:14:55.080Z
tags: 
editor: markdown
dateCreated: 2025-10-07T00:54:49.380Z
---

# Description

Boron (Box-Voron) is an open-source light cube that can be built for relatively cheap. The sides graphics are interchangeable and allow for quick reconfiguration by unscrewing the top of the frame. It allows us to display a large logo on a structure very similar to Voron printers.

The project is licensed under [GNU General Public License Version 3](https://www.gnu.org/licenses/gpl-3.0.en.html). This means, among others, that distributing either STL, printed parts or assemblies containing Boron, you must also make the modified CAD available to users. 

The design is built so that minimal electronics and soldering work is required. A 10-meter LED strip is cut into 4 equal sections and is wrapped around the cube's guide channels. Each strip's end arrives at the top of the cube, where it transitions to the top face.

The bottom of the cube contains two output wall sockets to aid with wiring. (Maybe chain more Borons?).



| ![screenshot_20251029_015652.png](/screenshot_20251029_015652.png) | ![screenshot_20251029_015722.png](/screenshot_20251029_015722.png) | ![screenshot_20251029_015741.png](/screenshot_20251029_015741.png) | ![screenshot_20251029_015841.png](/screenshot_20251029_015841.png) |
| -- | -- | -- | -- |

# Printing

Most of the parts fit on a 300^3^ printer, but the bottom and top crossbars should be printed on a 350^3^ machine. 
Use 3-4 perimeters for all parts and 25% gyroid infill. A thicker line width for infill will speed up the print a lot and add extra strangth. 

For the external and internal feet, we recommend at least 5 perimeters to ensure these will not creep over time. 

Many holes for M3 screws are dimensioned at 4.7mm. Insert heatset threaded inserts into these holes with a soldering iron. Perfect centering is not crucial because the design makes use of slots in many places where heat inserts are placed. In total, you should use 54 inserts.

# Flashing ESPHome on the Shelly controller

For this step, you will need a standard USB-UART converter. CH340 or FT232 modules work perfectly. A computer with linux environment is strongly recommended.

Flash the firmware onto the Shelly controller before assembling the electronics. Doing so after will complicate the setup a lot. 

## Connecting UART wires

A breadboard can be very useful for making connections because we will have to connect GND to two different places. The back of the shelly contains a few pins for flashing. The slots for pins are very small, therefore use wires from inside a CAT5A network cable that have solid copper cores. 

Ensure that your UART adapter is set to work at 3.3v levels, as the ESP inside shelly does not tolerate 5v signaling. 

Connect the UART adapter to the shelly as follows:
| Shelly | UART Adapter | 
| --- | --- |
| U0TXD | RX | 
| U0RXD | TX | 
| GND | GND |
| GPIO0 | GND |
| RESET | EN/DTR |
| +3.3_ESP | +3.3v |


| ![screenshot_20251121_031121.png](/screenshot_20251121_031121.png) |
| -- |

## Flashing

Power on the assembly by connecting the USB adapter to your linux computer, and take note of the serial port:

```bash
# Show all serial ports that are not system ports
ls  /dev/* | grep 'tty[^S0-9]'
```

Install the ESPHome toolkit:

```bash
# Arch linux
sudo pacman -S esphome

# Debian, Ubuntu, others
sudo pip install wheel esphome --break-system-packages

# Test your installation
esphome --version
```

Clone the repository with ESPHome config files and start flashing:

```bash
# Clone the repo
git clone https://github.com/TeamClockworks-RO108/Boron.git
cd Boron/firmware

# Flash. Replace /dev/tty<port> with your serial port obtained above.
esphome run boron-basic.yaml --device /dev/tty<port>
```



# Assembly

We will assemble the frame first, together with its internal and external feet and then build the inner LED cube.
At the end, we will combine both and wire up the electronics. 

## Frame

## Access holes

Use the extrusion drill guide to drill access holes for blind joints into all of the 500mm extrusions (4). You should drill 4 holes for each extrusion (a cross at each end). Use a 3mm drill bit. 

In total, 16 holes need to be drilled (4 beams x 2 ends x 2 holes).

Assemble the frame using 16x 8mm M3 BHCS. Use a flat surface to ensure the frame will be perfectly square.
When assembling the bttom face, preload the following Makerbeam XL Nuts:
 * 2 nuts on **each** extrusion on the bottom side
 * 4 nuts on **each** extrusion on the inside of the cube. On one side (that will be the back side) preload 7 nuts. 
 
A total of 27 nuts must be preloaded. 
 
| ![screenshot_20251029_024344.png](/screenshot_20251029_024344.png) | ![screenshot_20251029_025219.png](/screenshot_20251029_025219.png) |
| -- | -- |

Mount the external feet using 3x 16mm M3 BHCS and the internal feet using 4x 16mm M3 BHCS.
The middle screw of the external foot threads into the extrusion. 
Use the preloaded nuts in the earlier steps.

| ![screenshot_20251029_030341.png](/screenshot_20251029_030341.png) | ![screenshot_20251029_030245.png](/screenshot_20251029_030245.png) |
| -- | -- |

Final assembled frame

| ![screenshot_20251029_030642.png](/screenshot_20251029_030642.png) |
| -- |
 

## LED Structure

Assemble the main LED structure using 32x 16mm M4 SHCS screws. Connect the brackets to the main pillars and use the two crosses to fasten the 4 corners.

The two crosses **are not identical**! The top cross contains heated inserts on the upper side that will later be used to mount the top face LED channels. Install this part on the same side with the filleted pillars. 

The bottom cross has only 4 regular holes for mounting of the PSU and electronics. 

Afterwards, install the rigity supports at the top using 16x 16mm M4 SHCS screws. These beams help stabilize our build. 

| ![screenshot_20251029_033556.png](/screenshot_20251029_033556.png) | ![screenshot_20251029_033737-1.png](/screenshot_20251029_033737-1.png) | ![screenshot_20251029_035000.png](/screenshot_20251029_035000.png) |
| -- | -- | -- |


Install the 20 lateral LED channels. Mount them with 40x 8mm M3 BHCS screws. The channels have slots that allow good mounting even if the frame is not prefectly square. 

Afterwards, mount the top face LED channel using 4x 8mm M3 FHCS. These screws will go in the heatset inserts inside the top cross. 

| ![screenshot_20251029_035526.png](/screenshot_20251029_035526.png) |  ![screenshot_20251029_035542.png](/screenshot_20251029_035542.png)|
| -- | -- |

The LED structure is now ready for mounting inside the main frame. Use 16x 16mm M4 SHCS.

| ![screenshot_20251029_040306.png](/screenshot_20251029_040306.png) | ![screenshot_20251029_040338.png](/screenshot_20251029_040338.png) |
| -- | -- |

## Electronics

Start by inserting the 6 heat inserts. Then, fix in place the sockets and the C13 power plug using 10x 10mm M3 FHCS. 
To install the potentiometer, unscrew the included nut and put it trough the hole. Then, screw back the included plastic nut.

Secure the WAGO holder into the utility panel body using 2x 16mm M3 BHCS. To make the WAGO connectors stay in place, we can use Cyanoacrylate glue or hot glue. 

| ![screenshot_20251121_023725.png](/screenshot_20251121_023725.png) | ![screenshot_20251121_023804.png](/screenshot_20251121_023804.png) |
| -- |

Assemble the Shelly holder by sliding the shelly relay inside and securing it into place with its small bracket and 2x 10mm M3 BHCS. 
Use the same glue technique as above to install the 4 WAGO connectors.

| ![screenshot_20251121_024231.png](/screenshot_20251121_024231.png) |
| -- |

## Wiring

To properly program the elctronics, we will assemble and test the **wiring** outside the cube!
The wires between individual components nearby should be small. Eyeball each length to your preference. Wire lengths between different places inside the cube should be:
 * Utility panel (potentiometer) to shelly circuit - **300mm**
 * Utility panel to PSU (AC side) - **130mm**
 * PSU (DC side) to shelly circuit - **270mm**
 * Shelly circuit to LED strip start - **360mm**
 
All screw terminal connections (on the shelly relay or power sockets) should use crimped ferrules to prevent accidental disconnections.
Wires connected to wago terminals do not ferrules, but ensure that about 8-11mm of wire length is unsheathed. 

### Utility panel

When wiring the utility panel, take extra care to ensure that the neutral line (yellow, often found as yellow-green) does not mix with the two power lines. 

The potentiometer has three connection points: two ends and one center tap. We will wire one single end and the center tap, wires which will go to the shelly circuit. Dimension the wire accordingly. 

| ![screenshot_20251121_015217.png](/screenshot_20251121_015217.png) |
| -- |

### Shelly circuit

Follow the diagram below to wire the shelly circuit.

| ![screenshot_20251121_020634.png](/screenshot_20251121_020634.png) |
| -- |

### PSU

Connect the power wires coming from the utility panel to the PSU's AC side. Take extra care to find the right connector for the neutral wire.

Connect the +24V wires from shelly circuit to the PSU's DC side, respecting polarity. 

### LED Strips

Cut your 10m strip into 4 equal 2.5m sections and solder one end of each strip to the LED wires coming from the shelly circuit. 

## Power on & Check circuit.

> Before connecting power to the assembly, `ENSURE` that all AC connections are properly done and there are no exposed wires. There should be no connection between the AC circuit and DC circuit `EXCEPT` trough the PSU itself. 
> The DC section is relatively safe to touch, but please take care. Do `NOT` touch the AC side of the circuit in `ANY` circumstance.
{.is-warning}


# Old description

The structure is constructed similarly to a Voron frame. There are 4 vertical beams measuring 500mm and 8 horizontal beams measuring 470mm.

The 8 smaller beams are ordered from [Makerbeam](makerbeam.com) as longer 500mm extrusions and you should add to the cart 8 cuts and specify to cut them to 470mm.

All of the extrusions should be of type MakerbeamXL.


The cube will have feet to hold it at least 20mm off the ground to allow for cables to go underneath. We must look for an option to attach a standard PC socket connector to allow cable choice flexibility. 


The center will have a continous, square coil of LED strip. We should choose standard 9mm strip and design with clearance in mind (at lease 11mm of space).

The PSU will be MeanWell, from the UHP range, but for budgeting purposes we can design to attach a cheaper LRS option. 

To prevent overheating of the wires, everyting will work at 24v. Electronics will be controlled using a Shelly Plus RGBW PM (ABSOLUTE MAX 10A, 4A per ch, 4ch)

# Parts List

| Part | P/N | Price | Notes | 
| -- | -- | -- | -- |
| Shelly controller | Shelly Plus RGBW PM | 140 | |
| Wall socket | Gewiss GW 62 393 | 30 | |
| Potentiometru 10k | Tayieei LA42DWG-22 | 30 | For 22mm bore |
| 10m white neutral strip | | 120 | At most 10A/240W |
| 7x Wago 221 415 5-wire | | 70 | |
| IEC C13 Socket |  | 6 | | 
| IEC C13 Cable with 90* bend |  | 30 | | 
| 24V PSU | Meanwell UHP-350-24 | 370 | |
| Frame | | TBD | |
| Panels | | TBD | | 
| _**FASTENERS**_ ||||
| M3 Voron threaded inserts || 54 ||
| M3 BHCS (DIN 7380) 8mm || 64 ||
| M3 BHCS (DIN 7380) 16mm || 46 ||
| M3 BHCS (DIN 7380) 10mm || 10 ||
| M3 BHCS (DIN 7380) 40mm || 3 ||
| M3 FHCS (DIN 7991) 8mm || 18 || 
| M3 SHCS (DIN 912) 16mm || 40 ||
| Makerbeam T-Nut XL || 27 ||


The strip has 10m and must be divided on 5 equal sides, so each side must use up to 2m
