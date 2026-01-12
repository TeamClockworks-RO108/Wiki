---
title: Optimizare Topologica
description: ---
published: true
date: 2026-01-12T02:36:43.354Z
tags: 3dprinting, project, research
editor: markdown
dateCreated: 2025-05-13T05:32:37.620Z
---

# Descriere

Optimizarea topologica este un tool folosit în CAD pentru a îmbunătăți geometria pieselor afectate de stres mecanic

# Obiective

* Invatam sa folosim uneltele de optimizare topologica din Fusion 360
* Cercetam tehnici de optimizare a masei pieselor noastre
* Evaluarea fiabilitatii optimizarii topologice in proiectarea robotilor de FTC
* Publicam rezultatele obtinute in wiki-ul nostru si potential intr-un jurnal stiintific


# Cerinte 

Cerinta va consta in proiectarea a doua picioare de raft, avand ca scop rezistenta mărită comparativ cu raportul dintre masa optimizata si masa originala (targetul fiind de aprox. 57%). A fost aleasa tema piciorului de raft pentru simplitatea si eficienta testarii ei evaluarii rezistentei pieselor.

Proiectul reprezintă o buna oportunitate de aprofundare a cunoștințelor de Fusion și de proiectare 3D în general. De asemenea, familiarizandu-ne cu tool urile de simulare, pe lângă cel de optimizare topologica. Astfel, vrem sa ne obisnuim cu acest tool și sa ii verificam viabilitatea, integrandu-l in cât mai multe proiecte pe viitor (chiar și FTC) pentru a usura robotul și a economisi filament.

Modelul optimizat trebuie sa aibă o structura ce se poate printa fără suporti (overhanguri < 50°), ignorand timpul de printare pentru overhanguri.

Observam ca optimizarea topologica nu este o tehnica raspandita in FTC si ne dorim sa evaluam daca efortul depus cu aceasta etapa de proiectare ne ofera un avantaj fata de celelalte echipe. Pe langa argumentul tehnic, putem folosi optimizarea topologica pentru a demonstra tehnici de design industrial in interviurile cu juratii concursului.


# Modelul 3D

Vom utiliza un model 3D al unui picior de raft montat pe un perete fix. Raftul sustine o sarcina verticala pe suprafata de sus.
In comparatia de mai jos putem vedea atat piesa originala cat si piesa optimizata la aproximativ 57% din masa piesei originale. Piciorul de raft optimizat trebuie sa se printeze cu cat mai putin material dar sa isi pastreze proprietatiile mecanice. 

| Piesa originala    | Modelul optimizat |
| -------- | ------- |
| ![](/screenshot_2025-05-13_190310.png)  | ![](/screenshot_2025-04-26_232312.png) |


# Etape

1. Proiectarea 3d a pieselor ce trebuie optimizate
2. Utilizarea tool-ului si extragerea unei comparatii la mai multe grade de umplere
3. Printarea pieselor, impreuna cu evaluarea printabilitatii
4. Verificarea rezistentei pieselor

# Analiza stresului

Pentru a rula o optimizare topologica, incepem prin a configura zona fixa de sprijin (suprafata plata - peretele) si sarcina ce actioneaza asupra obiectului. 


Piesa originala trebuie sa fie suficient de masiva cat sa permita optimizarii sa aiba cu ce lucra, oferind in final un model al distribuirii stresului mecanic din interiorul piesei. Programul lucreaza eliminand materialul care nu preia suficient din sarcina mecanica, lasand doar zonele in care sarcina trece peste un prag. Pragul poate fi stabilit automat de catre Fusion sau poate fi setat de catre utilizator. Acest target reprezinta raportul procentual dintre masa piesei optimizate si masa piesei originale. In functie de modelul 3d original, acest target difera, valoarea maxima aflandu-se la un 60% si un mimim de aproape 40 sau 30%.

Mai jos putem vedea piciorul de raft simulat in 3 exemple in care configuram pragul de eliminare a materialului la 3 valori, exemplificand extremele plajei:

