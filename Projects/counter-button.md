---
title: Counter Button 
description: 
published: true
date: 2026-01-12T02:35:42.756Z
tags: programming, project
editor: markdown
dateCreated: 2025-09-01T21:37:56.641Z
---

# Descriere

 * Proiectul reprezinta un buton care numara cate persoane vin la atelier in fiecare zi.
 * Se va realiza in doua etape. Mai intai se verifica functionalitatea de baza (apasarea de buton) si in a doua faza se vor publica datele intr-un mod usor de citit de echipa.

# Obiective

 * Incepem sa masuram metrici de implicare la atelier. Printre acestea, masuram si in cat de multe zile este minim o persoana la atelier, pentru a opera imprimantele 3D.
 * Invatam sa lucram cu Java pentru Raspberry Pi. First va schimba sistemul de control in viitor catre unul raspberry-based si ne ajuta sa avem experienta cu el din avans.
 * Modernizam sistemele IT din atelier
 
## Phase One

In prima faza a proiectului, vom numara cate apasari se fac pe buton.
La fiecare apasare de buton se va accesa un fisier unde se va specifica numarul de apasari din,apoi va fi transpus intr-o pagina HTML servita local care va contine totalul pentru acea zi . Informatia se reseteaza la 12AM, cand teoretic toata lumea a plecat.

Piesele necesare sunt:

| --- | --- | --- | --- |
| Piesa | Cantitate | Pret | Notes |  
| Raspberry Pi 3B | 1 | 0 | Avem deja |
| Raspberry PoE Hat | 1 | 100 | [TME.EU](https://www.tme.eu/ro/details/sc1022/raspberry-pi-accesorii/raspberry-pi/poe-hat-r2/) |
| Card SD | 3 | 200 | [EMAG](https://www.emag.ro/card-de-memorie-sandisk-micro-sd-high-endurance-video-64-gb-class-10-v30-uhs-i-u3-adaptor-0619659173081/pd/DJ0WFWMBM/). Ne trebuie 1, dar vom lua 3 pentru alte nevoi prin atelier. | 
| Buton Mare | 1 | 30 | [EMAG](https://www.emag.ro/buton-motor-push-5a-fara-retinere-rosu-q-6e016/pd/DGYJWSYBM/?ref=graph_profiled_similar_fallback_1_1&provider=rec&recid=rec_49_b552e7bec827e45b79c5af96a98c2dab04c3aef65fa44398461fa067f9210285_1756748697&scenario_ID=49) | 
| Buzzer | 1 | 20 | [TME.EU](https://www.tme.eu/ro/details/df-dfr0032/alte-module/dfrobot/dfr0032/) | 


## Phase Two

In faza doi a proiectului, vom face o instanta de Home Assistant in care vom centraliza elementele smart ale atelierului. Pentru integrarea cu HASS, vom folosi proiectul [mqttbridge](https://github.com/lucaci32u4/mqttbridge). Acesta permite oricariu device care are un API de read/write sa se prezinte in HASS, cu integrare bidirectionala. Optional, se poate omite un API de write. 

Codul va trebui sa expuna un API. Nu am stabilit inca ce fel de api. Cea mai simpla solutie (si cea mai eleganta) este prin websocket. 

Va fi nevoie de un server local (de care va face rost Alex) care sa contina containere de HASS si MQTT.

| Piesa | Sursa | Notes |
| --- | --- | --- |
| Server HASS | Alex | Va fi un OPS-7101 | 
| Memorie Laptop 16G (2x8 DDR4) | Olx | Va costa 100-150 lei cash | 

# Implementare

Ca sa evitam sa tragem cabluri de power, toata contraptia va primi putere prin cablu de ethernet (de aici si hat-ul de PoE). 
La RPi vom lega butonul cu o rezistenta de pullup. Buzzer-ul se leaga standard (5V, GND, signal). 
Pentru tinerea corecta a timpului vom folosi feature-ul de ceas din sistemul de operare, si vom da drumul si la daemon-ul de NTP. 

# Progres

Am instalat OS-ul pe cardul SD pentru Raspberry Pi