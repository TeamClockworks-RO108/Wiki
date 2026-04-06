---
title: RouterOS
description: 
published: true
date: 2026-04-06T23:27:02.173Z
tags: infrastructure
editor: markdown
dateCreated: 2025-05-22T15:32:34.476Z
---

# Useful scripts

## Firewall configuration with IRAF

Main configuration of the firewall is built around accepting specific routing options and rejecting everything else.

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
add address=10.12.2.0/24 list=ip_core
add address=10.12.3.0/24 list=ip_alacrity
add address=10.12.0.0/16 list=ip_local_here
```

Create firewall bulk rules.

```bash
/ip firewall connection tracking
set enabled=yes udp-timeout=10s

# Bulk of rules here
add action=accept chain=input comment="Allow OOBE Winbox" dst-port=8291 \
    in-interface=client-oobe protocol=tcp
add action=accept chain=input comment="Allow OOBE HTTP" dst-port=80 \
    in-interface=client-oobe protocol=tcp
add action=accept chain=input comment="Accept already established" \
    connection-state=established,related
add action=accept chain=input comment="Allow traffic on private subnets" \
    src-address-list=allowed_to_router
add action=accept chain=input comment="Allow ICMP" protocol=icmp
add action=drop chain=input comment="Drop all other shit"
add action=accept chain=forward comment="Accept existing connections" \
    connection-state=established,related
add action=drop chain=forward comment="Drop invalid" connection-state=invalid \
    log-prefix=invalid
add action=drop chain=forward comment="Drop packets from WAN not NAT" \
    connection-nat-state=!dstnat connection-state=new in-interface-list=WAN \
    log=yes log-prefix="not nat"
add action=accept chain=icmp comment="echo reply" icmp-options=0:0 protocol=\
    icmp
add action=accept chain=icmp comment="net unreachable" icmp-options=3:0 \
    protocol=icmp
add action=accept chain=icmp comment="host unreachable" icmp-options=3:1 \
    protocol=icmp
add action=accept chain=icmp comment=\
    "host unreachable fragmentation required" icmp-options=3:4 protocol=icmp
add action=accept chain=icmp comment="allow echo request" icmp-options=8:0 \
    protocol=icmp
add action=accept chain=icmp comment="allow time exceed" icmp-options=11:0 \
    protocol=icmp
add action=accept chain=icmp comment="allow parameter bad" icmp-options=12:0 \
    protocol=icmp
add action=drop chain=icmp comment="deny all other types"
add action=jump chain=forward comment="ICMP Filters" jump-target=icmp \
    protocol=icmp
add action=drop chain=forward comment="Drop packets from WAN not in internet" \
    in-interface-list=WAN src-address-list=not_in_internet
add action=drop chain=forward comment="Drop packets from LAN not from LAN IP" \
    in-interface-list=LAN src-address-list=!allowed_to_router
    
# Accept DSTNAT
add action=accept chain=forward comment="Accept DSTNAT'ed" \
    connection-nat-state=dstnat dst-address-list=allowed_to_router

# Each subnet routed locally can access itself
add action=accept chain=forward dst-address-list=ip_core src-address-list=\
    ip_core comment="Loop Core"
add action=accept chain=forward dst-address-list=ip_alacrity src-address-list=\
    ip_alacrity comment="Loop Alacrity"
    
# Which subnet can cross vlans and where
# Who can do internet access
# And who can be accessed from IRAF and access IRAF
add action=accept chain=forward comment="Core to Alacrity" dst-address-list=\
    ip_alacrity src-address-list=ip_core


# External subnets coming from IRAF
add action=accept chain=forward comment="Alex Home Core to All" dst-address-list=\
    ip_local_here src-address=10.2.2.0/24

# Access IRAF interior, by default disabled
add action=accept chain=forward comment="Core to IRAF Interior" \
    dst-address-list=iraf_int src-address-list=ip_core disabled=yes
    
# Access IRAF edge devices, by default disabled
add action=accept chain=forward comment="Core to IRAF Edge" dst-address-list=\
    iraf_edge src-address-list=ip_core disabled=yes

# IRAF Edge can access subnet, default disabled
add action=accept chain=forward comment="IRAF Edge IDP to machines" \
    dst-address-list=ip_guest src-address=10.95.50.0/24 disabled=yes

# Internet access
add action=accept chain=forward comment="Core to Internet" dst-address-list=\
    !not_in_internet src-address-list=ip_core
add action=accept chain=forward comment="Alacrity to Internet" dst-address-list=\
    !not_in_internet src-address-list=ip_alacrity
    

    
# DENY anything else not explicitly allowed
# This is disabled
# Enable after doing modifications
add action=drop chain=forward comment="Drop all other shit" disabled=yes

# Create Hairpin NAT rule
/ip firewall nat
add action=masquerade chain=srcnat comment="Hairpin NAT. USES MIKROTIK SERVER \
    IN PORT FORWARD RULES FOR DDNS LOOKUP. ELIMINATE WITH STATIC IP." \
    dst-address=10.2.0.0/16 src-address=10.2.0.0/16
add action=masquerade chain=srcnat src-address-list=not_in_internet out-interface-list=WAN
add action=dst-nat chain=dstnat comment="Example HTTP" dst-address-list=\
    WAN_IP_MIKDDNS dst-port=80 protocol=tcp to-addresses=10.2.99.99 to-ports=80

```

Create a few other security configs:

```bash
/system clock
set time-zone-name=Europe/Bucharest
/system note
set show-at-login=no
/ip service
set telnet disabled=yes
set ftp disabled=yes
set www address=10.0.0.0/8
set ssh disabled=yes
set api address=10.0.0.0/8
set winbox address=10.0.0.0/8
set api-ssl disabled=yes
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

  
> This page is available both on the [Clockworks Wiki](https://wiki.teamclockworks.ro) and [Alacrity Wiki](https://wiki.alacrity.ro).
> Synchronization is done automatically.
{.is-info}