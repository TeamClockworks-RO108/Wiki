---
title: RouterOS
description: 
published: true
date: 2026-01-16T01:36:56.707Z
tags: infrastructure
editor: markdown
dateCreated: 2025-05-22T15:32:34.476Z
---

# Useful scripts

## Add all new LTE interfaces to the WAN list
Useful when using USB tethering functionality of a smartphone to share internet connection to a RouterOS router.
Configure this script to run every minute or so.

```bash
# Define the interface list name where LTE interfaces should be added
:local interfaceListName "WAN"

# Loop through all interfaces
:foreach i in=[/interface lte find] do={

    # Get the name of the LTE interface
    :local ifaceName [/interface get $i name]

    # Check if the interface is already in the interface list
    :if ([/interface list member find where list=$interfaceListName and interface=$ifaceName] = "") do={

        # Add the LTE interface to the interface list
        /interface list member add list=$interfaceListName interface=$ifaceName

        :log info ("Added LTE interface " . $ifaceName . " to list " . $interfaceListName)
    }
}
```

## Wipe all pulumi resources by a prefix

Can happen that pulumi loses connection details and resources need to be wiped en-masse. In this example `A-` is the prefix we're searching for.


```bash
export PULUMI_CONFIG_PASSPHRASE=...
pulumi stack --show-urns | grep URN | grep A- | awk '{print $3}' | xargs -I {} pulumi state delete {}
```


## Get information about printers, profiles and filaments

```bash
# Get a printer profile name. will list one printer per line
prusa-slicer --query-printer-models | grep -v 'error' | jq '.printer_models.[] | .variants[] | select (.user_printer_profiles != null) | .user_printer_profiles[] | select (.name | startswith("Iron")).name' -r

# Get print profiles for a printer
prusa-slicer --printer-profile "$PRINTER" --query-print-filament-profiles | grep -v error | jq '.user_print_profiles[].name' -r

# Get filament profiles for a printer
prusa-slicer --printer-profile "$PRINTER" --query-print-filament-profiles | grep -v error | jq '.user_print_profiles[] | select (.user_filament_profiles != null) | .user_filament_profiles[]' | jq -s 'sort | unique | .[]' -r

```


Replace R7 (20k, code 30C) with 22k. Size is imperial 0603
Tme link: https://www.tme.eu/ro/details/smd0603-22k-1%25/rezistente-smd/royalohm/0603saf2202t5e/

Inaltime birou Alex: 75.3 grosime placa 2cm
Inaltime birou Ioana: 76.7 grosime placa 2.5cm
Latime blat 50
Lungime blat 135
Inaltime suport 12


# Programming Swyft servos


The initial instructions were incomplete, but here is the bottom line, if you didn't source a programmer from them:

USB to TTL converter (CP2102 works)

  * 3 kΩ resistor across TxD and RxD

  * RxD → Servo gray wire (Servo pwm)

  * +5V → Servo center black wire (Servo 5V)

  * Gnd → Servo remaining black wire (Servo Gnd)