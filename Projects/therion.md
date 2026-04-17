---
title: Therion metal plating
description: a Project meant for 3d printer augmentation using a modified printing head meant for metal deposition on plastic substrate (a voron augmentation initiative).
published: true
date: 2026-04-17T14:23:38.263Z
tags: 
editor: markdown
dateCreated: 2026-01-31T10:04:25.526Z
---

# Introduction

## What is Therion?

Therion represents a 3d-printing augmentation project that aims for achieving thin-film deposition capabilities on a Voron 2.4 printer, enabling at-home prototyping and quality manufacturing of complex custom-3D-printed multilayer PCBs, or printed plastic pieces with inner metal traces or shielding for reliable electric work (as a better alternative to cable-management) or emf shielding.

> A theoretical research of a new technique of additively depositing conductive traces on 3D-printed substrates using plasma ion bombardment.

films could be virtually made of almost any polymer, metal or ceramic, using a modified plasma gun toolhead for depositing films.  A toolchanging system will be implemented, rapidly switching between traditional printing and thin-film deposition.

Therion implements a modified physical vapor deposition (PVD) technique, which we have branded: plasma-enhanced inductive physical vapor deposition. It uses induction heating for efficient excitation of surface atoms, vaporised by dense, ECR ionized gas precursor plasma for high deposition rates of dense, quality thin films.

## Problems Therion solves

1.  Desktop multilayer PCB manufacturing is available at the press of a button.
2.  Printed traces inside the plastic piece cuts the need for cables in most places, improving on reliability.
3.  Metal plating allows for shielding plastic pieces against EMF radiation.
4.  decorative metal plating
5.  possible minor optic modification of lenses using partial-mirror plastic lenses.
6.  easier prototyping, eliminating 3rd party PCB manufacturing altogether

### Fast introduction in plasma physics

![](/537834_post16maxwellbolzmanncurvesresources_7pptslide9_810995.png)

Figure1: maxwellian distribution (following a “normal distribution” of electron thermal energies)

The last decade has seen a dramatic increase in plasma related research. Currently, it's one of the most studied, if not the most studied field in physics. With extensive academic research carried over the last years and wildly available study materials on the subject, there are a couple reasons why plasma has peaked in interest.

-   ***first,*** most manufacturing processes carried today in the PCB manufacturing industry are plasma based, with total market price of about 70-73 billion USD in 2024, projected to reach 100 billion by 2032.
-   ***second,*** fusion related research has peaked in the last couple decades, requiring extensive plasma research and innovation for further design considerations. It is projected that once fusion reactors are developed and enter the market, they will dominate any other alternative energy reactors. Plasma will also become a critical component of future space explorations project, our civilization needing plasma research to grow and evolve
-   ***third,*** and most important, it's estimated that **more than 99% of matter in our universe is made of plasma, our planet being one of the few places where plasma doesn't occur naturally.**

First, it is important to remember a basic chemistry lesson that each of us learns during school. Most atomic elements are ions, either negative or positive ions. These elements search for other “complements” in nature so that they can form atomic compounds, reaching neutrality. Thus, by using high energy electrons, it is possible to sever these bonds, obtaining a ion. Having high percentages of ions in an atomic gas can eventually bring about the creation of a plasma.

electrons are knocked off orbit in processes of dissociation, excitation and dissociative ionization. Generally, when a high energy electron hits a molecule's electron, kinetic energy is transferred, exciting the electron

![Scintillation and ionization in argon. | Download Scientific Diagram](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTcSPdvnts83-zQjT5D4aXWaWu6pFpk1AvpeA&s)

Figure 2: diagram showing the steps in the ionization of an argon atom. From left to right: The last step from the bottom right corner shows the case in which a plasma ion recombines with a free electron, achieving yet again neutrality.

It is also important for our purposes to mention that plasma free electrons generally follow a gaussian like distribution, called maxwellian distribution.

