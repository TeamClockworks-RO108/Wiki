---
title: 3D Printer Usage
description: 
published: true
date: 2026-02-18T17:34:20.863Z
tags: 3dprinting, guide
editor: markdown
dateCreated: 2024-11-11T18:42:21.941Z
---

# 3D Printer Usage

Please read this page and follow the steps here when using the 3D Printers

3D printers are devices that are able to turn filament into functional components. They work by pushing the filament with the extruder and into the hotend, where it gets melted and pushed through the nozzle. It gets turned into thin layers of plastic that get stacked, starting from the bed, to form the desired components.

All our klipper-based printers can be accessed online over the printer portal located at [printer.lucaciresearch.net](printer.lucaciresearch.net). This URL can also be accessed from the [Dashboard](https://clockworks-dashboard.lucres.net/). 

| ![printer-web-menu.png](/printer-web-menu.png) |
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
  
> ### Updating from old installs
> If you are updating your existing installation and you have old profiles, always prefer to nuke the old configuration (delete the config folder outlined above).
> If you need to keep some of your old configs, go to your config folder and identify all print, printer and filament profiles you wish to keep. Delete all other. 
{.is-success}

  
# Bed placement considerations

To ensure that the parts do no warp and lift off the plate, try to break down complex geometry into simpler parts. 

Keep massive, warpy parts off the edges of the buildplate. Because the edges of the buildplate are slightly colder than the center, putting warpy parts on the edge **will** cause the print fail. 
Rounding corners also helps prevent warping.

|  Example: large parts as close to the center |
| ![printer-bed-placement.png](/printer-bed-placement.png) |
| -- |

# Build plate

Our printers are equipped with magnetic, hot-swappable build plates. All build plates have functioning surfaces on both sides. When switching to a new build plate, follow the general checklist:
 * The plate is correctly dimensioned for the printer.
   * Prusa XL plates for Medina.
   * Prusa Core One plates for Palmyr.
   * Prusa Mini plates for Dueling.
 * Wipe the plate with IPA
 * Ensure correct positioning (example: for Palmyr the plate should not cross under the nozzle wiper)
 * **Check recommandations given in the materials section below.**
 
The printers are usually equipped with a **Satin** sheet. This is the daily setup that we run and it should fit your workkflow too. The **Satin** has a few drawbacks, notably that is does not have that much holding power for our most usual materials (ABS, ASA, PC). Big parts can still warp and small parts can get knocked off during printing. In these cases, you might end up needing much stronger adhesion than Satin, in which cases please switch to the **PEI Smooth** sheet. 
 
| PEI Smooth | Satin | Textured |
| -- | -- | -- |
| Very good adhesion for a wide range of materials. | Decent adhesion for almost all materials imaginable, including first-class support for PC.  | Good adhesion for PETG, but not really useful beyond that. 

> Tree supports tipically do not succeed on the **Satin** sheet using ABS. This is because the bottom layer of the supports is fragile, and combined with the reduced adhesion, may cause the support to fly off the print. Prefer to use Snug supports or better, switch to the **Smooth** sheet
{.is-info}


> The **Satin** sheet does not provide excellent adhesion for large parts **AND** for parts with small contact bases. 
> If you need to print large parts, prefer to redesign so that the effects of warping are minimized. If that is not possible, the **Smooth** sheet can be used instead, but PLEASE let us know first.
> The strong adhesion of the **Smooth** sheet combined with significant warping can permanently damage the sheet!
> 
> After using the **Smooth** sheet, always revert to the **Satin** sheet.
{.is-warning}

# Material selection

When choosing a material for a print, take into consideration the following:
 * ABS is very solid and heat-resistant. It holds up well under heavy load. Special care must be taken to prevent warping by careful design and placement on the buildplate. Additives can severely degrade the mechanical properties.
   * Matte ABS (Everfil ABS-L.01 and ABS-M.34) has very poor layer adhesion and break resistance. Use only for decorative prints and some Voron printer parts.
   * Regular ABS has good mechanical properties. This category includes 3DPower, Sakata3D, Everfil ABS-S.01 and other.
   * White ABS is **EXTREMELY** brittle even in filament form. It is very abrasive to extruder gears and nozzles. The cause of this is the addition of TiO~2~ as a whitener. Do not print unless necessary. It can break in the extruder, in filament changers, in the tube or pretty much anywhere.
   * Print on the regular **Satin** plate except for when printing parts that are susceptible to warp or are too small to keep adhesion during printing. For these cases, switch to **PEI Smooth**.
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

---

> This bit here is not yet implemented, please read but do not take seriously.
{.is-danger}


All of our printers share common filament profiles. Despite having different cooling performance, the fan commands are hijacked by a klipper macro that scales the needed fan around what are the printer's capabilities. 

The fan scaling parameters can be changed using the `TEST_FAN_TUNING` macro. After tuning, don't forget to save the new values in the `KlipperScripts/fan_scale.cfg` file.

```ini
[gcode_macro TEST_FAN_TUNING]

# Test the scale and offset parametes of the overriden M106 fan macro.
# Also allows an override value to be set. If overridden, any value set on the fan
# will use the override value, except if 0 is set, 0 is written.
# Normal operation follows this formula: new_fan = (old_fan * SCALE) + OFFSET
#
#  P A R A M E T E R S :
# SCALE: float to scale the fan with
# OFFSET: float to add after scaling
# OVERRIDE: float to set as raw speed (no scaling and offset!).
#           Takes effect until this macro is called again *without* OVERRIDE.
#           If the macro is called parameterless, it just clears any active overrride.
#
```

# Spool management

We use spoolman to track the filament usage. Spoolman can be accessed from the Dashboard or at [spoolman.lucres.net](https://spoolman.lucres.net) All the klipper-equipped printers report to spoolman the used quantity of material. 

Each spool is tracked using an unique number (example: `#17`) that is written using a marker on the spool or on the spool box. If opening a new spool, **please** take the time to transfer the writing from the box to the spool itself using a suitable permanent marker. Some spools will have a sticker that you can transfer to the spool.

| ![printer-spoolman-label.png](/printer-spoolman-label.png) |
| -- |

Before printing, ensure that you have enough filament on the spool. You can typically see this information inside the printer's page in the spoolman section. In this menu you can also eject the spool (`1`) (if using an untracked spool) or change the spool to another (`2`).

| ![printer-spoolman-mainsail.png](/printer-spoolman-mainsail.png) | ![printer-spoolman-mainsail-annotated.png](/printer-spoolman-mainsail-annotated.png) |
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
| ![printer-palmyr-spoolman-1.png](/printer-palmyr-spoolman-1.png) | ![printer-palmyr-spoolman-2.png](/printer-palmyr-spoolman-2.png) |
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



## Prusa Mk3.5S

Prusa Mk3S+ are the 3D printers that our team has used since 2021 and they have been the most helpful tools for building our robots across the years, allowing us to bring our components and designs into reality. They were bought in the form of kits directly from Prusa and were built by our team with the help of the very user-friendly assembly [manual](https://help.prusa3d.com/manual/original-prusa-i3-mk3s-kit-assembly_1128). The assembly manual can also be used when doing teardowns of the printers to fix any issues, alongside other instructions and suggestions from the [support page](https://help.prusa3d.com/product/mk3s-2). 

In 2026 we chose to upgrade our Prusa Mk3S+ printers to the Prusa Mk3.5S model, using upgrade kits bought from Prusa, and were assembled by our team using the very user-friendly upgrade [manual](https://help.prusa3d.com/manual/original-prusa-i3-mk3s-mk3s-to-mk3-5s-upgrade_2194).

The Prusa Mk3.5S upgrade gives us access to more modern features, such as input shaper, a new screen interface with USB support and printing over network, while maintaining most of the hardware used by the Prusa Mk3S+. These features make the printers run faster than ever while having a more user-accesible interface, helps us print pieces faster and easier than before.

The bed sheets attach magnetically to the bed and can be changed with our other sheets stored near the printers. For more information about the materials that can be printed on Prusa Sheets, you can consult [Prusa’s Material Guide](https://help.prusa3d.com/filament-material-guide).
We print PLA on the smooth sheet and PETG on the textured sheet.

For more general information about the Prusa Mk3.5S printers you can consult [the printer's handbook](https://www.prusa3d.com/downloads/manual/prusa3d_manual_mk35s_101_en.pdf) or read the physical versions present at the workshop, stored near the printers themselves.

To print, remove the printer's USB stick and conect it to the workshop's PC, upload your gcode file on the USB stick and insert the USB stick back into the printer. Press the "Print" button on the printer's LCD screen, select the file you uploaded and start printing.

# Printer Errors

When the printer detects a malfunction, an error is thrown and the print is interrupted. When this situation happens, you will see an error box on the printer page like below:

| ![screenshot_20260218_191526.png](/screenshot_20260218_191526.png) |
| -- |

When this happens, **PLEASE** notify us on Mechanich channels before pressing the `FIRMWARE RESTART` button. Include all the relevant details of the error, so that we can debug the issue later on. It's important to know which is the reported problem. 

# Observability

All Klipper printers are connected to a data collection system called Prometheus. To view the status of the fleet, access the Grafana application from the [Dashboard](https://clockworks-dashboard.lucres.net/). When you open Grafana from the Dashboard, you should be automatically logged in.

> Grafana is a tool that can create visualisations from any given data. It is able to read data from Prometheus, SQL databases, time series databases, log collection systems like Loki and more.
> We use Grafana to create fancy graphs 
{.is-info}

After you open Grafana, you will see an empty welcome page. In the left menu, go to `Dashboards` then select the `Printers` dashboard. You will see a page with overview of the fleet status.

Full history is available for analysys in Grafana. Select your time interval in the top-right box and all charts will update. You can also drag on a graph to zoom in on a time interval.

![printer-grafana.png](/printer-grafana.png)

## Using Grafana to investigate errors

It is possible to use the grafana's history of temperatures to investigate different situations regarding heater issues.

To make reading easier, the power field (scale 0-1) is multiplied by current temperature. This causes the power line to *touch* the temperature line when power is maxed.

In the graph below we can see that at some point in the print, the extruder temperature sagged a bit. We can also see the power field maxxing (touching the temperature line). This indicates that the heater was not able to keep up with the required temperature due to unexpected cooling events.  Possible causes are:
 * Too much cooling for localized features (for example, bridges, overhangs). Cooling looks OK for general cooling as there is no sag for the entirety of the print
 * Silicone sock is damaged and normal cooling for bridges overpower the extruder's heating ability.
 
We can also see a slight increase in chamber temperatures at that point, possibly meaning power dissipation indeed rises, caused by cooling and mis-isolation. 

| ![screenshot_20260218_192723.png](/screenshot_20260218_192723.png) |
| -- |




# Extruder Multiplier Calibration

Create a 55mm x 30mm x 55mm (Z) cube in the slicer. Do the following settings:
 * Layer height: 0.2mm
 * Bottom layers: 3
 * Top layers: 269
 * Infill: Gyroid, 15%
 * Perimeters: 3
 * Filament Extrusion Multiplier: 1
 * Fill pattern: Archimedean chords
 
> `TODO` Change process to use archimedean chords like in [orcaslicer](https://www.orcaslicer.com/wiki/calibration/flow-rate-calib.html).
{.is-success}

 
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
![printer-em-calibration.png](/printer-em-calibration.png)

# Printing small details

If printing very small details (like teethed pulleys),  apply the following settings to print:
 * Layers and Perimeters -> Perimeter generator: Classic
 * Speed -> Acceleration control -> Default: 1000

# Slicer profile mapping

PrusaSlicer includes features to restrict filament and printer profilese to a specific set of printers.

Set default filament and print profiles by opening the printer file and change these lines:

```ini
default_filament_profile = "Prusament PLA @MK3.5"
default_print_profile = 0.20mm SPEED @MK3.5 0.4
```
---
Configure for each printer a model.
```ini
printer_model = CVoron24
printer_model = CVoron24-ERCF
printer_model = CVoron0
printer_model = CMK35
```

Configure for each material what printers can use it. Restrict based on cooling performance, temperature compatibility and extruder type. If the filament is specific for a single printer, please prefix the filament name with the printer's name (not the `printer_model` above) and restrict it properly.
```ini
compatible_printers_condition = printer_model=="CVoron24" or printer_model=="CVoron0"
```

For filament compatibility, restrict based on compatible printers and nozzle diameter.
Take into consideration multimaterial handling. 
```ini
compatible_printers_condition = printer_model=="CVoron24" and nozzle_diameter[0]==0.4
```



# Special maintenance

## Printer cleanup

All Vorons have a tendancy to accumulate plastic bits at the bottom, so make sure to remove them often. You can use a vacuum cleaner for this task.

## Palmyr Blobifier tray
After quite a few filament loads and unloads, the blobifier tray will fill up with purged blobs. Simply take it out by pulling the tab on the left towards the front and empty inside a trashcan.

## Palmyr ERCF servo startup

Due to unusual behaviour of the Axon servo at startup, it will vibrate aggressively until it is commanded to go to a position. 
If you hear it vibrate after bootup, go to the ERCF menu, the Manage submenu and order to servo to go to the Move or Up position.

## Palmyr ERCF servo horn

If the loading of material starts behaving eratically and does not have enough grip, it is very possible that the servo horn is worn out.
Print [this servo horn](https://github.com/moggieuk/ERCF-Springy/blob/main/Savox_Servo_Option/%5Ba%5D_Servo_Arm_Savox.stl). The screw at the center is nonstandard, so make sure to not strip it and keep it safe during the repair. 

# Shortcuts

Conversion between filament units:
 * 1 mm = 2.4 mm^3^
 * 1 mm^3^ = 0.415 mm