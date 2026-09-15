---
title: BOB linear stepper system
description: A linear closed loop stepper system used as XY motion system on a 3D printer
published: true
date: 2026-09-15T17:13:24.498Z
tags: 
editor: markdown
dateCreated: 2026-05-28T11:35:58.532Z
---

> Documentation is not complete and needs to go through further revision after testing
{.is-warning}

# Description

BOB (binary operated bridge) linear closed loop stepper motion system is an augmentation brought to the [Therion](https://wiki.teamclockworks.ro/en/Projects/therion) metal plating project. It consists of a hybrid linear stepper system consisting of an electromagnetically actuated motion system, converting electric energy directly into linear motion. Thus, rotary to linear motion conversion is unnecessary, such as belt systems or screw shafts.

## Project ethos

The BOB linear stepper project was created to aid the aforementioned Therion project, an experimental additive manufacturing printer, implementing experimental motion systems (amongst others) with the purpose of improving quality, performance and user experience as well as cost, based on each printers requirements, a core value best represented by the belief that a system should best fit its purpose and user - not its designer and industrial "get a  quote" limitations.

Thus, this project aims to offer an open source close alternative to industry standard linear stepper systems, offering continuous updates which aim to improve performance and reduce cost. The project can also aid other open source projects (such as [Voron](https://vorondesign.com/)) in building experimental printers (and new "proto" [printers](https://docs.cartographer3d.com/linear-motor/coming-soon)).

> 100% made by humans
{.is-info}


## Advantages

- High speed motion system
- Higher overall power efficiency compared to classic motion systems
- Vacuum compatibility
- Friction is reduced
- Lubricating the system is optional, but not essential (based on the project design)
- higher achievable precision (for CNC systems, 3D printers or high precision machines)
- significant reduction of VFAs (Vertical Fine Artifacts) in 3D prints, caused by finite belt tooth pitch

# Technical description 
The linear closed-loop stepper acts as a 3-phase synchronous motor, rolled over a flat, straight magnet "tooth" rail, using command pulses to precisely control positional precision of a 3 electromagnet carriage, which implements a form of magnetic (and potentially optical) incremental encoder control system, composed of one linear magnetic/optical strip, and one readout head mounted on the carriage.

Compared to a classic stepper motion system, linear steppers have tooth pitches ranging from couple mm to over 10mm. a tradeoff between cost, magnet type, total magnet holding force as well as aspect rati and area/volume have to all be considered when selecting the type of magnet tooth used. Neodymium magnets have high holding force compared to their volume and mass, as well as  high commercial availability (even strong N52 types). On the other hand, they are mechanically brittle, can be expensive and they lose their holding force rapidly, experiencing maximum force at around 0C (273,15K), and dropping at a minimum around 80C (353,15K). Heat resistant types exist, but are harder to find. We found the best option for our application to be an N52 Neodymium magnet, with 10x20mm surface and 2-5mm thickness. They have a holding force ranging from 2-to 5kg per magnet.

Following the inverse cube law applied to magnetic fields (B ∝ 1/d^3 ; where d - distance and B - magnetic field), we conclude that the distance between the carriage electromagnets and the platen has to be kept at a minimum (within about 1mm or less) so that torque is maintained high enough. Carriage structural rigidity needs to be maintained in order to prevent buckling caused by the attraction between the electromagnets and the permanent magnets as well as stalling (friction between the electromagnet core and the platen).

Each electromagnet tooth pitchb is approximately equal to its twin platen magnet teeth. A slight offset is applied for the spacing of the electromagnet teeth, assuring that one magnet is always perfectly aligned to one platen magnet (corresponding to one full step), while the other two teeth are both either left hand biased (closer to the platen tooth to its left) or right hand biased (closer to the platen tooth to its right). Thus, by alternating the control signal in each electromagnet, motion is achieved. Each signal is offset by about 120 electrical degrees from eachother, making for high efficiency. Field oriented control (FOC) will be used to ensure proper control of the positional accuracy, as well as speed and torque of the stepper at all times.

![linearmotorprinzip.png](/Projects/linearmotorprinzip.png)

Two types of encoders will be tested, both optical and magnetic, and compared in different conditions and levels of dust, use, speeds, light, precision etc. Thus, quality will be compared against total cost and the best system will be selected and integrated. The two chips will be [AS5304B TSSOP20 LF T&RDP](https://www.digikey.at/en/products/detail/ams-osram-usa-inc/AS5304B-TSSOP20-LF-T-RDP/18769154) (magnetic) and a variant of the [AEDR-8300-1W2](https://ro.farnell.com/broadcom/aedr-8300-1w2/photointerrupter-reflective/dp/1735258) (optical). Different strips will also be tested.

For the prototype, self-lubricating [IGLIDUR polymer linear bushing](https://www.igus.eu/plain-bearing) inserts will be used, thanks to their low maintanance requirements, high chemical resistance, optimal lubrication in all kinds of environments as well as cost and availability. These inserts will also be tested for future use in different systems and projects. In the future, custom teflon linear bearings compatible with the 2020/3030/4040 V-slot aluminum extrusions  might be implemented for use in 3D printers and other systems.

The magnetic core which will offer support for the three electromagnets will be one solid "M" shaped silicon steel (also known as electrical steel) laminated core, made out of multiple thin sheet laminations, joined via screws and electrically isolated from eachother using thin insulator (kapton or electrical paper). The laminations run parallel to the magnetic field, ensuring a continuous magnetic field with little to no variations in its magnetic reluctance path. Laminated cores ensure high power efficiency and lower coefficient of core heating per watt of used power. Electrical steel also has high magnetic permeability and low [remanent magnetization](https://www.electronics-tutorials.ws/electromagnetism/magnetic-hysteresis.html) (gold standard of both transformers and stepper cores).

## Coil winding machine


## Additional sources

- https://www.researchgate.net/figure/The-three-phase-modular-hybrid-linear-stepper-motor_fig1_242444457

- https://www.youtube.com/watch?v=TPCgbfWZ6IQ

- https://www.youtube.com/shorts/E_I5j0IrIio

- https://wiki.teamclockworks.ro/en/Projects/therion

- https://www.youtube.com/watch?v=fc7UEUkDd_o

# Parts list & sourcing
| Category | Part | Quantity | Notes | Distributor | Cost | Total cost |
| -- | -- | -- | -- |
|Stepper prototype| rail magnet teeth | 30 |Magnet Neodim bloc 20x10x5 mm N52; Forță de aderență: 4.90kg ; Temperatură maximă de utilizare: 60C | NeoMagnet(RO) - https://neomagnet.ro/Magnet-Neodim-bloc-20x10x5-mm-N52 | 419,66RON | ~~~ |
|^^|carriage compression springs|8|Arc de compresie 1,2 mm - 20 mm|ardushop(RO) - https://ardushop.ro/ro/componente/1988-arc-compresie-12mm-20mm-6427854030238.html|^^|^^|
|^^|creality test compression spring| 1| Arc compresie Creality D8xL22 1.1mm| Ardushop(RO)- https://ardushop.ro/ro/creality/1237-arc-compresie-creality-d8xl22-11mm-6427854017772.html|^^|^^|
|^^|precision guide shaft| 2 | Axa de precizie rectificata si calita de 16mm| cnc shop(RO) - https://cnc-shop.ro/index.php?route=product/product&path=59&product_id=60 | ^^ | ^^|
|^^|kapton tape| 1 | Bandă adezivă termorezistentă tip Kapton, 10 mm x 33 m | Ardushop(RO) - https://ardushop.ro/ro/componente/1178-banda-kapton-25m-10mm-6427854016713.html| ^^ |^^|
|^^| IGLIDUR polymer linear bearing| 2 | JUMO-01-16 - Insert; iglidur® J; Ø: 16mm; L: 35mm; DryLin® W | TME(EU) - https://www.tme.eu/ro/details/jumo-01-16/ghidaje-liniare/igus/ | ^^|^^|
|^^| aluminum 3030 V-slot extrusion| 1| Profil din aluminiu 30x30 negru - 300mm | DROT.RO - https://www.drot.ro/platforma-arduino/230749-profil-din-aluminiu-30x30-negru-300mm.html|^^|^^|
| Coil winding machine |

| Encoder test rig |

# Timeline

- CAD for a first prototype exists

- Trebuie cumparate componentem si mers la firme luna asta, ideal pana la final de septembrie se vrea sa fie gasita finantare (DAVID SI CALIN).

- COIL WINDING MACHINE trebuie terminat de Calin saptamana 13-20 SEP.

- Trebuie facut CAD ul pentru un test RIG ce sa testeze encoderele liniare, sistemul de detectie si codul (Calin face CAD ul, David electronica si design de pcb + teste de ambii)

- Trebuie gasit om pe marketing care sa se ocupe constant atat de rescrierea documentatiei intr un mod profi, cat si redactare si scriere de cereri si emails pentru sponsori, plus promotionale logo sau orice se va mai face in viitor (pana la FINAL DE SAPTAMANA 13-20 SEP)

- DUPA 	ce se face rost de finantare, se cumpara piese si se asambleaza V! (TESTE MECANICE, strength test etc.) se va face de CALIN SI DAVID.

- SE TERMINA LISTA CU componente ce trebuie cumparate, atat pentru ENCODER TEST RIG, COIL WINDING MACHINE CAT SI PROTOTIP, se scrie intr un excel si se iau piese

- LOGO CAD trebuie facut