| 100% | 57.6% | 32% |
| ---- | ----- | --- |
| ![](/screenshot_2025-05-13_194556.png) | ![](/screenshot_2025-05-13_194632.png) | ![](/screenshot_2025-05-13_194646.png) |
| Pragul de masa este 100%, deci avem chiar piesa originala. Putem vedea distributia stresului mecanic, unde peretii nu contribuie prea mult la rezistenta piesei. | La 57.6% obtinem o taiere optima. Piesa isi pastreaza structurile critice desi cantareste cu foarte putin peste jumatate din masa originala. | La 32% umplere pierdem atat structuri critice cat si structuri non-critice, rezultatul devenind neoptim.

Observam ca simularile de optimizare trebuie efectuate de mai multe ori, pe mai multe cazuri, iar parametrii simularii trebuie ajustati pentru imbunatatirea rezultatelor.

# Printabilitatea pieselor optimizate

Majoritatea surselor afirma ca, in majoritatea cazurilor, daca piesa originala are o structura ce se poate printa fara suporti, atunci si piesa optimizata va putea fi printata fara suporti. Structura optimizata are de cele mai multe ori un aspect organic, cu overhanguri mai mici de 50 de grade. De asemenea, directia pe care o stabilesc structurile organice din interiorul pieselor optimizate depind in principal de directia fortei aplicate asupra sa, fiind un aspect de luat in calcul atunci cand straturile trebuie orientate pe o anumita axa pentru a spori rezistenta. Desi piesa se poate printa fara suporti intr-o anumita orientare, de cele mai multe ori nu va lasa prea multe alternative designer-ului pentru a o orienta pe alta fata.

Este foarte important ca rezultatele sa fie verificate printr-o alta simulare, stress test, aceasta validand rezistenta structurii. Simularile trebuie refacute de multiple ori pentru a valida rezultatele, atat simularile de optimizare, cat si cele de stress test. Pe langa asta, uneori este nevoie sa fie facute modificari si in design, permitand o printare mai usoara.

# Continuarea proiectarii dupa optimizarea topologica

Odata ce suntem multumiti de ce avem, trebuie sa dam promote la rezultatele optimizarii, adica sa le transformam intr-un STL ce se transfera in spatiul de design. De aici, exista doua cai diferite ce pot fi abordate.

1. Conversia din mesh catre corp solid (STEP): 
Intrand in sectiunea de “mesh” ce exista in spatiul de design, mergi la modify si apasa “convert mesh”. Selecteaza mesh-ul simularii si foloseste metoda faceted (prismatic nu va merge). Inainte de asta, este recomandat sa dai repair la mesh si sa reduci numarul de poligoane a modelului. Altfel, in timp ce dai convert la mesh sau dupa, e o sansa mare ca fusion-ul sa dea crash sau sa foloseasca mai multe resurse ale pc-ului decat este nevoie. La final ramai cu un STEP al simularii. Recomand sa se dea cut la piesa originala si la cea optimizata, in acelasi timp (acestea fiind suprapuse), in zonele care interactioneaza cu alte piese sau cu mediul real, iar apoi sa se dea remove la partile ce nu sunt necesare ca pe urma sa se dea combine la corpurile ramase. Astfel, va fi obtinuta o piesa curata, usoara si care poate fi montata usor.

2. Folosirea rezultatelor ca o referinta pentru un nou design:
Simularea reprezinta un cadru pentru un nou design, facut de la 0 sau imbunatatit pe piesa originala, astfel oferind o idee generala a distributiei stresului mecanic din piesa. Aceasta metoda cere efort mai mare, dar ofera rezultate pe care proiectarea ulterioara se face mai usor, fara dificultatile de a lucra pe o piesa ce contine mii de poligoane. 
Piesa din imaginea de jos a fost creata folosind metoda 2 a optimizarii topologice. Rezultatele simularii au fost folosite ca o baza pentru un nou design.

![](/screenshot_2025-05-13_202210.png)

# Printarea pieselor optimizate

Vom analiza timpul de printare si consumul de material pentru piesa originala si cea optimizata cu prag de 57%.

Studiu pentru 4 perimetre si 25% infill gyroid:

