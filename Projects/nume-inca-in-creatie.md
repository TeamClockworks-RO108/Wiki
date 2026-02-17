---
title: Therion metal plating
description: a Project meant for 3d printer augmentation using a modified printing head meant for metal deposition on plastic substrate (a voron augmentation initiative).
published: true
date: 2026-02-17T17:48:57.957Z
tags: 3dprinting, davidcore, voron, research, electroplating
editor: markdown
dateCreated: 2026-01-31T10:04:25.526Z
---

# Introduction

  The last decade has seen a dramatic increase in plasma related research. Currently, it's one of the most studied, if not the most studied field in physics. With extensive academic research carried over the last years and wildly available study materials on the subject, there are a couple reasons why plasma has peaked in interest. 

-   ***first,*** most manufacturing processes carried today in the PCB manufacturing industry are plasma based, with total market price of about 70-73 billion USD in 2024, projected to reach 100 billion by 2032.
-   ***second,*** fusion related research has peaked in the last couple decades, requirin extensive plasma research and innovation for further design considerations. It is projected that once fusion reactors are developed and enter the market, they will dominate any other alternative energy reactors. Plasma will also become a critical component of future space explorations project, our civilization needing plasma research to grow and evolve
-   ***third,*** and most important, it's estimated that **more than 99% of matter in our universe is made of plasma, our planet being one of the few places where plasma doesn't occur naturally.**

  The project follows a modification of a process used in pcb manufacturing industry, called plasma sputtering. This process is used in vacuum sealed chambers, and allows for efficient ionization of noble gases at minimum energy usage. There is another industrial process, used in atmospheric pressure environments, called plasma jet systems. This process uses atmospheric plasma to vaporize metal targets in small, microscopic molten droplets that are thereafter deposited on a substrate. We propose a 3d printing augmentation that allows for a toolchanger implemented on a voron 2.4 printer to switch between a normal printer head to a metal printing plasma toolhead. This toolhead allows for metal trace printing, allowing for multi layer PCB manufacturing in-home. It also allows for the manufacturing of plastic parts with metal traces inside, with multi layers levels, cutting the need for cables in most places. As cable connection failures represent most causes of failure in robotics projects, it enhances reliability. For hobbyists, and also any other prototyping and research purposes, it will represent a heaven project, allowing for fast, precise pcb manufacturing.

## Problems Therion solves

1.  Desktop multilayer PCB manufacturing is available at the press of a button.
2.  Printed traces inside the plastic piece cuts the need for cables in most places, improving on reliability.
3.  Metal plating allows for shielding plastic pieces against EMF radiation.
4.  decorative metal plating
5.  possible minor optic modification of lenses using partial-mirror plastic lenses.
6.  easier prototyping, eliminating 3rd party PCB manufacturing altogether

### Fast introduction in plasma physics

![](/537834_post16maxwellbolzmanncurvesresources_7pptslide9_810995.png)

maxwellian distribution (following a “normal distribution” of electron thermal energies)

 First, it is important to remember a basic chemistry lesson that each of us learns during school. Most atomic elements are ions, either negative or positive ions. These elements search for other “complements” in nature so that they can form atomic compounds, reaching neutrality. Thus, by using high energy electrons, it is possible to sever these bonds, obtaining a ion. Having high percentages of ions in an atomic gas can eventually bring about the creation of a plasma.

electrons are knocked off orbit in processes of dissociation, excitation and dissociative ionization. Generally, when a high energy electron hits a molecule's electron, kinetic energy is transferred, exciting the electron

![Scintillation and ionization in argon. | Download Scientific Diagram](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTcSPdvnts83-zQjT5D4aXWaWu6pFpk1AvpeA&s)

diagram showing the steps in the ionization of an argon atom. From left to right: The last step from the bottom right corner shows the case in which a plasma ion recombines with a free electron, achieving yet again neutrality.

It is also important for our purposes to mention that plasma free electrons generally follow a gaussian like distribution, called maxwellian distribution.

 and thus bringing it into a higher energy state. Then, if the electron that hit the molecule is hot enough, the molecule's electron will continue to migrate away from the nucleus, causing dissociation and, eventually, dissociative ionization (the molecule will become a positive ion - x^+^); ionization reaction of argon could be written as

        Ar(g) + e^\-^ → Ar^+^(g) + 2e^\-^

