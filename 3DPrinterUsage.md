---
title: 3D Printer Usage
description: 
published: true
date: 2026-01-12T03:29:50.695Z
tags: 3dprinting, guide
editor: markdown
dateCreated: 2024-11-11T18:42:21.941Z
---

# 3D Printer Usage

Please read this page and follow the steps here when using the 3D Printers

3D printers are devices that are able to turn filament into functional components. They work by pushing the filament with the extruder and into the hotend, where it gets melted and pushed through the nozzle. It gets turned into thin layers of plastic that get stacked, starting from the bed, to form the desired components.

All our klipper-based printers can be accessed online over the printer portal located at [printer.lucaciresearch.net](printer.lucaciresearch.net). This URL can also be accessed from the [Dashboard](https://clockworks-dashboard.lucres.net/). 

| ![screenshot_20251009_035232.png](/screenshot_20251009_035232.png) |
| --- |


| Medina | Iron | Envy | Malice | Supermodel | Kraftmaschine |
| --- | --- | --- | --- | --- |
| Voron 2.4 350^3^ | Voron Zero 120^3^ | Prusa i3 MK3S+ | Prusa i3 MK3S+ | DuelingZ | DuelingZ |
# Slicer setup

Our slicer of choice is [PrusaSlicer](https://www.prusa3d.com/page/prusaslicer_424/). After installing, the first time you open the slicer, it will ask which printer models we have. You can select any printers that **you** own.

> Do not select any of the team's printers in the configuration wizard. We maintain a custom repository of configuration and it is ideal we do not stray from it. They will be imported in the next section of this page.
{.is-info}

## Updating your slicer configuration

It is very important to update your slicer configuration to the latest version. The printers will refuse to print a gcode that is sliced using an older version of the slicer configuration. 

1. Download the newest configurations from our [github repository](https://github.com/TeamClockworks-RO108/PrusaSlicerConfig). To download, press the green button and click `Download ZIP`.
2. Extract the contents of the zip file in your PrusaSlicer's config folder. If asked, overwrite any files folders. The possible locations are outlined below:
  * Linux: `~/.config/PrusaSlicer`
  * Windows: `%APPDATA%\PrusaSlicer` (Type this in your file explorer, it will open the right directory)
  
# Bed placement considerations

To ensure that the parts do no warp and lift off the plate, try to break down complex geometry into simpler parts. 

Keep massive, warpy parts off the edges of the buildplate. Because the edges of the buildplate are slightly colder than the center, putting warpy parts on the edge **will** cause the print fail. 
Rounding corners also helps prevent warping.

|  Example: large parts as close to the center |
| ![screenshot_20260107_200513.png](/screenshot_20260107_200513.png) |
| -- |

# Material selection

When choosing a material for a print, take into consideration the following:
 * ABS is very solid and heat-resistant. It holds up well under heavy load. Special care must be taken to prevent warping by careful design and placement on the buildplate. Additives can severely degrade the mechanical properties.
   * Matte ABS (Everfil ABS-L.01 and ABS-M.34) has very poor layer adhesion and break resistance. Use only for decorative prints and some Voron printer parts.
   * Regular ABS has good mechanical properties. This category includes 3DPower, Sakata3D, Everfil ABS-S.01 and other.
   * White ABS is **EXTREMELY** brittle even in filament form. It is very abrasive to extruder gears and nozzles. The cause of this is the addition of TiO~2~ as a whitener. Do not print unless necessary. It can break in the extruder, in filament changers, in the tube or pretty much anywhere.
 * ASA is equivalent to ABS and is resistant to UV degradation. It rarely contains destructive additives.
 * PC is literally ABS on steroids. Mechanical resistance is trough the roof, but it warps severely. It is dense and heavy. Print PC on the Satin sheet only after careful evaluation of the design with Alex or Cristi. Do **NOT** print on Smooth PEI as it will bond permanently. 
 * PCCF is PC with added carbon fibers that reduce the warping effect at the expense of worse layer adhesion and surface finish. Stiffness and dimensional stability is much improved. Careful considerations for:
   * Print on Satin sheet or on Smooth sheet with the reccomandation below.
   * Minimize bed contact area by adding pocketing-like features on the bottom. Use strip width of 8mm and maximum bridge length of 30mm. This can allow you to print with Smooth sheet but take note that if the part warps, it will warp *together with the bed*, or destroy the bed coating.
   * Do not expect smooth surface finish.
   * Does not play well with filament changers (too stiff). Load manually.
   * **WILL** eat right trough extruder gears and nozzles, so talk to Alex or Cristi before pulling the trigger on the print button.
   * 0.6mm nozzle is strongly preffered to prevent the CF jamming.
   * Most printers are not able to keep up with the required temperature on standard profiles and speed, so ensure to lower the speed until the extruder power does not cross 90% consistently. Start at 75% speed and increase if there is headroom.
 * ABS-CF is ABS with carbon fibers added. It is stiff, low-warp but a bit more brittle. It follows the general recomendations of PCCF except that it can be successfully printed on Smooth sheets without fear of damage.
 * PETG is good for prototypes and decorative parts. It has low impact resistance but good printability.
   * If not hit with impact, it will bend before failing. Impacts will cause it to crack instantly.
   * Parts under load slowly get microfractures over time, *without giving any signs of failure*. At some point, they disintegrate into bits. Do not use for gears or moving assemblies.
   * Print only on Prusa with the Textured sheet. 
 * PLA is for kids, we do not use it.

For filament compatibility, as a general rule:
 * Enclosed printers only use ABS and ASA
 * Open printers only use PLA and PETG
 * HIPS can be used as support material on multi-material enclosed printers
 * PC will be printed only on enclosed printers and after careful evaluation of the design. Due to severe adhesion and warping, it can damage PEI sheets. It is a good idea to print it on multimaterial printers (Palmyr) to allow for ABS strain relief features. 
 
If a filament profile is not available in the slicer, it generally means that the selected printer is not compatible with it. If you need to print nonstandard setups, talk to us and we will figure out a way to make it work.

# Spool management

We use spoolman to track the filament usage. Spoolman can be accessed from the Dashboard or at [spoolman.lucres.net](https://spoolman.lucres.net) All the klipper-equipped printers report to spoolman the used quantity of material. 

Each spool is tracked using an unique number (example: `#17`) that is written using a marker on the spool or on the spool box. If opening a new spool, **please** take the time to transfer the writing from the box to the spool itself using a suitable permanent marker. Some spools will have a sticker that you can transfer to the spool.

| ![screenshot_20260106_030348.png](/screenshot_20260106_030348.png) |
| -- |

Before printing, ensure that you have enough filament on the spool. You can typically see this information inside the printer's page in the spoolman section. In this menu you can also eject the spool (`1`) (if using an untracked spool) or change the spool to another (`2`).

| ![screenshot_20260106_031019.png](/screenshot_20260106_031019.png) | ![screenshot_20260106_031140.png](/screenshot_20260106_031140.png) |
| -- | -- |

> Always change the spool configured in the printer when switching spools. If you forget, the printer will keep consuming from the old one and we'll end up with bad data in spoolman.
>
> It is possible to correct this situation by weighing all the affected spools manually and entering the data into spoolman. Ask Cristi or Alex to help with this operation.
{.is-info}

> You might get an error similar to `Cannot reach spoolman instance`. This is because you might not be logged in to the spoolman instance in a long while. To fix it, open the [Spoolman URL](https://spoolman.lucres.net) and then refresh the printer page.
{.is-warning}

## Palmyr integration

Palmyr has a different way to integrate with spoolman. Because there are up to 8 gates/spools, we cannot use the usual spoolman panel to set the filament. If we still use the regular panel and/or macros, the spool will remnain set only until the next load/unload happens, when the data is overriden and lost. 

Palmyr keeps track of spool ID's inside its gate map. To modify the gate map, follow the instructions below:

| Locate the MMU panel and open the Edit Filaments menu inside the dots button | Click on the gate you wish to modify and enable Spoolman. Type the spool ID or click the Choose Spool button to have it auto-filled. To remove a gate from filament tracking, just disable Spoolman from that gate. 
| ![screenshot_20260109_122122.png](/screenshot_20260109_122122.png) | ![screenshot_20260109_122150.png](/screenshot_20260109_122150.png) |
| -- | -- |

The printer will fetch filament's details from spoolman like type, name and color. At each filament switch, the printer will set the appropiate spool ID and Moonraker will submit filament consumption to Spoolman. Selecting a gate will **not** change the current spool, only load operations.  


# Pre-flight checks

Before printing, please have a look at the printer to ensure that it is operating normally.

- [ ] The printer's mechanics do not look damaged, bent or broken
- [ ] There is filament loaded and it is the same type of filament as in the slicer. 
- [ ] The filament is compatible with the printer

> Before the print, always wipe the bed with Isopropanol. 
{.is-info}

> When in doubt, ***PLEASE*** ask Alex to help figure the issue out.
{.is-warning}

## Medina (Voron 2.4 350^3^)

Medina is a large format, enclosed Voron 2.4 printer. It only uses ABS and ASA.

The print sheet to be used is the **PrusaXL Satin sheet**. 

Currently, when loading filament, you have to disconnect the bowden tube from the extruder to manually feed the filament inside the gears. The reason for this process is that the extruder body has burrs from CNC machining and feeding from the tube will cause filament to get stuck.

To control the printer, use the [webpage](https://printer.lucaciresearch.net) or the klipperscreen terminal. 

> The **Satin** sheet does not provide excellent adhesion for large parts. 
> If you need to print large parts, prefer to redesign so that the effects of warping are minimized. If that is not possible, the **Smooth** sheet can be used instead, but PLEASE let us know first.
> The strong adhesion of the **Smooth** sheet combined with significant warping can permanently damage the sheet!
> 
> After using the **Smooth** sheet, always revert to the **Satin** sheet.
{.is-warning}


## Prusa Mk3S+

Prusa Mk3S+ are the 3D printers that our team has used since 2021 and they have been the most helpful tools for building our robots across the years, allowing us to bring our components and designs into reality. They were bought in the form of kits directly from Prusa and were built by our team with the help of the very user-friendly assembly [manual](https://help.prusa3d.com/manual/original-prusa-i3-mk3s-kit-assembly_1128). The assembly manual can also be used when doing teardowns of the printers to fix any issues, alongside other instructions and suggestions from the [support page](https://help.prusa3d.com/product/mk3s-2). 

The bed sheets attach magnetically to the bed and can be changed with our other sheets stored near the printers. For more information about the materials that can be printed on Prusa Sheets, you can consult [Prusa’s Material Guide](https://help.prusa3d.com/filament-material-guide).
We print PLA on the smooth sheet and PETG on the textured sheet.

For more general information about the PrusaMk3S+ printers you can consult the [printer handbook](https://cdn.prusa3d.com/downloads/manual/prusa3d_manual_mk3s_en.pdf) or read the slightly older physical version present at the workshop, stored near the printers themselves.

To print, put your gcode file on a SD card and insert the SD card into the printer. Navigate on the printer's LCD to find the file and start printing.

> They are pending an upgrade to Mk3.5. Cristi and Dragos, please update this section once the printers are upgraded with instructions for prusaconnect after Alex configures it. 
{.is-success}


# Observability

All Klipper printers are connected to a data collection system called Prometheus. To view the status of the fleet, access the Grafana application from the [Dashboard](https://clockworks-dashboard.lucres.net/). When you open Grafana from the Dashboard, you should be automatically logged in.

> Grafana is a tool that can create visualisations from any given data. It is able to read data from Prometheus, SQL databases, time series databases, log collection systems like Loki and more.
> We use Grafana to create fancy graphs 
{.is-info}

After you open Grafana, you will see an empty welcome page. In the left menu, go to `Dashboards` then select the `Printers` dashboard. You will see a page with overview of the fleet status.

Full history is available for analysys in Grafana. Select your time interval in the top-right box and all charts will update. You can also drag on a graph to zoom in on a time interval.

![screenshot_20251009_051254.png](/screenshot_20251009_051254.png)

# Extruder Multiplier Calibration

Create a 55mm^3^ cube in the slicer. Do the following settings:
 * Layer height: 0.2mm
 * Bottom layers: 3
 * Top layers: 269
 * Infill: Gyroid, 15%
 * Perimeters: 3
 * Filament Extrusion Multiplier: 1
 
Print the cube. After it has finished doing infill layers, lower the EM until there are gaps between the lines. Then, slowly raise it, waiting 5-6 layers between each change. When the EM is too much, you will start to see extra filament buildup on the layers.
Perfect EM will have a nice finish of fused lines at the **center of the surface**. Disregard the edges where material builds up because of movement changes.

## Calibrating the `rotation_distance` printer (hardware) value

Do the sequence above with the **REFERENCE ABS** roll loaded. This roll is a blue Everfil filament that is **only** used for reference calibration across printers. To save the value, go to the printer configuration and replace the value of `rotation_distance` with the new calculated value by this formula:

```java
rotation_distance = rotation_distance * 100 / EM 
```

## Calibrating the extrusion multiplier slicer value

To be able to obtain accurate values from this test, the printer's `rotation_distance` should be calibrated first. 

This process should be done with **every type and brand** of filament we own. Save the value in the slicer's filament extrusion multiplier setting (scale 0-100% to 0-1).

## Reference 
![emprints-coarse-annotated.png](/emprints-coarse-annotated.png)

## Shortcuts

Conversion between filament units:
 * 1 mm = 2.4 mm^3^
 * 1 mm^3^ = 0.415 mm


# Special maintenance

## Printer cleanup

All Vorons have a tendancy to accumulate plastic bits at the bottom, so make sure to remove them often. You can use a vacuum cleaner for this task.

## Palmyr Blobifier tray
After quite a few filament loads and unloads, the blobifier tray will fill up with purged blobs. Simply take it out by pulling the tab on the left towards the front and empty inside a trashcan.

## Palmyr ERCF servo startup

Due to unusual behaviour of the Axon servo at startup, it will vibrate aggressively until it is commanded to go to a position. 
If you hear it vibrate after bootup, go to the ERCF menu, the Manage aubmenu and order to servo to go to the Move or Up position.

## Palmyr ERCF servo horn

If the loading of material starts behaving eratically and does not have enough grip, it is very possible that the servo horn is worn out.
Print [this servo horn](https://github.com/moggieuk/ERCF-Springy/blob/main/Savox_Servo_Option/%5Ba%5D_Servo_Arm_Savox.stl). The screw at the center is nonstandard, so make sure to not strip it and keep it safe during the repair. 