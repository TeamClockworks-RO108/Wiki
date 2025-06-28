---
title: RouterOS
description: 
published: true
date: 2025-06-28T23:41:40.875Z
tags: 
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
pulumi stack --show-urns | grep URN | grep A- | awk '{print $3}' | xargs -I {} pulumi state delete {}
```