---
title: Programare
description: 
published: true
date: 2025-06-03T15:11:41.072Z
tags: 
editor: markdown
dateCreated: 2024-11-14T15:41:24.277Z
---

# Minuta 14 Noiembrie 2024 
>Paricipanti : Sasha, Alex Iercosean, Alex Dedu, Ioana, Miruna, Bogdan

Ioana ne-a prezentat design-ul pentru aplicatia ClockWorks de care se vor ocupa maxim 2 pentru FE si 1 pentru BE si s-a vorbit despre cum vor face atelierul smart. Alex Iercosan a sugerat sa montam un router si un AP in atelier, pentru a putea avea acces remote la componentele din cadrul proiectului. Bogdan si Sasha se vor ocupa de proiectul de **Entry Point** pentru atelier. 

~Bogdan
# Minuta 16 Noiembrie 2024

> Participanti : Sasha, Alex, Ciobo, Ioana, Bogdan

Sasha ne-a prezentat [diagrama codului](/FTC/Into-The-Deep), Bogdan se va ocupa de gripper si Ioana se ocupa de bratul robotului, iar Sasha se ocupa de movement si controller.

~Bogdan

# Minuta Programare x Mecanica, 20 noiembrie

> Participanti: Alex, Radu, Ciprian, Bogdan, Sasha, Miruna, Andrei, Stefan, Tudor si Ioana 

Stefan si Tudor au realizat un model 3d in Fusion pentru drona, inspirandu-se dupa o poza a unui quadcopter.
Am realizat ca jumatate din prelungitoarele servo-urilor erau cam nefunctionale si le-am inlocuit, iar mai apoi ne-am distrat cu encoderele. Am reusit pana la urma sa facem robotul functional, ar mai trebui adaugate niste greutati pe robot, deoarece glisierele sunt cam grele, iar robotul nu este destul de stabil, de asemenea motorul de ridicare al glisierei ar trebui inlocuit cu unul ceva mai puternic pentru ca avem mici probleme in momentul in care glisiera este intinsa la maxim. 
Am facut si lista care contine componentele de care avem nevoie la Ploiesti.

~Bogdan

# Minuta Programare x Mecanica, 6 decembrie

> Participanti: Alex Dedu, Alex Iercosan, Cristi, Radu Catalin, Radu Garbaci, Bogdan, Sasha, Ioana, Tudor, Stefan Mihai, Ciprian, Iannis

L-am reparat pe Peter, am pus glisiera si Alex, Ioana, Radu Catalin au fost indrumati de Alex Iercosan au facut prelungitoare custom de servo, acestea au fost bine primite de catre Peter :)
Cristi a facut un model 3D pentru hub-urile rotilor
S-au facut 2 dintre etapele de tuning ale autonomului pe robotul de test 
La final am facut bagajele pentru demo-ul de pe 8 decembrie de la Poli si le-am dus la Alex Dedu acasa.

~Bogdan

# Minuta mentenanta robot inainte de demo, 7 decembrie

>Participanti: Sasha, Bogdan, Alex 

Am incercat sa rezolvam problemele de la quickstart-ul Roadrunner-ului si gradle-ul, dar nu prea ne-a iesit asa ca am facut un repo nou numit "FTC9", iar cel vechi a fost redenumit in "PREV-FTC-INTO-THE-DEEP", in repo-ul FTC9 am clonat repo-ul oficial FTC in loc de quickstart. 
De asemenea am schimbat si limitele bratului pentru a se conforma cu noul motor

~Bogdan

# Minuta Programare, 11 decembrie

>Participanti: Sasha, Bogdan, Ioana, David

Am progresat tuning-ul autonomului pe robotul de test, ajungand la ultimele 2 etape, Feedfoward si Feedback tuning, dar ne-am dat seama ca valoarea folosita pentru a calcula **inPerTick** a fost diametrul rotilor mecanum in loc de diametrul odometrelor => trebuie sa refacem tot tuning-ul de la 0 cu valoarea corecta. <br> De asemenea, a fost reinstalat Windows-ul pe laptop-ul care avea Linux Mint deoarece majoritatea membrilor nu stiu sa foloseasca Linux + era un laptop in minus pentru mecanica deoarece Fusion nu este complet compatibil cu Linux.


~Sasha

# Minuta Programare X Mecanica, 7 ianuarie

> Participanti: Sasha, Alex, Alex Iercosan, Bogdan, Cristi

Am tunat unghiurile de la servo-urile de la intake si am rescris codul pt intake pentru a automatiza toate miscarile servo-ului. A fost scris si codul pentru brat cu PIDF + au fost refacute butoanele pentru gamepad si impartite pe 2 gamepad-uri. Au inceput sa fie schimbate glisierele verticale de pe curea de transmisie GT2 pe sfoara.

# Minuta Programare x Mecanica, 8 ianuarie

> Participanti: Sasha, Alex, Radu, Alex Iercosan, David, Andrei Mocanu, Stefan Mihai

Intake-ul este acum complet automatizat cu un singur buton care face toata extinderea, rotirea si activarea intake-ului activ prin intermediul unui **state machine**. De asemenea, am programat gripper-ul pentru cele 2 unghiuri si asteptam sa il facem si pe al treilea cand avem un zid pe care sa testam colectarea specimenelor. 