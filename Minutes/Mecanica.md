---
title: Mecanica
description: 
published: true
date: 2025-06-03T15:11:42.865Z
tags: 
editor: markdown
dateCreated: 2024-11-16T14:33:08.460Z
---



# Minuta 15 Noiembrie 2024
>Participanti :  Alex Dedu, Miruna Cătălin, Stefan Mihai, Bogdan Buzgaru, George Constantinescu, Ciprian Petre, Sasha Vovcenco, Cristi Dobrin, Alex Iercosan, Tudor Scarlat, Radu Cătălin, Iannis Voicu, Andrei Oprea. 

Alex Iercosan si Bogdan au configurat router-ul si AP-ul. S-a montat cosul la inaltimea corespunzatoare. Am montat si sistemul de agatare al robotului pe bara. Am discutat despre battle bots si drona. Asteptam miercuri, 20 noiembrie sa testam robotul dupa ce va fi programat.

~Bogdan

# Minuta Programare x Mecanica 20 noiembrie

> Participanti: Alex, Radu, Ciprian, Bogdan, Sasha, Miruna, Andrei, Stefan, Tudor si Ioana 

Stefan si Tudor au realizat un model 3d in Fusion pentru drona, inspirandu-se dupa o poza a unui quadcopter.
Am realizat ca jumatate din prelungitoarele servo-urilor erau cam nefunctionale si le-am inlocuit, iar mai apoi ne-am distrat cu encoderele. Am reusit pana la urma sa facem robotul functional, ar mai trebui adaugate niste greutati pe robot, deoarece glisierele sunt cam grele, iar robotul nu este destul de stabil, de asemenea motorul de ridicare al glisierei ar trebui inlocuit cu unul ceva mai puternic pentru ca avem mici probleme in momentul in care glisiera este intinsa la maxim. 
Am facut si lista care contine componentele de care avem nevoie la Ploiesti.

~Bogdan


# Minuta Mecanica 27 noiembrie 2024 

>Participanti: Alex, Alex, Cristi, Ioana, David, George, Bogdan, Stefan, Sasha, Miruna, Radu, Andrei.

1. BRAINSTORMING
Motoare in afara canalului 

Avantaje:

-spatiu in canal (odometre, axuri)


Dezavantaje:

-spatiu in partea de sus
-centrul de greutate
-joc in motoare



Am ajuns la concluzia ca punem motoarele in canal, deoarece rezolva toate defectele, iar spatiul din canal nu este asa de valoros

Daca avem loc sa punem odometrele in canal le punem in canal, iar daca nu este loc le punem pe lateral si printam o protectie 

Vom printa o protectie pentru roti, avand in vedere ca bateria este la fel de lata ca rotile vom avea loc si pentru baterie special facut din print

Vrem sa cumparam un extender de servo, deoarece ridica tensiunea din servo la 7 V.

Am ales sa utilizam glisiere liniare,cu transmisie pe curea, rulmenti cu flansa si in partea de jos vom pune la motor fulie(printata daca nu se gaseste de cumparat, 80/60 dinti)

Glisiere orizontale SAR230 3-stage cu curea
Glisiere verticale SAR230 4-stage cu curea

glisierele de pe orizontala sa fie actionate de un singur motor( rpm de experimentat)
cele doua funii de pe glisierele sa fie coliniare; 

Prioritatea nr 1 sunt sample urile si specimenele, NU catararea. 

glisiera orizontala trb sa fie LA MIJLOCUL pozitiei cubului  de pe podea si cubului parcat in robot.
pct ul de pivot al glisierei verticale trb sa fie intre(LA MIJLOC) pozitia de parcare si  cea a specimenului de pe plexiglass. 


!! Chestii importante de cumparat: !!

-extender de servo (servo power module, REV, https://www.revrobotics.com/rev-11-1144/)
- 4x motoare 1100 rpm (GoBilda, Rex Shaft, 8mm REX, 24mm Length Shaft (5203 Series)  https://www.gobilda.com/5203-series-yellow-jacket-planetary-gear-motor-5-2-1-ratio-24mm-length-8mm-rex-shaft-1150-rpm-3-3-5v-encoder/)
- 3x rulete 5m 
- hub rex, hub dshaft, 8 de fiecare
-axe dshaft si rex;

2. A VENIT ODOMETRIAAA( facem sasiu pe care sa o montam)

~Ioana

# Minuta Programare x Mecanica 6 decembrie

> Participanti: Alex Dedu, Alex Iercosan, Cristi, Radu Catalin, Radu Garbaci, Bogdan, Sasha, Ioana, Tudor, Stefan Mihai, Ciprian, Iannis

L-am reparat pe Peter, am pus glisiera si Alex, Ioana, Radu Catalin au fost indrumati de Alex Iercosan au facut prelungitoare custom de servo, acestea au fost bine primite de catre Peter :)
Cristi a facut un model 3D pentru hub-urile rotilor
S-au facut 2 dintre etapele de tuning ale autonomului pe robotul de test 
La final am facut bagajele pentru demo-ul de pe 8 decembrie de la Poli si le-am dus la Alex Dedu acasa.

~Bogdan


# Minuta sedinte 23 dec - 2 ian mecanica

> Participanti (cel putin intr o zi): MARK ERENA, Ciobotenco Vlad, Stefan (Caramida), Alex Dedu (eu), Ioana Constantinescu, Radu Catalin, Radu Garbaci, Alex Iercosan, George Constantinescu, Stefan Mihai, Bogdan Buzgaru, Andrei Mocanu, Miruna Catalin

A VENIT MARK LA ATELIEEERR!!! 

Stadiul robotului: George a facut la firma unde lucreaza sora lui cu placile la cnc pentru outtake. Au fost montate pe sasiu. Au fost montate temporar glisierele de outtake (spun temporar pentru ca vor trebui scoase cand vin rulmentii si cureaua). Motoarele pt glisiere sunt doua pana cand va fi gata cutia de viteze si sunt pe sasiu impreuna cu un ax cu fuliile printate. 

Foarfecele au avut mari probleme cu frecarea dar s a rezolvat dupa ce s au slabit suruburile dintre fiecare piesa de pe ea. Totusi una dintre glisierele orizontale trebuie desfacuta si unsa pt ca se cam blocheaza la mijlocul drumului. Glisierele orizontale sunt si ele montare pe robot alaturi de intake.
 
Intake ul are nevoie de niste îmbunătățiri de care s au vorbit si pe grupul de whatsapp: sa facem pereti laterali ca sa nu fuga sample ul si sa pune tuburile de silicon care sunt mai felxibile cand ajunge comanda. 

Si bratele si gripperul de outtake a fost montate. Se pare ca bara dintre glisiere este perfect pusa in asa fel incat glisiera sa se poata ridica, iar bratul sa treaca la limita pe langa aceea bara (sampleul se loveste dar se poate da bratul pe dedesubt). 

Parking stationul ar merge sa aiba zona unde sta sample ul putin extinsa pt ca sample ul are sansa sa cada si ar fi indicat sa nu ne bazam doar pe intake neaparat ca l va tine acolo