---
title: Prometheus Monitoring
description: 
published: true
date: 2026-02-11T17:12:58.561Z
tags: 
editor: markdown
dateCreated: 2026-02-11T17:12:58.561Z
---

# Uptime Monitoring

Uptime monitoring is based on prometheus. The prometheus central server scrapes all devices enrolled in monitoring every X seconds. 

Each device has a prometheus agent installed that exposes a HTTP service on port 9100. When this endpoint is queried, the prometheus agent queries the system for status (cpu, ram, network, uptime) and returns the result. 

The prometheus server stores thsi data and adds labels to differentiate the source (the IP of ghe device being queried)