and thus bringing it into a higher energy state. Then, if the electron that hit the molecule is hot enough, the molecule's electron will continue to migrate away from the nucleus, causing dissociation and, eventually, dissociative ionization (the molecule will become a positive ion - x^+^); ionization reaction of argon could be written as

     Ar(g) + e^\-^ → Ar^+^(g) + 2e^\-^

or, if the electron is energetic enough, it can remove more electrons 

    Ar(g) + e^\-^ → Ar^2+^(g) + 3e^\-^

 Not every ionic gas or fluid is considered a plasma. There are a few criterions that need to be fulfilled in order for a gas to be considered a plasma. These criterions are:

-   “A plasma is a quasineutral gas of charged and neutral particles which exhibits collective behavior”, a short explanation taken from “Introduction To Plasma Physics”, by F. Chen, reveals that

> Consider the forces acting on a molecule of, say, ordinary air. Since the molecule is neutral, there is no net electromagnetic force on it, and the force of gravity is negligible. The molecule moves undisturbed until it makes a collision with another molecule, and these collisions control the particle’s motion. A macroscopic force applied to a neutral gas, such ass2q from a loudspeaker generating sound waves, is transmitted to the individual atoms by collisions. The situation is totally different in a plasma, which has charged particles. As these charges move around, they can generate local concentrations of positive or negative charge, which give rise to electric fields. Motion of charges also generates currents, and hence magnetic fields. These fields affect the motion of other charged particles far away.

