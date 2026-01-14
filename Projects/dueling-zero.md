---
title: Dueling Zero 3DP
description: 
published: true
date: 2026-01-12T02:36:25.469Z
tags: mechanics, 3dprinting, project, voron
editor: markdown
dateCreated: 2025-05-18T00:26:10.510Z
---

# Descriere
**Dueling Zero** este o imprimanta 3D de ultima generatie, complet open-source, bazata pe designul imprimantei Voron Zero, care introduce o arhitectura inovatoare cu doua gantry-uri independente (Dual Gantry). 
Beneficiaza de un sistem IDEX (Independent Dual Extrusion - 2 capete de printare independente), care permite printarea simultana cu 2 culori diferite sau 2 materiale diferite intr-un singur print. Este conceputa pentru precizie, viteza si versatilitate.

| ![alt_text](/duelingzero-render-top.png){.align-center} | ![alt_text](/duelingzero-render-iso.png){.align-center} | ![alt_text](/duelingzero-gantry-iso.png){.align-center}
| - | - | - |

Pentru mai multe detalii se poate accesa link-ul de GitHub [Dueling Zero](https://github.com/zruncho3d/DuelingZero?tab=readme-ov-file).

# Etapele proiectului
1. Studierea documentatiei oficiale [Dueling Zero](https://github.com/zruncho3d/DuelingZero?tab=readme-ov-file), unde se gasesc fisiere STL pentru piese printate, lista de piese si instructiuni necesare pentru construirea imprimantei.
2. Achizitionarea componentelor conform *Tabelului de achizitii* de mai jos.
3. Printarea pieselor de plastic pe o alta imprimanta 3D.
4. Asamblarea structurii mecanice:
	- Asamblarea cadrului principal (cubul de baza) format din profilele de aluminiu
	- Asamblarea gantry-ului dublu si montarea pe cadrul imprimantei
	- Asamblarea kit-ului pentru patul de printare si montarea acestuia pe sina de miscare verticala (Z)
	- Montarea celor 2 extrudere (capete de printare)
5. Realizarea conexiunilor electrice
6. Instalarea si configurarea firmware-ului Klipper
7. Testarea si calibrarea imprimantei.

# Imbunatatiri

Am discutat urmatoarele idei si vom incepe proiectarea pieselor pentru ele:

## Re-rutarea tubului bowden catre exteriorul imprimantei
Tubul bowden merge catre rolele pozitionate in interior. Pentru ca preferam sa tinem rolele in exterior, vom muta traseul tubului catre exterior, similar ca la imprimanta Voron V0.2

Tubul existent in proiect este desenat cu verde. Rosu este extensia pe care noi o vom adauga.

| ![screenshot_20250524_195636.png](/screenshot_20250524_195636.png) |
| --- |

## Renuntam la afisajul integrat si folosim ecran pe retea

Afisajul integrat este greu de controlat, si are textul foarte mic, deci devine greu de citit de la distanta. Multe informatii sunt greu de gasit deoarece afisajul nu este grafic, ci este display de caractere.

In loc, vom folosi un Raspberry conectat la un touchscreen cu alimentare prin PoE. Asa avem mult mai multe controale. Pe Pi va rula KlipperScreen si va avea configurate toate imprimantele in el. 

| ![whatsapp_image_2025-05-24_at_8.05.53_pm.jpeg](/whatsapp_image_2025-05-24_at_8.05.53_pm.jpeg) | ![whatsapp_image_2025-05-24_at_8.05.06_pm.jpeg](/whatsapp_image_2025-05-24_at_8.05.06_pm.jpeg) |
| --- | --- |

## Inlocuirea placii de pe carriage EBB42 cu EBB36

Inlocuirea nu necesita nici o modificare la imprimanta. EBB36 este mai compact si ofera o organizare mai buna a firelor in jurul ei. In plus, este ce avem deja pe celalate imprimante ale noastre si stim bine cum sa o configuram.


# Tabel de achizitii
| **Item** | **Cantiatate necesare** | **Cantitate cumparat** | **Livrare gratuita** | **Pret (RON)** | **Link** | **Comentarii** |
| :---- | -------------: | --------------: | :-----------: | ----------: | :--- | :------- |
| Can Toolboard EBB36  | 2 | 1x (2-pack) | Yes | 128 | [BIQU](https://biqu.equipment/products/bigtreetech-ebb-36-42-can-bus-for-connecting-klipper-expansion-device?variant=39833569689698) | |
| Octopus with 8 drivers | 1 | 1 | Yes | 580 | [BIQU](https://biqu.equipment/products/bigtreetech-octopus-v1-1?variant=40171130519650) | |
| Sherpa Crew Ali Metal kit | 2 | 2 | Yes | 600 | [AliExpress](https://www.aliexpress.com/item/1005007469813414.html?spm=a2g0o.productlist.main.1.7fc51ff2hCa9on&algo_pvid=d9065ecc-37ce-441a-af5e-97508542c5a6&pdp_ext_f=%7B%22order%22%3A%222%22%2C%22eval%22%3A%221%22%7D&utparam-url=scene%3Asearch%7Cquery_from%3A) | |
| 50mm MGN9H | 2 | 2 | No | 130 | [3do.dk](https://3do.dk/en/linear-rails/1451-honeybadger-stainless-mgn9h-rail.html) | For Boops |
| 300mm MGN7H  | 2 | 2 | Yes | 85 | [AliExpress](https://www.aliexpress.com) | |
| 250mm MGN9H | 2 | 2 | Yes | 106 | [AliExpress](https://www.aliexpress.com) | |
| MGN7H Carriage only | 2 | 2 | Yes | 51 | [AliExpress](https://www.aliexpress.com) | |
| 200mm MGN7H | 4 | 4 | Yes | 120 | [AliExpress](https://www.aliexpress.com) | |
| Bed Hardware | 1 | 1 | Yes | 302 | [AliExpress](https://www.aliexpress.com/item/1005007084645274.html?spm=a2g0o.productlist.main.9.bd2f3738oWsyZr&algo_pvid=8b0a737f-84df-4d29-8a4b-2406c81b71a4&pdp_ext_f=%7B%22order%22%3A%226%22%2C%22eval%22%3A%221%22%7D&utparam-url=scene%3Asearch%7Cquery_from%3A) | Complete kit | 
| F623 Bearing | 70 | 70 | Yes | 160 | [AliExpress](https://www.aliexpress.com/item/1005008385551788.html?spm=a2g0o.productlist.main.2.597b1f06wXwFjb&algo_pvid=d10b01b0-f21c-4426-9e6c-6203117c6cfd&pdp_ext_f=%7B%22order%22%3A%2244%22%2C%22eval%22%3A%221%22%7D&utparam-url=scene%3Asearch%7Cquery_from%3A) | ABEC3, (64 + 6)pcs | 
| Hotend Dragon HF Alu | 2 | 2 | Yes | 468 | [Triangle-Lab](https://trianglelab.net/products/dragon-hotend?VariantsId=11396) | We don't know if the ceramic heatbreak is better. |
| Thermistor Hotend | 2 | 1x (2-pack) | Yes | 116 | [Traingle-Lab](https://trianglelab.net/products/pt1000-pro?VariantsId=12120) | |
| Heater Hotend | 2 | 2 | Yes | 50 | [REPRAPMANIA](https://www.reprapmania.ro/cumpara/cartus-de-incalzire-24v-50w-pentru-voron-2527) | |
| TriZero Fulie | 3 | 3 | Yes | 72 | [REPRAPMANIA](https://www.reprapmania.ro/cumpara/fulie-dintata-gates-powergrip%C2%AE-2gt-16-dinti-curea-6mm-ax-5mm-1267) | |
| Gantry Fulie 20T | 4 | 4 | Yes | 96 | [Reprapmania](https://www.reprapmania.ro/cumpara/fulie-dintata-gates-powergrip%C2%AE-2gt-20-dinti-curea-6mm-ax-5mm-1266) | |
| XY XY Belt | 90 | 90 | Yes | 306 | [Reprapmania](https://www.reprapmania.ro/cumpara/curea-gates-powergrip%C2%AE-2gt-6mm-x-100mm-1265) | 7000 mm + 2000 mm |
| Sursa LRS-350-24 | 1 | 1 | Yes | 183 | [CONEX ELECTRONIC](https://www.conexelectronic.ro/surse-mean-well/18092-SURSA-LRS-350-24-24V-14-6A-MEAN-WELL-5949203901620.html?ssa_query=LRS-350-2) | |
| Keystone RJ45 | 1 | 1 | Yes | 50 | [eMAG](https://www.emag.ro/conector-modul-keystone-jack-cat6-lankatt-ftp-stp-ecranat-full-shield-autosertizare-toolless-modular-suport-de-cabluri-integrat-rj45-gigabit-cg-con-f6sl/pd/D3VD3DMBM/?ref=fam#CAT6-Ecranat-%22Snap-in%22) | |
| Keystone USB | 2 | 2 | Yes | 100 | [eMAG](https://www.emag.ro/mufa-digitus-usb-2-0-negru-dn-93402/pd/DM6PVGMBM/?ref=history-shopping_414583148_106944_1) | |
| Black Beam 15x15x1000mm | 9 | 9 | No | 435 | [MakerBeam](https://www.makerbeam.com/1000mm-1p-black-makerbeamxl-15mmx15mm.html) | Frame gantry/bed/rear-brace/xdir - 8x350mm <br /> Frame Y-Dir - 4x260mm <br /> Frame Z-Dir - 4x450mm <br /> Gantry fix small Y dir - 2x160mm <br /> Frame bed - 1x160mm <br /> Gantry moving Y dir - 2x250mm <br /> | 
| Beam cuts | 26 | 26 | No | 435 | [MakerBeam](https://www.makerbeam.com/t-slot-nuts-for-makerbeamxl-50p.html) | 1m x 4: (350+350+260) x4 -> 12 cuts <br /> 1m: (450+450) x2 -> 4 cuts <br />  1m: (250+160+160+160) x1 -> 4 cuts <br /> (260+260+rest) x2 -> 6 cuts | 
| T-Slot Nuts | 100 | 2 x (50-pack) | No | 175 | [MakerBeam](https://www.makerbeam.com/t-slot-nuts-for-makerbeamxl-50p.html) | The shipping cost of the order from MakerBeam is 150 RON |
| 2510 Axial fan | 3 | 3 | No | 108 | [DigiKey](https://www.digikey.ro/en/products/detail/delta-electronics/ASB02505SHA-AY6B/7491489) | The shipping cost is 90 RON | 
| 4010 Blower fan | 4 | 4 | No | 153 | [meltbro](https://meltbro.de/1x-12v-24v-dc-40x40x10mm-radial-luefter-doppelt-gelagerter-404010-fan-ender-3-5.html) | The shipping cost is 12 RON |
| Z steppers | 3 | 3 | No | 380 | [3DO](https://3do.dk/en/motors/1170-nema17-42sth48-2504ac.html) | 
| AB steppers | 4 | 4 | No | 568 | [3DO](https://3do.dk/en/motors/1170-nema17-42sth48-2504ac.html) | The shipping cost is 120 RON | |
| M2 nut | 50 | 100 | Yes | 21 | [SAM](https://www.screwsandmore.de/100-stueck-sechskantmuttern-din-934-a2-m2/93422-435) | |
| M3 nut | 300 | 300 | Yes | 63 | [SAM](https://www.screwsandmore.de/100-stueck-sechskantmuttern-din-934-a2-m3/93423-441) | |
| M2x4 SHCS | 50 | 100 | Yes | 35 | [SAM](https://www.screwsandmore.de/100-stueck-zylinderkopfschrauben-din-912-a2-m2x4/912224-87) | |
| M2x6 SHCS | 100 | 100 | Yes | 35 | [SAM](https://www.screwsandmore.de/100-stueck-zylinderkopfschrauben-din-912-a2-m2x6/912226-91) | |
| M2x8 SHCS | 50 | 100 | Yes | 35 | [SAM](https://www.screwsandmore.de/100-stueck-zylinderkopfschrauben-din-912-a2-m2x8/912228-93) | |
| M2x6 FHCS | 50 | 50 | Yes | 44 | [SAM](https://www.screwsandmore.de/50-stueck-senkkopfschrauben-din-7991-a2-m2x6/7991226-196) | |
| M2x6 BHCS | 50 | 50 | Yes | 61 | [SAM](https://www.screwsandmore.de/50-stueck-linsenkopfschrauben-iso-7380-a2-m2x6/7380226-281) | |
| M2x8 BHCS | 50 | 50 | Yes | 61 | [SAM](https://www.screwsandmore.de/50-stueck-linsenkopfschrauben-iso-7380-a2-m2x8/7380228-284) | |
| M2x10 Self-Tap | 50 | 50 | Yes | 18 | [SAM](https://www.screwsandmore.de/50-stueck-blechschrauben-linsenkopf-din-7981-a2-2-2x9-5-torx/798122295tx) | |
| M3x6 FHCS | 50 | 50 | Yes | 21 | [SAM](https://www.screwsandmore.de/50-stueck-senkkopfschrauben-din-7991-a2-m3x6/7991236-214) | |
| M3x8 FHCS | 50 | 50 | Yes | 21 | [SAM](https://www.screwsandmore.de/50-stueck-senkkopfschrauben-din-7991-a2-m3x8/7991238-217) | |
| M3x6 BHCS | 100 | 100 | Yes | 35 | [SAM](https://www.screwsandmore.de/100-stueck-linsenkopfschrauben-iso-7380-a2-m3x6/7380236-303) | |
| M3x8 BHCS | 50 | 50 | Yes | 21 | [SAM](https://www.screwsandmore.de/50-stueck-linsenkopfschrauben-iso-7380-a2-m3x8/7380238-305) | |
| M3x10 BHCS | 50 | 50 | Yes | 21 | [SAM](https://www.screwsandmore.de/50-stueck-linsenkopfschrauben-iso-7380-a2-m3x10/73802310-308) | |
| M3x12 BHCS | 50 | 50 | Yes | 21 | [SAM](https://www.screwsandmore.de/50-stueck-linsenkopfschrauben-iso-7380-a2-m3x12/73802312-310) | |
| M3x16 BHCS | 50 | 50 | Yes | 21 | [SAM](https://www.screwsandmore.de/50-stueck-linsenkopfschrauben-iso-7380-a2-m3x16/73802316-314) | |
| M3x25 BHCS | 25 | 50 | Yes | 24 | [SAM](https://www.screwsandmore.de/50-stueck-linsenkopfschrauben-iso-7380-a2-m3x25/73802325) | |
| M3x30 BHCS | 25 | 25 | Yes | 18 | [SAM](https://www.screwsandmore.de/25-stueck-linsenkopfschrauben-iso-7380-a2-m3x30/73802330-321) | |
| M3x35 BHCS | 25 | 25 | Yes | 21 | [SAM](https://www.screwsandmore.de/25-stueck-linsenkopfschrauben-iso-7380-a2-m3x35/73802335) | |
| M3x40 BHCS | 25 | 25 | Yes | 28 | [SAM](https://www.screwsandmore.de/25-stueck-linsenkopfschrauben-iso-7380-a2-m3x40/73802340) | |
| Washer 3x6x0.5 | 100 | 100 | Yes | 14 | [SAM](https://www.screwsandmore.de/100-stueck-unterlegscheiben-din-125-a2-3-2/125232-985) | |
| **TOTAL** |  |  |  | **6888** |  | This price includes shipping costs. |

# Expansiune viitoare

# New Frame

Vertical beams: 4x 450mm
Horizontal long beams: 7x 350mm
Horizontal short beams: 4x 260mm
Gantry short beams: 2x 158mm
Gantry center beams: 2x 248mm
Bottom short beams: 2x 250mm

2m 450+450+260+260+250+250
2m 450+450+260+260+248+248
2m 350+350+350+350+350+158
1m 350+350+158

we already have 4x450 and 8x 350, therefore new cutting scheme will be:
2m 260+260+260+260+158+158+248+248
1m 250+250+400 (400 is extra for future expansion)



### Adaugam un sistem de schimbare de filament pe unul din extrudere

Ne permite sa avem avantajele unui sistem dual-carriage (viteza, consistenta in timpul printului) cu "biblioteca" de materiale ce se pot pune pe un schimbator cu 8 canale.

Cel mai potrivit pentru imprimantele din familia Voron este [ERCFv2](https://github.com/Enraged-Rabbit-Community/ERCF_v2). 
Exista suport de software pentru a pune schimbatorul de filament pe un singur extruder, lasandu-l pe celalat nealterat. 

Ansamblul de hotend permite montarea unui taietor exact inaintea hotend-ului. [Fisiere de printare](https://github.com/chirpy2605/voron/tree/main/V0/Dragon_Burner_Cutter).

Vor fi necesare cateva profile de aluminiu [1515](https://www.makerbeam.com/1000mm-1p-black-makerbeamxl-15mmx15mm.html) pentru montare.

| Componenta  | Cantitate | Link | Comentarii |
| ----------  | ---------:| ---- | ---------- |
| Profil 1515 | 4         | [Makerbeam](https://www.makerbeam.com/1000mm-1p-black-makerbeamxl-15mmx15mm.html) | |
| Kit ERCFv2  | 1         | [Meltbro](https://meltbro.de/Siboor-ERCF-Carrot-Feeder-V2-komplettes-Kit-incl--LEDs-Cutter-CNC-gears-pre-crimped-lizensiert-zertifiziert-metall-servo-mmu-voron-2-4-trident-klipper-open-source.html) | Optiunea "Keine ABS Teile" |

### Incinta inchisa

Este util sa avem incinta inchisa ca sa evitam degajarea stirenului in atelier. Nu este un pericol de sanatate, dar are un miros neplacut. 

Panourile potrivite au urmatoarele dimensiuni:

2x 282 mm x 443 mm	(grosime 3mm transparent)
1x 362 mm x 282 mm	(grosime 3mm transparent)
2x 362 mm x 432 mm	(grosime 3mm transparent)
1x 359 mm x 269 mm  (3mm negru/opac cu taieri - fisier DXF [aici](https://github.com/zruncho3d/DuelingZero/blob/main/DXFs/baseplate.dxf))

### Ecran pe retea

Piesele pentru ecranul pe retea sunt:
 * [Ecran](https://www.emag.ro/display-ips-waveshare-10-1-inch-800x1280-touch-capacitiv-interfata-dsi-compatibil-raspberry-pi-sticla-temperata-10-8-mm-10-1-dsi-touch-awaveshare30052/pd/D4HRQN3BM/)
 * [Raspberry pi 5](https://www.emag.ro/placa-de-baza-raspberry-pi-5-4-gb-multicolor-rpi5-4gb-single/pd/DD298KYBM/)
 * [PoE Hat](https://www.emag.ro/modul-raspberry-pi-poe-hat-g-40-pini-gpio-5v-5a-56-5-64-98-mm-compatible-cu-ieee-802-3af-at-ao2/pd/DQ2SR1YBM/)
 
 
## References
 
| Board | Pinout |
| --- | --- | 
| Octopus V1.1 | ![refs-octopus-pinout-functional.png](/refs-octopus-pinout-functional.png) <br> ![refs-octopus-pinout.png](/refs-octopus-pinout.png) | 
| EBB36 CAN | ![refs-ebb36-pinout.png](/refs-ebb36-pinout.png) | 
| SB2209 CAN | ![refs-sb2209-pinout.png](/refs-sb2209-pinout.png) | 