| Metrica | Original (100%) | Optimizat (57%) | Schimbare |
| --- | --- | --- | --- |
| Greutate | 42.8g | 36.63g  | -16% | 
| Timp Total | 1h39m | 1h48m  | + |
| Timp Perimetre | 1h4m | 1h16m | + |
| Timp Infill | 31m | 19m | - |

Studiu pentru 4 perimetre si 80% infill:

| Metrica | Original (100%) | Optimizat (57%) | Schimbare |
| --- | --- | --- | --- |
| Greutate | 75.88g | 49.56g  | -36% | 
| Timp Total | 3h6m | 2h25m  | - |
| Timp Perimetre | 1h4m | 1h16m | + |
| Timp Infill | 1h57m | 55m | - |

Deoarece se mareste suprafata exterioara a obiectului, este de asteptat ca timpul de printare al perimetrelor sa creasca. Astfel, creste timpul de printare total. 
Volumul interior al obiectului scade, deci volumul ocupat de infill scade si el. Daca intentionam sa printam cu infill mare, prin scaderea volumului, timpul de printare scade.   
  
De exemplu, daca dorim sa fabricam piesa originala la 60% infill, putem in schimb sa fabricam piesa optimizata la 90% infill folosind cu 20% mai putin material si acelasi timp de printare. In comparatia urmatoare se poare observa diferenta de densitate:

| 60% Infill (original) | 90% Infill (optimizat) |
| --- | --- |
| ![screenshot_20250522_211756.png](/screenshot_20250522_211756.png) | ![screenshot_20250522_211733.png](/screenshot_20250522_211733.png) |

# Concluzii

Tool-ul de optimizare topologica este destul de usor de utilizat in Fusion, licenta de student permitand folosirea simularilor fara vreun cost aferent (cloud credits). Simularile sunt versatile, iar rezultatele vorbesc de la sine. Totusi, multe surse mentioneaza alte programe de CAD ce permit folosirea tool-ului intr-un mod mai complex, nefiind limitat de interfata si de simplicitatea Fusion-ului. Pe aceasta cale (si din alte motive), cred ca se merita in viitor sa dam o sansa si altor programe de design 3D (Autodesk Inventor), rezultatele obtinute avand potentialul sa creasca nivelul la care se face CAD in cadrul clubului.

Cu toate ca de multe ori nu scade timpul de printare a pieselor, avem parte de un consum redus de material. Abia cand intentionam sa printam cu un procentaj mare de umplere, optimizarea topologica straluceste in domeniul imprimarii 3D facand atat consumul de material, dar si timpul de printare mult mai mici.

# Resurse si bibliografie

[Making STRONG shelves with Topology Optimization](https://www.youtube.com/watch?v=3smr5CEdksc&t=304s) (un videoclip ce exploreaza aceeasi problema, propunand o idee despre cum se poate folosi acest tool in Fusion)

[TUTORIAL: Topology Optimization in Fusion 360 – 3D printing filament spool holder](https://www.youtube.com/watch?v=hAGFkWkqocI) (un videoclip ce exploreaza acelasi tool, dar abordeaza folosirea simularilor de optimizare intr-o modalitate diferita, simularile reprezentand un “frame”, un punct de pornire pentru modelarea pieselor).

[Topology Optimization and Autodesk Fusion - Fusion Blog](https://www.autodesk.com/products/fusion-360/blog/topology-optimization-and-autodesk-fusion/#:~:text=Autodesk%20Fusion%20incorporates%20topology%20optimization%20principles%20into%20its,beyond%20manual%20iteration%20and%20access%20AI-assisted%20design%20exploration.?msockid=36a662a0ba9763cd37f6715bbb6d6277) (documentatie tehnica fusion)

[Convert STL Mesh to a Solid Body in Fusion 360 (2023)](https://www.youtube.com/watch?v=tVGtG-UjlYg&t=26s) /[Convert STL to Solid in Fusion 360 | Day 18 of Learn Fusion 360 in 30 Days - 2023 EDITION](https://www.youtube.com/watch?v=vr_zPVEsyjs&t=463s) (tutorial: cum se transforma o fila stl intr-o fila step)

De asemenea, stack overflow sau reddit reprezinta de asemenea surse ce pot fi de ajutor.