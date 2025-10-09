---
title: 3D Printer Usage
description: 
published: true
date: 2025-10-09T02:20:20.488Z
tags: util
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

# Updating your slicer configuration

It is very important to update your slicer configuration to the latest version. The printers will refuse to print a gcode that is sliced using an older version of the slicer configuration. 

1. Download the newest configurations from our [github repository](https://github.com/TeamClockworks-RO108/PrusaSlicerConfig). To download, press the green button and click `Download ZIP`.
2. Extract the contents of the zip file in your PrusaSlicer's config folder. If asked, overwrite any files folders. The possible locations are outlined below:
  * Linux: `~/.config/PrusaSlicer`
  * Windows: `%APPDATA%\PrusaSlicer` (Type this in your file explorer, it will open the right directory)
  
  
# Pre-flight checks

Before printing, please have a look at the printer to ensure that it is operating normally.

- [ ] The printer's mechanics do not look damaged, bent or broken
- [ ] There is filament loaded and it is the same type of filament as in the slicer. 
- [ ] The filament is compatible with the printer

> Before the print, always wipe the bed with Isopropanol. 
{.is-info}


> When in doubt, ***PLEASE*** ask Alex to help figure the issue out.
{.is-warning}

For filament compatibility, as a general rule:
 * Enclosed printers only use ABS and ASA
 * Open printers only use PLA and PETG
 * HIPS can be used as support material on multi-material enclosed printers
 
If a filament profile is not available in the slicer, it generally means that the selected printer is not compatible with it. If you need to print nonstandard setups, talk to us and we will figure out a way to make it work.

## Medina (Voron 2.4 350^3^)

Medina is a large format, enclosed Voron 2.4 printer. It only uses ABS and ASA.

The print sheet should always be used on the smooth side.

Currently, when loading filament, you have to disconnect the bowden tube from the extruder to manually feed the filament inside the gears. The reason for this process is that the extruder body has burrs from CNC machining and feeding from the tube will cause filament to get stuck.

To control the printer, use the [webpage](printer.lucaciresearch.net) or the Ironport terminal. 

## Prusa Mk3S+

Prusa Mk3S+ are the 3D printers that our team has used since 2021 and they have been the most helpful tools for building our robots across the years, allowing us to bring our components and designs into reality. They were bought in the form of kits directly from Prusa and were built by our team with the help of the very user-friendly assembly [manual](https://help.prusa3d.com/manual/original-prusa-i3-mk3s-kit-assembly_1128). The assembly manual can also be used when doing teardowns of the printers to fix any issues, alongside other instructions and suggestions from the [support page](https://help.prusa3d.com/product/mk3s-2). 

The bed sheets attach magnetically to the bed and can be changed with our other sheets stored near the printers. For more information about the materials that can be printed on Prusa Sheets, you can consult [Prusa’s Material Guide](https://help.prusa3d.com/filament-material-guide).
We print PLA on the smooth sheet and PETG on the textured sheet.

For more general information about the PrusaMk3S+ printers you can consult the [printer handbook](https://cdn.prusa3d.com/downloads/manual/prusa3d_manual_mk3s_en.pdf) or read the slightly older physical version present at the workshop, stored near the printers themselves.

To print, put your gcode file on a SD card and insert the SD card into the printer. Navigate on the printer's LCD to find the file and start printing.

# Observability

All Klipper printers are connected to a data collection system called Prometheus. To view the status of the fleet, access the Grafana application from the [Dashboard](https://clockworks-dashboard.lucres.net/). When you open Grafana from the Dashboard, you should be automatically logged in.

> Grafana is a tool that can create visualisations from any given data. It is able to read data from Prometheus, SQL databases, time series databases, log collection systems like Loki and more.
> We use Grafana to create fancy graphs 
{.is-info}

After you open Grafana, you will see an empty welcome page. In the left menu, go to `Dashboards` then select the `Printers` dashboard. You will see a page with overview of the fleet status.

Full history is available for analysys in Grafana. Select your time interval in the top-right box and all charts will update. You can also drag on a graph to zoom in on a time interval.

![screenshot_20251009_051254.png](/screenshot_20251009_051254.png)