or, if the electron is energetic enough, it can remove more electrons

   Ar(g) + e^\-^ → Ar^2+^(g) + 3e^\-^  

Not every ionic gas or fluid is considered a plasma. There are a few criterions that need to be fulfilled in order for a gas to be considered a plasma. These criterions are: 

-   “A plasma is a quasineutral gas of charged and neutral particles which exhibits collective behavior”, a short explanation taken from “Introduction To Plasma Physics”, by F. Chen, reveals that

> Consider the forces acting on a molecule of, say, ordinary air. Since the molecule is neutral, there is no net electromagnetic force on it, and the force of gravity is negligible. The molecule moves undisturbed until it makes a collision with another molecule, and these collisions control the particle’s motion. A macroscopic force applied to a neutral gas, such ass2q from a loudspeaker generating sound waves, is transmitted to the individual atoms by collisions. The situation is totally different in a plasma, which has charged particles. As these charges move around, they can generate local concentrations of positive or negative charge, which give rise to electric fields. Motion of charges also generates currents, and hence magnetic fields. These fields affect the motion of other charged particles far away.

         It is exactly these forces that the ions inside a plasma to move simultaneously with the electrons inside. These particles exert forces of          attraction on eachother, giving them the ability to shield potential changes or local concentrations of charges because of these very                movements and forces. Therefore giving ni = ne = n (where n stands for ni-ion density ne-electron density and n is the number                          representing these densities.

-   Another criterion is that the total number of collisions between plasma particles is low enough so that the recombination rate of ions and electrons stays low. If electrons knock with positive ions, the electron will get absorbed by the ion, becoming a neutral particle once again. This is not a wanted effect, as the energy required to maintain a plasma increases exponentially with pressure. Also, plasma motion should be  mostly dominated by electrostatic forces, not usual hydrodynamic mechanics, given the high collision rate of high pressure systems.

   Plasma electrons and ions generally have very high thermal energies, in the tens of thousands of K. For this reason, plasma particles generally have low mass but high energy density, meaning that they can easily excite and vaporize surface atoms. 

Most common sputtering gases are noble gases, helium for specialized applications, argon for most applications and xenon for most high-end applications. For our application, argon will be used. 

Other non-noble gases can also be used for plasma etching, an industrial application in which material is removed from a substrate using specific chemical reactions between plasma and the substrate, creating volatile compounds which then evaporate.

The ionization energy-the minimum energy required to remove the most loosely bound electron (valence electron) from an isolated, gaseous atom or ion-also differs with each element. This energy is inversely proportional to the number of electrons in the electron shell.

|     |     |     |
| --- | --- | --- |
| Noble gas | atomic number(Z) | ionization energy(eV) |
| Helium(He) | 2   | 24.6 |
| Neon(Ne) | 10  | 21.6 |
| Argon(Ar) | 18  | 15.8 |
| Kripton(Kr) | 36  | 14.0 |
| Xenon(Xe) | 54  | 12.1 |
| Radon(Rn) | 86  | 10.7 |

## The main manufacturing processes used for metal film deposition

  The main processes are plasma ion sputtering (vacuum) and plasma jet evaporation (for atmospheric plasmas).

1.  Plasma sputtering - used widely in lens production and metal film deposition, it is used for quality film production and can be scaled down to accommodate a 2.4 voron printing chamber. The concept it's quite simple: a magnetron accelerates electrons, producing plasma ions inside a vacuum sealed chamber. The plasma gas is usually argon. A strong permanent magnet positioned on top of the magnetron has the purpose of confining the electrons, and therefore (because of the quasineutral nature of the plasma) the ions in a small volume in the proximity of the metal target. The target represents the metal wafer that will be plated on top of the substrate. The ions, being accelerated near the target knock metal atoms for the crystal lattice of the metal. These atoms are hence ballistically launched radially in all directions, coating the substrate with a dense metal layer. This layer is a quality film layer, its porosity being low. a couple downsides will be the necessity
2.  plasma jet (thermal evaporation) - used at higher pressures, typically in open atmosphere or at fractions of one atm. It uses energetic ions to rapidly excite and vaporize surface atom layers, launching molten metal droplets on the adjoining substrate. This method yields high deposition speeds, the major drawback being represented by the increased porosity cause by large droplets rapidly cooling on the substrate, the conductivity, therefore can be poor if the method is not applied correctly. For increased film quality, smaller evaporation rates have to be used.

# Therion-concept

  Therion will incorporate one of the methods presented above - either thermal evaporation or plasma sputtering. We will now explore each concept and how they would affect the design.

## Pros and cons - design considerations

First, we need to establish in what way the project design differs based on the concept we'll incorporate henceforth. The main difference is represented by the pressure inside the printing chamber. 

### Plasma sputtering

If plasma sputtering is to be used, the pressure inside needs to stay really low, a maximum of about 5p (0.005% of atmospheric pressure). This would require the chamber to be vacuum sealed, completely isolated from the outside. The film quality would then be much higher, requiring a vacuum pump to be tied to the chamber for air removal. The next step would require argon to be pumped inside the inner ionization chamber (inside the toolhead), creating plasma and allowing for the sputtering process to begin. Careful manufacturing of such a chamber would not be easy for several reasons which will later be discussed, but it has been done before and it is possible. A few problems arising from vacuum sealing the chamber would be (amongst others): motors would have to be cooled with liquid, through teflon tubes (resistant to high vacuum), vacuum grade grease would replace any other lubricant used for bearings, filament will have to be stored in a chamber adjacent to the printing chamber, rerouting the vacuum pump input to it so as to keep the filament dry and eliminate any bubbles from the filament. This way, outgassing will be kept at a minimum. The deposition rate is fairly slow, ranging from 0.1 nm/min up to several hundred nm/min.

### Thermal evaporation

If thermal evaporation will be incorporated instead, the pressure inside the chamber can be kept as high as normal atmospheric, but it would best be recommended to keep the pressure a bit lower than normal, about 20.000-30.000pa for higher trace quality. Vacuum grease would not be required, fans would replace water cooling of the stepper motors. Higher vacuum would also dramatically help lower the metal target's melting  point (because of lower pressure), thus increasing power efficiency. depositions rates are also much higher (tens of nm/min up to um/min). A downside would be the fact that thermal evaporation in atmospheric plasmas yields lower film quality, metal droplets that plate the plastic substrate giving rise to high porosity in traces.

![](/gold_silver_copper_pressure_melting_temperatures.png)

pressure vs melting temperature graph; the melting temperature drastically increases with higher temperature

 Quality can be increased by managing deposition rates (lowering them), thus increasing uniformity. This tradeoff between speed vs quality is worth it, given that even at slower rates the deposition is still much faster than it would be in sputtering systems.

 Also, the melting temperature3 of a metal is proportional to the the preswsure inside the chamber, decreasing dramatically. Hernce, lower pressure would enable thermal evaporation at a higher energy efficency, compared to atmospheric evaporation. Moreover, a larger range of deposition speeds can be achieved and maintained.

The optimal design incorporats best of both methods, enabling both partial thermal evaporation and sputtering capabilities at lower than normal chamber pressure.

## Design schematic

The design is fairly similar to that of a plasma jet barrel.

![](/therion-schita+legenda.jpg)

Profile view of the design schematic-plasma jet barrel used as a toolhead for metal plating

![](/therion-schita-zone_de_interes.jpg)

Main five areas of the toolhead; a-Ar outlet(maintains and modulates a constant Argon inflow); b-Electron depletion zone(the area where electrons are accelerated, ionizing the Ar atoms); c-Plasma confinement zone(the area where plasma is concentrated and partly confined, allowing for surface vaporization and sputtering of the metal target); d-Ion barrel(a tube through which sputtered metal ions are focused-andx ooled down-in a straight beam, being kept on orbit by the strong side electromagnets and enabling consistent deposition); e-Deposition zone (the area under the barrel where metal is deposited on the plastic substrate)