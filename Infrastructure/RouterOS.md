---
title: RouterOS
description: 
published: true
date: 2026-02-24T18:09:26.436Z
tags: infrastructure
editor: markdown
dateCreated: 2025-05-22T15:32:34.476Z
---

# Useful scripts

## Firewall configuration with IRAF

Main configuration of the firewall is built around accepting specific routing options and rejecting everything else.
Do not forget to add both `A->B` and `B->A` routes as TCP connections are bidirectional.

Configure the `WAN` interface list to include the physical port where internet is connected and any carriers it may also have (PPPoE or such). Enable internet detection on these interfaces. Enable DDNS for Hairpin NAT.

```bash
/interface list member
add interface=ether2 list=WAN
add interface=pppoe-out1 list=WAN
/interface detect-internet
set detect-interface-list=WAN internet-interface-list=WAN lan-interface-list=\
    LAN wan-interface-list=WAN
/ip cloud
set ddns-enabled=yes
```

Configure router to respond to DNS queries.


```bash
/ip dns
set allow-remote-requests=yes cache-size=20480KiB max-concurrent-queries=1000 \
    max-concurrent-tcp-sessions=200 query-total-timeout=3s servers=\
    1.1.1.1,8.8.8.8
```

Create address lists for RFC6890 RFC3068 and IRAF addresses.
Set the `WAN_IP_MIKDDNS` to the mikrotik-provided DDNS name.
Configure address lists for local vlans.

```bash
/ip firewall address-list
add address=10.0.0.0/8 list=allowed_to_router
add address=192.168.0.0/16 list=allowed_to_router
add address=0.0.0.0/8 comment=RFC6890 list=not_in_internet
add address=172.16.0.0/12 comment=RFC6890 list=not_in_internet
add address=192.168.0.0/16 comment=RFC6890 list=not_in_internet
add address=10.0.0.0/8 comment=RFC6890 list=not_in_internet
add address=169.254.0.0/16 comment=RFC6890 list=not_in_internet
add address=127.0.0.0/8 comment=RFC6890 list=not_in_internet
add address=224.0.0.0/4 comment=Multicast list=not_in_internet
add address=198.18.0.0/15 comment=RFC6890 list=not_in_internet
add address=192.0.0.0/24 comment=RFC6890 list=not_in_internet
add address=192.0.2.0/24 comment=RFC6890 list=not_in_internet
add address=198.51.100.0/24 comment=RFC6890 list=not_in_internet
add address=203.0.113.0/24 comment=RFC6890 list=not_in_internet
add address=100.64.0.0/10 comment=RFC6890 list=not_in_internet
add address=240.0.0.0/4 comment=RFC6890 list=not_in_internet
add address=192.88.99.0/24 comment="6to4 relay Anycast [RFC 3068]" list=\
    not_in_internet
add address=10.200.0.0/16 list=iraf_int
add address=10.95.0.0/16 list=iraf_edge
add address=192.168.10.0/24 list=iraf_edge
add address=10.5.0.0/16 list=iraf_edge
add address=10.9.0.0/16 list=iraf_edge
add address=10.12.0.0/16 list=iraf_edge

# Edit here
# DDNS name provided by mikrotik
add address=heh08gs3gcg.sn.mynetname.net list=WAN_IP_MIKDDNS


# Edit here
# Local vlans and ip_local_here to the whole local net. 
add address=10.2.2.0/24 list=ip_core
add address=10.2.3.0/24 list=ip_autom
add address=10.2.4.0/24 list=ip_guest
add address=10.2.0.0/16 list=ip_local_here
```

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