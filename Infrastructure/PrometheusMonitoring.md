---
title: Prometheus Monitoring
description: 
published: true
date: 2026-02-11T17:27:36.986Z
tags: 
editor: markdown
dateCreated: 2026-02-11T17:12:58.561Z
---

# Uptime Monitoring

Uptime monitoring is based on prometheus. The prometheus central server scrapes all devices enrolled in monitoring every X seconds. 

Each device has a prometheus agent installed that exposes a HTTP service on port 9100. When this endpoint is queried, the prometheus agent queries the system for status (cpu, ram, network, uptime) and returns the result. 

The prometheus server stores thsi data and adds labels to differentiate the source (the IP of ghe device being queried)

# Installation on pis

OS is 64 bit. Wget, tar -xzvf, creste systemd service and daemon-restart.

# Installation on server

Use docker compose. Mount a volume for data and mount a directory for config, because the configs will change often (new devices enrolled). 

Also create container for grafana, with volume for data and configs. 

# 