It is exactly these forces that the ions inside a plasma to move simultaneously with the electrons inside. These particles exert forces of attraction on eachother, giving them the ability to shield potential changes or local concentrations of charges because of these very movements and forces. Therefore giving ni = ne = n (where n stands for ni-ion density ne-electron density and n is the number representing these densities.

-   Another criterion is that the total number of collisions between plasma particles is low enough so that the recombination rate of ions and electrons stays low. If electrons knock with positive ions, the electron will get absorbed by the ion, becoming a neutral particle once again. This is not a wanted effect, as the energy required to maintain a plasma increases exponentially with pressure. Also, plasma motion should be  mostly dominated by electrostatic forces, not usual hydrodynamic mechanics, given the high collision rate of high pressure systems.

Plasma electrons and ions generally have very high thermal energies, in the tens of thousands of K. For this reason, plasma particles generally have low mass but high energy density, meaning that they can easily excite and vaporize surface atoms.

## The main manufacturing processes used for metal film deposition

First, as a short definition, “The formation of a condensible vapor by physical mechanisms and subsequent deposition of this material onto a substrate as a thin film or coating is referred to as physical vapor deposition (PVD) (Mahan 2000, Rossnagel 2003, Thornton 1988). The formation of a vapor refers to a phase transition of the filmforming material from a solid or liquid phase into a gaseous or plasma phase. PVD is a broad field and various processes are applied to create film-forming material and to achieve thin film deposition.” (Foundations of physical vapor deposition with plasma assistance). As it's frequently mentioned, the term vapor used here is sort of a misnomer, in comparison to vapor-gaseous state released through thermal excitation, the term refers to any subatomic gas-like conglomerate of particles that is obtained through electric-plasma/thermal excitation phenomena. 

The main processes are plasma ion sputtering (vacuum) and plasma jet evaporation (for atmospheric plasmas).

1.  Plasma sputtering - used widely in lens production and metal film deposition, it is used for quality film production and can be scaled down to accommodate a 2.4 voron printing chamber. The concept it's quite simple: a magnetron accelerates electrons, producing plasma ions inside a vacuum sealed chamber. The plasma gas is usually argon. A strong permanent magnet positioned on top of the magnetron has the purpose of confining the electrons, and therefore (because of the quasineutral nature of the plasma) the ions in a small volume in the proximity of the metal target. The target represents the metal wafer that will be plated on top of the substrate. The ions, being accelerated near the target knock metal atoms for the crystal lattice of the metal. These atoms are hence ballistically launched radially in all directions (not line-of-sight). The deposited film is a dense, quality film, its porosity being low.
2.  Plasma jet (thermal spraying) - used at higher pressures, typically in open atmosphere or at fractions of one atm. It typically implements a hollow cathode design, known for higher efficiency in high pressure systems. It uses hot plasma to excite and vaporize surface atoms from the target, plating it on the opposing substrate. This process is line-of-sight.
3.  Thermal evaporation - typically used in a vacuum, due to higher efficiency and lower corresponding melting temperature. This design typically incorporates metal filaments, warmed up beyond their melting temperature, creating a vapor cloud that deposits on the opposing substrate. This process is typically line-of-sight, unless there's additional augmentation given by vapor cloud ionization techniques.

The main difference between these methods is the degree of atomization of the plating medium, energetic processes (such as plasma sputtering in vacuum) yielding high atomization levels, vapor clouds being composed out of individually energetic, ballistically launched ion species, as well as energetic neutrals. films are effectively built block-by-block, causing high film mass density. The overall atomic structure of the bulk target is reproduced in high enthalpy plating methods (high-energy) on the substrate, while lower enthalpy processes cause higher oxidation (open atmosphere process), porosity and less atomic reproduction of the bulk. 

Higher atomization also means higher power consumption (unless open-atmosphere processes are implemented, yielding low efficiency and high poer consumption), given that the energy density of the vapor cloud increases, atoms on average have higher kinetic and potential energies. Most of the time, higher power-consumption also adds the need for a vacuum-sealed chamber where the process is carried on.

# Therion-concept

Therion will incorporate one of the methods presented above - or a combination, depending on the pressure and power level used. We will now explore each concept and how they would affect the design.

## Pros and cons - design considerations

First, we need to establish in what way the project design differs based on the concept we'll incorporate henceforth. The main difference is represented by the pressure inside the printing chamber.

### Plasma sputtering

If plasma sputtering is to be used, the pressure inside needs to stay low, about under 5pa (0.005% of atmospheric pressure). This would require the chamber to be vacuum sealed, completely isolated from the outside. 

The film quality would then be much higher, requiring a vacuum pump to be tied to the chamber for air removal. The next step would require argon to be pumped inside the inner ionization chamber (inside the toolhead), creating plasma and allowing for the sputtering process to begin. 

Careful manufacturing of such a chamber would not be easy for several reasons which will later be discussed, but it has been done before and it is possible.

A few problems arising from vacuum sealing the chamber would be (amongst others): motors would have to be cooled with liquid, through teflon tubes (resistant to high vacuum), vacuum grade grease would replace any other lubricant used for bearings, filament will have to be stored in a chamber adjacent to the printing chamber, rerouting the vacuum pump input to it so as to keep the filament dry and eliminate any bubbles from the filament.

The ionization energy-the minimum energy required to remove the most loosely bound electron (valence electron) from an isolated, gaseous atom or ion-also differs with each element. This energy is inversely proportional (in noble gases) to the number of electrons in the electron shell.

Most common sputtering gases are noble gases, helium for specialized applications, argon for most applications and xenon, used generally for high-end applications. For our application, argon will be used. Th

|     |     |     |
| --- | --- | --- |
| Noble gas | atomic number(Z) | ionization energy(eV) |
| Helium(He) | 2   | 24.6 |
| Neon(Ne) | 10  | 21.6 |
| Argon(Ar) | 18  | 15.8 |
| Kripton(Kr) | 36  | 14.0 |
| Xenon(Xe) | 54  | 12.1 |
| Radon(Rn) | 86  | 10.7 |

Other non-noble gases can also be used for plasma etching, an industrial application in which material is removed from a substrate using specific chemical reactions between plasma and the substrate, creating volatile compounds which then evaporate.

 This way, outgassing will be kept at a minimum. The deposition rate is fairly slow, ranging from 0.1 nm/min up to several hundred nm/min.

### Thermal evaporation

If [thermal evaporation](https://en.wikipedia.org/wiki/Evaporation_(deposition)) will be incorporated instead, the pressure inside the chamber has to be kept low, about 20.000-30.000pa or high vacuum for higher trace quality. Vacuum grease would not be required, unless high vacuum is implemented, fans would replace water cooling of the stepper motors. Higher vacuum would also dramatically help lower the metal target's melting  point (because of lower pressure), thus increasing power efficiency. depositions rates are also much higher (tens of nm/min up to um/min). A downside would be the fact that thermal evaporation in atmospheric plasmas yields lower film quality, combining with oxygen to form oxides. Also, the process is line-of-sight, given the lower thermal energies of the vapor atoms, yielding lower adatom mobility (surface diffusion of atoms) and thus, lower film density.

![](/gold_silver_copper_pressure_melting_temperatures.png)

Figure  3: pressure vs melting temperature graph; the melting temperature drastically increases with higher temperature

Quality can be increased by managing deposition rates (lowering them), thus increasing uniformity. This tradeoff between speed vs quality is worth it, given that even at slower rates the deposition is still much faster than it would be in sputtering systems.

Also, the melting temperature of most metals is proportional to the the pressure inside the chamber, decreasing dramatically with higher vacuum. Hence, lower pressure would enable thermal evaporation at higher energy efficiency, compared to atmospheric evaporation. 

Moreover, a larger range of deposition speeds can be achieved and maintained.

Induction heating of surface atoms, combined with hot plasma surface excitation could enable [sublimation](https://en.wikipedia.org/wiki/Sublimation_(phase_transition)) of metal atoms in our design. Controlling the power fed to the inductor and the plasma would also precisely manage the deposition rate.

Exposed structural parts inside the toolhead would have to be covered with a protection film so that deposits don't form on the surface, possibly corrosion structural elements.

This process is line-of-sight only if the chamber allows for collisionless deposition, otherwise overall atom vapor movement would be governed by basic hydrodynamic interactions. If the vapor is ionised (by say, an [ECR](https://en.wikipedia.org/wiki/Electron_cyclotron_resonance) unit-a microwave magnetron), then the thermal energy of the vapor atoms drastically increases, reaching high ionization density at efficient power consumption, especially in high-vacuum setup.

## Plasma barrel design schematic

 The design incorporates a barrel-like appearance similar to that used in atmospheric plasma jet guns. Argon or other process gases are injected through an inlet (a) into the process chamber (b) where ionization happens and plasma is concentrated via a set of magnetic mirrors formed by the magnets coaxially attached to the barrel. an ECR unit (a microwave amplifier PCB or a magnetron with near ECR characteristic frequency) of high power is placed on top of the assembly, allowing for line-of-sight operation of the magnetron antenna (microwaves are coaxially directed through the barrel tube).

|![therionv2-legenda.jpg](/therionv2-legenda.jpg)|
|Design schematic and legend|
|--|

Zone (b) is where thermal evaporation takes place. The metal-to-be deposited is placed as a ring (disk or toroid) inside a ceramic hearth between two in phase inductors placed face-to-face. The metal is heated through induction heating near its melting point, and given that in HV the boiling point is close to the melting point temperature, sublimation of surface metal atoms starts to produce. Thus, a metal atom cloud forms, which is ionised and atomized by the microwaves coming in from the ECR unit. atoms gain high temperature and kinetic energy which helps enhance the deposition process. high plasma densities can be achieved through careful design and choice of high power ECR unit. Often ionization percentages ranging between 80-90% can be achieved, drastically

|![therionv2-indicatii.jpg](/therionv2-indicatii.jpg)|
|Process path of plasma through the apparatus. Main areas: (a)->(b)->(c)->(d). Gas enters in the assembly through area (a), ionizes the metal vapor plum in (b), gets focused in (c) and exists through (d), coating the substrate|
|--|

increasing the quality of the deposited film. The in phase inductors act as one single strong inductor, interfering constructively right in the middle, where the metal disk is found. Thus, efficiency is increased and heating of the metal is achieved more effectively. The most important advantage of using two paired inductors is the ability to slide and switch the metal disk right through the “sleeve” created by the gap between the two inductors. This way, more than one metal can be plated. Stacking more pairs of inductors allows for alloy plating (the temperature within each disk being closely monitored and controlled) and lots of other applications. The metal disks will be placed on a ceramic disk hearth which will be actuated via a stepper motor, allowing for easy and precise switching between the disks.

The metal ions are then magnetically confined on one central axis ( c), forming a plasma beam which is shot through the barrel outlet (d). microwave electrons launching from the ECR antenna are also confined on one axis by the magnets found in area (a). A combination of electromagnets and permanent magnets will be used, making use of efficient power usage and simple calibration of magnetic force lines and ion trajectory. The total magnet contingent will form one continuous [magnetic mirror](https://en.wikipedia.org/wiki/Magnetic_mirror) which will trap electrons and ions inside area (b), increasing transit time and forcing ions back, thus increasing energy efficiency and plasma density.

The barrel will most likely be built out of some sort of ceramic (alumina or other material), given its high compressive strength, low mass, high melting point, chemical stability, dielectric properties (electric insulation) and low vapor pressure (very important in high-vacuum systems and UHV making use of thermal and chemical vapor deposition). the ceramic barrel will likely cover areas (a), (b) and ( c). Area (b) will most certainly be made out of some sort of ceramic tubing hearth, given that many ceramic hearths are used in thermal evaporation deposition systems (typically zirconia, alumina and sometimes refractory metals \[gudmundson\]).

## Industrial design

Similiar design principles have previously been implemented in industry, making for high plasma density at relatively medium pressure levels (around 0.1pa).

|![](/screenshot_2026-04-14_193312.png)|
|Plasma enhanced thermal deposition apparatus|
|--|

The metal target is brought close to its melting temperature, producing a metal vapor plume. The ECR unit ionizes the plume, achieving high ionization percentages (close to 100%), achiving high quality film.  Magnetic confimenet makes sure both the microwaves and the ions move parallel to the field lines, bombarding the substrate with metal ions. Increasing the ECR power feed also increases the plasma density of the plume, increasing quality and efficiency. a quartz crystal film monitor keeps track of film thickness by measuring the change of the resonating frequency of the crystal. This deposition technique has proven to be very efficient, yielding high film quality as well as high depotion rates (when compared to sputtering). Moreover, this technique has proven to be compatible with higher process pressures, ranging from 10^-2^ to 5*10^-1^ Pa.

## (A) - Argon inlet

The argon inlet is placed as a cap on the top of the barrel, containing mainly a [throttle valve](https://en.wikipedia.org/wiki/Throttle) tied to a tube through which gas is let into from an outside source. The throttle valve will likely be placed on the atmospheric side, in combination with a basic vacuum gate valve which will restrict any unwanted parasitic gas flow outside of normal operation, which can happen in some lower quality throttle valves not meant for flow restriction. Pressure through the tube will be measured, and based on the total conductance of the supply tubing and system, the flow through the tube will be calculated. Reactive gases that can be used range from Argon to Helium and nitrogen. Nitrogen can be used to create nitrates. Oxygen may also be used to create oxide films, but given the high flammability of oxygen it would be recommended to use oxide base targets instead.

some aluminum or ceramic tubing on the top cap of the barrel, together with a pair of permanent magnets will make use of directed confinement to keep gas ions and microwaves on one trajectory, without leaking microwaves through the walls. The ECR unit (likely magnetron) will be placed on top of the cap with the purpose of supplying the required microwaves.

## (B) - Plasma confinement zone

A strong pair of neodymium magnets placed on the top and bottom end of the confinement zone will increase electron and ion dwell times, achieving more efficient microwave absorption of metal vapor atoms. The ions and electrons will complete cyclotron orbits along the field lines, losing momentum near the magnets where the intensity of the field increases, thus forming a magnetic mirror in combination with the other permanent and electromagnets placed coaxially along the barrel tube. The intensity of the magnetic field passing through the electromagnets is increased, allowing for manipulation of the magnetic mirror intensity and of the loss cone.

Only energetic ions will be able to escape through the loss cone into zone (c ) (and then in zone (d) and onto the substrate), thus allowing for high adatom mobility of deposited surface atoms, filling gaps within the film and reducing porosity (therefore increasing quality).

The inductor coil is made out of hollow copper wire allowing for water to run through and cool down the inductor. High power induction heating applications create a lot of residual heat within the inductor wire which can potentially melt the wire and create hot spots because of the skin effect (explained bellow). As mentioned above, a pair of two inductors placed face-to-face will act as one inductor heating the metal target disk, the intensity of the field peaking halfway between the two inductors, where the target is places. Therefore, the metal disk can be off-centered from the center of an inductor without causing losses and heating inefficiencies of the metal. 

The geometry of area (b) will be similar to a cross, plasma extending and covering the zone where the target is placed so that a bigger plasma cloud can form, covering more of the target's surface.

It is important to mention that there will be up to three individual ceramic heath branches (a branch represents one ceramic heath on which targets have been placed) between which the user can choose and switch, via the stepper motor placed on the back of the barrel.

### Inductor coil

 The inductor coil is used in this design for precise surface heating of the metal target used. Thanks to the [skin effect](https://en.wikipedia.org/wiki/Skin_effect), most of the current induced inside the target is focused in a narrow volume, close to the surface of the conductor.

![Skin effect - Wikipedia](https://upload.wikimedia.org/wikipedia/commons/thumb/c/c7/Skineffect_reason.svg/250px-Skineffect_reason.svg.png)

Figure 6: diagram showing the fields induced inside a metal conductor through which AC current is circulating (image from [Skin effect](https://en.wikipedia.org/wiki/Skin_effect) - Wikipedia)

 This effect is caused by the inability of currents and magnetic fields close to the outside of the metal to shield it from the induced current. 

In the center, where the opposing fields are strongest, the current reduces close to zero. Therefore, it is easy to precisely control the degree of heating and evaporation of the outside metal layer, given that the skin depth is proportional to frequency-higher frequency creates shallower skin depths, raising the resistance of the skin layer which in turn raises the temperature(this effect is AC specific). Bringing the surface metal atoms close to melting temperature also increases the mobility of these atoms, freeing themselves from the crystalline lattice they occupy and allowing for easier vapor formation (either by plasma or by sputtering). 

In this specific design, induction heating could also enable easier alloying of metals by precisely controlling the vapor formation and pressure of the metals being used. It could also allow for individual deposition of the metal targets. Once surface atoms reach about 90% of melting temperature, energetic plasma ions will further transfer their high kinetic energy to these atoms, vaporizing or sputtering them-depending on the pressure used inside the chamber.

 Given the high energy density of plasma, but low mass, only surface level heating is achieved, further managing deposition rates.

![File:Example of skin effect in circular wire.png - Wikimedia Commons](https://upload.wikimedia.org/wikipedia/commons/4/42/Example_of_skin_effect_in_circular_wire.png)

Figure 7: thermal energy transition in AC coupled metal showing the effect of the skin effect in induction heating. 20kHz vs 81KHz (image [from](https://commons.wikimedia.org/wiki/File:Example_of_skin_effect_in_circular_wire.png))

For efficient heating of the metal element, the distance between the target and the inductor would have to be fairly small, around couple mm. Thermal dilatation would also have to be considered. Moreover, the shape of the target would best allow field lines to sit perpendicular to the surface of the metal, for high efficiency. 

Hollow, water cooled inductors would be best, minimizing coil overheating, but other conductive cooling methods that don't require hollow conductors can be implemented. Efficiency would also depend on the electric resistance of the target, Higher resistance yielding better results. It's essential that the temperature of the bulk metal doesn't reach melting point, preventing structural deformation. 

Also, induction heating would only work for metal targets, ceramics or polymers would have to be exclusively sputtered on the substrate surface.

A strong permanent magnet placed under the target and the inductor will purposely concentrate and confine plasma near the target, enabling fast removal of surface atoms from the crystal lattice. 

The surface heating resulted from the skin effect combined with hot electrons and ions colliding with the metal evaporates and sputters metal atoms towards area ( c), onto the substrate. Thus, deposition is achieved through mainly evaporation deposition, but also sputtering.

As mentioned above, future barrels can implement one of two designs - 1. one pair of inductors for depositing metal individually (pros: simple, clean deposition of metal; cons: no alloy deposition) or 2. multi-pair inductor branches which can switch between branches containing up to three individual metal targets which can be closely temperature controlled to achieve precise alloy deposition (pairs such as copper, iron and nickel).

### Managing deposition rates and target temperature

For the purpose of the project, it is vital for the deposition rate of metal to be controlled and managed. Evaporation rate of metal surface atoms is largely exponentially dependent on surface temperature, staying close to 0 at temperatures bellow the boiling point and drastically increasing at temperatures near or over this threshold. Careful, controlled deposition allows for the design of intricate PCBs, either HF, RF or power circuits. In order to achieve this, the width and thickness of the deposited film has to be controlled. The use of empiric methods, mathematical models as well as precise measurement instruments can all help achieve this.

For temperature measurement, an industrial IR precision sensor, with a maximum range between 1000-1500 degrees Celsius would be optimal. Close, indirect measurement can thus be achieved without the risk of damaging the sensor, which will likely be placed on the outer shell of the barrel, where the metal target lays uncovered inside the ceramic heath. The instrument will be mounted on an aluminum frame surrounding the barrel, which helps both structural integrity, as well as for sensor mounting.

Given that convection is limited in vacuum, cooling of the target would be achieved mainly through the ceramic heath, which (if made out of thermally conductive ceramic) can be water cooled to keep the temperature in check, or to change the evaporation rate of the target. 

A PID algorithm modified for vacuum conditions will likely be used for controlling the power feed to the inductor, making sure the temperature of the metal doesn't raise drastically over the target temperature. Careful temperature control has to be implemented in order to keep trace quality in check - uneven metal distribution over the length of the trace can lead to hot spots during use which can damage the PCB and increase electrical resistance (lower trace quality) or it can lead to problematic signal reflections in RF circuits (unmatched impedance). 

## Electrical feedthroughs

Ideally, electric feedthroughs should be leak-free, with no micro-leaks created where the copper pins have been pressed into the ceramic/plastic isolation. FR4 circuit boards have high outgassing rates because of the binding resin that they're made of, so they cannot be use \]d as a medium between vacuum and atmosphere. microscopic leaks can be managed and outpowered by the pump, provided the leaks are small and long enough to reduce conductivity and resist the pressure difference. A thick, aluminum CNC panel will be used as a back wall for the chamber, providing the electrical communication between the atmospheric and the vacuum side. D-sub connectrs as well as circular metal connectors will be mounted on the CNC panel, and their copper connections will be potted though a metal insert which has the rok of isolating the vacuum from any outside permeation or virtual leaks. The potted seal needs to be at least about 15mm thick, made out of a mix of torrseal and 832fx.

# Filament considerations in vacuum

In deep vacuum, most materials experience a certain degree of outgassing, given by the time taken for inner organic volatile gases to desorb and diffuse though the material walls. Most common outgas gases are H~2~O, H~2~, N~2~ or O~2~. H~2~O typically represents 80% of the total outgas quantity, depending on the specific atmospheric conditions in which the material has absorbed water form the atmosphere. Materials such as metals also experience outgassing, water vapor traveling through the metal walls and out into the vacuum chamber. Filaments and components are usually degassed and baked for couple days prior to usage, removing most of the absorbed gas.

Furthermore, as one study puts it, “Outgassing rates, for example, largely determine a material’s suitability for vacuum or space applications. Perhaps more importantly, the suitability of a material for applications in gas sensing, for gas filters, or for gas storage strongly depends on the ability of the material to uptake or desorb gas.”

Filament outgassing represents a great cause of concern for our project, given that if filament is not properly deep vacuum dried before use, it would foam and basically explode when molten at 250 C inside the printing chamber. Therefore, it's important we take into consideration proper filament drying techniques in vacuum, as well as specific filament differences that help us choose the best polymer for vacuum use. 

Filaments that can be considered vacuum grade have low outgassing and diffusion coefficients, meaning that they release less gas when put under high vacuum. Vacuum grade filaments should also allow for gas desorption in an acceptable amount of time, vacuum components being typically degassed and baked before use. 

ABS has a lower diffusion rate when compared to PLA and PETG, sitting at around 8.1 × 10^−8^ cm^2^/s and 8.3 × 10^−8^ cm^2^/s, respectively. Water diffusion through ABS is similar to typical elastomer seals used in high-vacuum systems (viton o rings or buna-N), making it a suitable polymer that can be used in vacuum systems, especially in our project. Amorphous materials (such as plastics and glass), have a glass transition temperature, which once passed can alter structural strength, making them soft and malleable. ABS glass transition temperature sits between 105-115 C. ASA, a close polymer in chemical composition to ABS, has a slightly lower glass transition phase, a minimum of about 100 C. The same aforementioned article suggests that, ABS baked at 103 C-just under the glass transition temperature-in high vacuum for about 3 days removes almost all gas from the filament. Outgas rates depends on gas diffusion path through the inner walls of the material, which makes it easy for filament outgassing, given its small thickness.

![Fig. 4](https://cdn.ncbi.nlm.nih.gov/pmc/blobs/7147/5514850/f5e40729d98f/nihms868979f4.jpg)

Figure 8: mass variation during vacuum drying of an ABS sample- rectangular cuboid of dimensions of 6.0 mm × 48.0 mm × 24.9 mm and a mass of approximately 6.5 grams (before loading with gas)

ASA is typically considered a better alternative to ABS, having better mechanical and chemical properties, as well as generally higher resistance to environmental factors that would otherwise degrade in time most polymers. Its superior diffusion coefficient allows for higher resistance to environmental factors that would otherwise degrade other polymers, having higher moisture resistance and less gas retention, as well as better UV resistance and less release of toxic fumes during 3D-printing (such as styrene when printing with ABS) amongst others. Water reabsorption of ABS and ASA filaments sits between 0.2-0.6% by weight, depending on time of exposure, and the humidity level of the atmosphere in which the filament spools have been deposited. Therefore, it should be tested if ASA yields better results in near vacuum printing when compared to ABS.

Storing and vacuum drying filament spools in controlled chambers before use could also drastically improve print quality, not just film deposition, by removing virtually all moisture from the filament. Therefore, a chamber in which filament is stored would have to be build next to the printer, bypassing the main vacuum pump to it. Also, a heater would have to be mounted inside so that filament can be baked and vacuum dried before use. 

In normal printing mode, pressure inside the chamber will be kept slightly higher than in film deposition mode, given that filament is heated beyond melting temperature during printing, resulting in higher outgas rates and possible foaming in high vacuum. During film deposition, air inside the chamber will be pumped down, the temperature of the plastic printed substrate remaining lower than bed temperature, and thus lower than the temperature at which filament had been baked before use, keeping outgassing at a minimum.