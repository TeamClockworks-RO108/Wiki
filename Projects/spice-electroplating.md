---
title: Spice Electroplating
description: 
published: true
date: 2025-12-09T06:37:12.281Z
tags: 
editor: markdown
dateCreated: 2025-11-28T04:20:41.717Z
---

# Description

**Sppice** (**S**pecial **P**late-on-**P**rint **I**on-**C**ooper **E**missions) is our attempt at embedding electrically conductive elements on 3D printed parts. We envisioned a two-step process that can be executed at a relatively low cost using commodity tooling.

# Process

To embed electrical conductors in a part, we will use a electrolysis bath to deposit copper metal where it is needed. To achieve this, traces need to be painted using electrically conductive paint (or paste) in order to become an electrode.

The process is subdivided further into the electrolysis bath in two main parts: strike bath and layer thickening. 

**Strike bath** is the first step, being composed of an aggressive plating process which strives to cover all of the printed traces in copper, making use of the electrical properties of the deposited layer. At this stage, we're using a low current (around 200mA).

The target is partially submerged in an initial solution that only contains copper sulfate and distilled water, allowing for local copper hydroxide deposition processes to take place on the top layer of the electrical trace.
![img-20251128-wa0026.jpg](/img-20251128-wa0026.jpg)
***diagram showing a profile view of the plating process during strike bath***

As it can be seen in the picture, there is a local hydroxide layer build on top of a thin, conductive copper layer. this helps speed up the copper deposition process (electrons being virtually pushed to the edge), allowing for uniform plating and excluding the possibility of thickness gradients being found in the conductive layer.

**Layer thickening** is the second step, allowing for copper deposition under normal conditions. Sulphuric acid is added to the mix, eating away any deposited copper hydroxide, revealing the conductive copper layer. At this stage, copper deposition happens at a very fast rate, trace resistance plummeting exponentially and allowing for low resistance, electronics grade traces to be formed. the acid also allows for higher currents to be used, breaking down any OH bonds.

## Evaluating and maintaining normal copper deposition rate

The quality of the deposited copper depends on a few variables: current, quantity/existence of acid in the chemical bath and copper replacement rate, which remains almost constant throughout most of the plating process.

For our experiment, we have used a sensitive power source, capable of reading mV changes in the solution bath. After the strike bath is finished and we start adding the acid, we can start increasing the current to about 300-500 mA. it's important we monitor the voltage rate of change. Rapid increases in voltage corresponding to hydroxide layer formation. A slow drop in voltage means the process is functioning and copper gets deposited correctly. As we have mentioned, resistance drops exponentially at this stage, final voltage readings corresponding to about a 0.1V drop. 

it's recommended we use a heater to keep the temperature constant in the solution bath. higher temperatures accelerate the process at low risks (compared to increasing the current). Also, they keep the resistance of the copper bath virtually constant (varying mostly only due to temperature changes which can be caused by the ongoing chemical reactions).

Furthermore, voltage changes are a nice way of evaluating and approximating voltage deposition, finding the appropriate time at which to physically check layer thickness.

## Electrode paste deposition

To create an electrically conductive solid layer, we started off using very fine graphite powder and a volatile solvent (acetone). This approach yielded good deposition uniformity and low electrical resistance, but the layer is mechanically very fragile. The graphite layer might diffuse inside the electrolyte bath and the deposited copper will peel off very easily.

To mitigate these effects, we added a binder to our paste. We tested three acetone-soluble polymers and settled on ABS, which had the best properties for our project. 

We also researched optimal drying conditions to evaporate the solvent. Tests showed that slower, cooler drying at about 55*C* prevents cracking of the paste layers from evaporation pressure. 

Different concentrations of binder were tested for mechanical properties and electrical resistance. It was found that, at low binder concentrations, electrical resistance is not significantly affected.



Overall electrical resistance can be greatly affected by the nature of the connection to the electrical wire:
 * Alligator clips offer 2-6 small points of contact with a high pressure. Contact resistance is on the order of kOhms.
 * A screw embedded inside the substrate, underneath the paste layer can give a few square mm's of good contact. Resistance is between 0 and 5 Ohms. 
 
Because acetone dries quickly at room temperature, it is difficult to obtain a smooth application of the paste. To combat this, we have designed insets where paste is deposited. This allows for the plastic part to be lapped using sandpaper and also creates a smoother surface finish for the deposited copper.

## Electroplating Bath

To deposit copper onto conductive paste layer, we are using the electrolysis of copper (II) sulfate (CuSO~4~), which is readily available for agricultural use. A current-controller power source is ideal because it will alow us to control the rate of deposition (mA/mm^2^) regardless of electrode contact resistance or other changing parameters.

It is very important for the metal anode contacts (wires, clips) to not come into contact with the electrolysis solution. Because of the higher resistance of the graphite paste (in comparison with pure copper or steel), failing to do so will leak most of the current trough the metal contact itself, bringing productive deposition of copper to a halt. To prevent this situation, we are routing anode contacts to the other side of the board using buried screws underneath the conductive paste. The board is partially submerged in the solution.

The rate of deposition is controlled by changing the outgoing current density trough the boundary of the paste. At higher currents, the Cu^2+^ ions are not replenished fast enough to carry the current, therefore water molecules are broken down into H^2^ and OH^-^. Hydroxide ions lead to the formation of unwanted Cu(OH)~2~, which can be spotted as green depositions around high-current areas. This phenomenon can be mitigated by adding a small amount of sulphuric acid (70g/L) which serves to oxidize the Cu(OH)~2~ back into CuSO~4~. The sulphuric acid also helps reduce the rate of Cu(OH)~2~ production by aiding with current carrying. 