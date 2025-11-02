---
title: Smart Trashcan
description: 
published: true
date: 2025-11-02T17:26:39.941Z
tags: 
editor: markdown
dateCreated: 2024-11-11T20:49:35.696Z
---

# Descriere

Un cos de gunoi inteligent ce sorteaza patru tipuri de ambalaje(metale-doze si conserve, plastic-sticle/SGR-uri, gunoi menajer si sticle din sticla), fara a fi nevoie de interventie umana.

Aparatul foloseste o combinatie de senzori pentru a discerne tipul de ambalaj introdus in aparat.

Cosul este rapid, determinand o detectie eficienta ce faciliteaza reciclarea a multiple ambalaje intr-o durata scurta de timp. Aparatul este suficient de compact cât sa poată fii atașat unui cos de gunoi usor modificat, tetracameral.

| ![screenshot_2025-05-25_140819.png](/screenshot_2025-05-25_140819.png) |
| -- |


# Obiective

* Construirea unui cos compact ce poate fi folosit in spatii publice, plaje/spatii de birouri/blocuri etc. unde acest dispozitiv poate fi folosit pentru eficientizarea procesului de reciclare si salvarea de timp.
* Proliferara unui comportament responsabil si limitarea poluarii.
* reciclarea ambalajelor din cadrul atelierului nostru si crearea unei baze de date ce 


# Constructie

Cosul consta dintr-un cilindru rotativ aflat la o inclinatie de 30 de grade, cosul in sine fiind compus dintr-un cos normal, cu gura fie rotunda fie patrata, impartit in 4 camere de depozitare pe diagonalele cosului. Astfel, proiectul si device-ul in sine reprezinta mai mult un "accesoriu" compact ce poate fi usor integrat in orice spatiu de functionare.
  
![proiect_walle.jpg](/proiect_walle.jpg)

## Parcursul unui ambalaj prin cos

 Pentru inceput, este important sa se precizeze faptul ca cilindrul ocupa un volum adaptat pentru o sticla de 2L (aceasta reprezentand volumul maxim ce poate fi gazduit de catre ansamblu fara a exista riscul sa cedeze structura cosului din cauza greutatii excesive).
 
### 1.  CANTARUL
Cantarul are 3 roluri importante: detecteaza intrarea unui ambalaj in cilindru, incepand procesul de detectie. 2-masoara masa ambalajului si 3-mentine in loc obiectul pentru a putea fi continuat procesul de scanare, pana la sortarea acestuia intr-unul dn cele 4 compartimente.

 La baza cantarului sta un loadcell, aflat intr-o configuratie de parghie, in combinatie cu un amplificator digital hx711. Acesta functioneaza ca un rezistor a carui valoare se modifica in urma aplicarii unei forte exterioare. Astfel, cantarul masoara magnitudinea fortei si o transforma in unitati de masa.
 
|![screenshot_2025-05-25_131221.png](/screenshot_2025-05-25_131221.png)| ![load-cell-diagram-72.png](/load-cell-diagram-72.png)|
| -- | -- |

 [Mai multe detalii referitoare la functionarea unui load cell](https://learn.sparkfun.com/tutorials/getting-started-with-load-cells/all)
 
### 3. Detectorul de metale
 
1. Folosim un detector de metale custom format dintr-o bobina ce incojoara cilindrul.


##### Circuit custom de detectie metale

Circuitul consta dintr-un filtru LR highpass (L-inductor si R-rezistor) prin care trece un curent AC de eprox. 10kHz. Inductorul este format dintr-o bobina cu un diametru de aprox. 10-11cm si aprox. 100 de ture de cupru cu diametru de 0.4mm (L aprox.= 625 uH).
  Pe urma, semnalul trece printr-o dioda simpla de semnal la care este legat un condensator de poliester de 100nf.
  
  La introducerea unui obiect metalic in intriorul detectorului, inductanta fie scade, fie creste, caz in care valoarea de referinta de pe condensator de eprox. 530mV se va modifica. Precizia detectorului se bazeaza cel mai mult pe geometria ambalajului, nu pe masa acestuia sau grosimea materialului metalic. Astfel, pentru acuitate marita este nevoie ca linile campului magnetic sa fie perpendiculare pe suprafata metalica. Astfel, ambalajele de aluminiu ce sunt considerate ca fiind "gunoi menajer" sunt sortate cu succes, fara a fi confundate de aparat ca fiind doze metalice.
  Amplificatorul digital folosit este tot hx711, fiind folosita setarea de gain de 32biti.

| ![schema circuitului](/aaa.webp) |
 

  
Astfel, legand valoarea condensatorului la un amplificator digital, se poate obtine precizie mai mare pentru obiecte metalice mai mici si, de asemenea, se poate comunica valoarea mai departe raspberry pi-ului.
Avantajele detectorului sunt multe: precizie mai ridicata, comparativ cu senzorul inductiv, design mai compact, lipsa nevoii de a stii exact locatia ambalajului in cos etc.
Un dezavantaj ar fi riscul ca obiectul reciclat sa ramana blocat in cadrul detectorului, lucru ce a fost rezolvat din cod prin "impringerea" ambalajului in momentul soratrii de catre "falcile" ce suporta greutatea ambalajului. De asemenea, se poate mari usor diametrul detectorului si poate fi adaugat un fillet/chamber pe partea interioara pentru a putea impune ambalajului sa alunece/rastogoleasca in mmentul inclinarii cilindrului.

![detectormetale_walle.jpg](/detectormetale_walle.jpg)
   
### 5. Lidar
  
  Urmeaza sa fie testat un modul lidar cu precizie de 64 de pixeli [VL53L7CX](https://www.robofun.ro/vl53l7cx-time-of-flight-8-8-zone-wide-fov-distance-sensor-carrier-with-voltage-regulator-350cm-max.html?gad_source=1&gad_campaignid=20383925641&gclid=Cj0KCQjw_dbABhC5ARIsAAh2Z-SsQSl8gLTzo1tBTG-PHYMbIrvgGt-ZnvaIW4blQK0FZV3CvSHxr8AaAv7REALw_wcB). Cu acest senzor se masoara dimensiunile ambalajului.

  ![drawing1.jpg](/drawing1.jpg)

note post teste: lidarul are suport doar pentru librărie de python și de c++, neexistând nici o librărie ce implementează pi4j. Din acest motiv, am înlocuit lidar ul cu un simplu senzor de distanta tof de la rev de 2m, acesta citind suficient de  precis distanta catre vârful ambalajului care sa nu afecteze detectie. in versiunile viitoare, codul va fi cel mai probabil rescris în c++ sau python, iar lidar ul va fi folosit în detrimentul senzorului de la rev pentru precizia sa mai ridicata de detectie.

Senzorul de distanta mai are și un al 2lea rol: acesta functioneaza și ca senzorul de proximitate. senzorul, fiind amplasat in partea superioara a cilindrului, la întrarea ambalajelor în ansamblu, este destul de sensibil la orice introducerea în cos al unui ambalaj, indiferent de mărimea acestuia, in cod valorile inregistrate de acest senzor fiind folosite pentru începerea procesului de detecție. De asemenea, daca ambalajul introdus este prea mic/usor pentru a putea fi detectat de alt senzor, înregistrarea intrarea unui astfel de ambalaj in ansamblu de catre senzorul tof permite sortarea acestuia în compartimentul de gunoaie menajere.

### 5. Senzor capacitiv de proximitate
Acest senzor are rolul de a detecta prezent lichidelor in interiorul ambalajelor. Procesul este automatizat, astfel incat dupa ce se stabileste ca ambalajul este de tip "sticla", ansamblul incepe sa "impunga" sticla pentru a facilita contactul dintre senzor si ambalaj. In cazul in care este detectat lichid in interiorul sticlei, aceasta este imediat trimisa catre compartimentul de gunoaie menajere, fara a fi nevoie de interventie din exterior pentru indepartarea obiectului. Cu toate acestea, pentru o reciclare cat mai corecta, utilizatorii vor fi rugati sa indeparteze orice lichid din interiorul sticlelor inainte de introducerea acestora in ansamblu. Senzorul capacitiv este un senzor ce detecteaza schimbarea in indicele dielectric din mediul inconjurator, materialele conductive (precum metale/apa) avand o constanta dielectrica mult mai ridicata.

nota: v_out al senzorului este, initial, aproximativ 20V, egala cu valoarea voltajului furnizat de sursa (lrs 50-24 meanwell). Senzorul foloseste un optocuplor și câteva rezistoare pentru a schimba voltajul de ieșire de la 20v la 3.3v când e high, și aprox. 600mv low. Astfel, este folosit nivelul de voltaj logic necesar pentru detectia raspberry pi ului. Ambalajul este "împins" de senzor de 2 ori pentru a asigura un contact bun pentru detectia lichidului in ambalaj.


|![051135_5_522_1024x1024.webp](/051135_5_522_1024x1024.webp)|![whatsapp_image_2025-11-02_at_18.25.12_2e654ebd.jpg](/whatsapp_image_2025-11-02_at_18.25.12_2e654ebd.jpg)|
| -- | -- |
	

# Metoda de detectie

  Cantarul masoara schimbarea treptata a valorii de referinta a cantarului in momentul intrarii unui obiect in ansamblu. In acest fel, sunt evitate masuratorile false aproape spre 0, schimbarile bruste care pot fi atribuite fie introducerii unui ambalaj cu o masa respectiv mare, fie unor spike-rui in voltajul de linie al sursei fiind verificate de doua ori pentru stabilirea naturii acestora. Schimbarile relativ mici, aflate sub un anumit prag stabilit empiric sunt considerate ca fiind rezultatul introducerii unui ambalaj cu masa mica, precum un servetel sau o hartie mototolita, acestea fiind detectate imediat si trimise mai departe prin tot circuitul de scanare.
  
  In continuare, este masurata inaltimea ambalajului, fiind stabilit daca acesta este de tip menajer (ambalaj usor, hartie mototlita/servetel/celofan), sau de tip sticla (doza, sticla de sticla/plastic etc.). Daca inaltimea ambalajului este sub un anumit prag (in general, 40mm), atunci acesta este sortat automat la gunoaie menajere. Altfel, este continuat procesul de scanare.
  
  In aceslasi timp, este masurata masa ambalajului, fiind pusa in raport cu inaltimea ambalajului. Astfel, este calculata o contanta k = masa/inaltimea ambalajului. Aceasta constanta ne ajuta in stabilirea naturii ambalajului, constanta fiind mai mare pentru ambalaje mai grele, cum ar fi sticle de sticla, comarativ cu alte ambalaje cum ar fi sticlele de plastic. Astfel, pot fi sortate cu precizie sticlele de sticla fata de cele de alt material, fiind gasit un prag numeric empiric sub care se afla sticlele si ambalajele de plastic sau carton si peste care se afla ambalajele de sticla. Aceasta constanta empirica, T este egala cu 0.5 din multiple teste efectuate. k normal pentru o sticla de plastic este intre 0.15-0.3, pentru sticle este minim 0.7 si maxim aprox. 2.5 . Astfel, orice ambalaj aflat sub 0.1 este clar menajer, peste 2.5 este un ambalaj plin cu apa care este sortat automat la menajere.


|![chatgpt_image_nov_2_2025_07_01_45_pm.png](/chatgpt_image_nov_2_2025_07_01_45_pm.png)|![chatgpt_image_nov_2_2025_07_13_04_pm.png](/chatgpt_image_nov_2_2025_07_13_04_pm.png)|
| -- | -- |


”

In acelasi timp, detectorul de metale va incepe sa functioneze, citind datele primite de la acesta. Daca valoarea inregistrata difera fata de valoarea de referinta, atunci ambalajul va fi categorisit ca fiind metal, fiind trimis in compartimentul de metale. Din fericire, atat senzorul inductiv cat si detector de metale poate diferentia atat metalele feroase, cat si cele neferoase, putand fii cu usurinta diferentiate.
  
Daca ambalajul este menajer,a tunci cantarul se va roti in partea stanga aprox. 60 de grade pentru a permite produsului sa cada in interiorul structurii de sustinere.

In cazul in care ambalajul este sticla, cilindrul se va roti 90 de grade spre stanga in timp ce actioneaza "falcile" pentru a impinge si a depozita obiectul.

Daca ambalajul este metalic (doza) , atunci cilindrul se va roti 90 de grade spre dreapta pentru a sorta ambalajul.

Daca ambalajul este sticla de plastic, atunci falcile ce sustin obiectul se vor deschide si vor lasa ambalajul sa cada in interior.

![screenshot_2025-05-25_135908.png](/screenshot_2025-05-25_135908.png)

 (versiuni viitoare:) In interior se va afla o pereche de perii/rotite ce au rolul sa preseze usor ambalajul. Un microfon aflat in partea superioara a structurii de sustinere va recepta sunetul produs. Pe urma, cu ajutorul unei librarii de python va fi efectuata o analiza fourier a sunetului (fft), fiind astfel diferentiate sunetele produse de ambalaje din carton fata de ambalaje din pastic. Cartonul produce un sunet de intensitate mai mica si frecventa mai joasa, pe cand plasticul produce un sunet mai intens si de frecenta mai inalta, astfel reprezentand o metoda ce merita explorata si posibil implementata pentru sortarea plasticului vs cartonului.

In cazul in care ambalajul este de tip carton, acesta va fi trecut mai departe prin perii, fiind sortat in compartimentul pentru gunoaie menajere. Sticla, fiind mai rezistenta, va cadea in interiorul cilindrului, "falcile" ce mentin structura deschizandu-se la 45 de grade fiecare pentru a permite ca ambalajul sa cada in interior. Astfel, periile nu trebuie sa aiba putere foarte mare, acestea presand doar usor ambalajul.
  
|![screenshot_2025-05-25_141411.png](/screenshot_2025-05-25_141411.png)|![screenshot_2025-05-25_141800.png](/screenshot_2025-05-25_141800.png)|
| -- | -- |
  




# Folosirea optimizarii topologice in design
Piciorul de sustinere fost optimizat topologic, folosind uneltele de simulare din fusion pentru a-i reduce masa si pentru a obtine rezistenta maxima.


|![screenshot_2025-05-13_202210.png](/screenshot_2025-05-13_202210.png)|![screenshot_2025-05-25_161333.png](/screenshot_2025-05-25_161333.png)|![screenshot_2025-05-25_161348.png](/screenshot_2025-05-25_161348.png)|
| -- | -- | -- |

Aceasta structura, comparativ cu piciorul de raft din [proiectul de cercetare](https://wiki.teamclockworks.ro/en/Projects/optimizare-topologica) pentru tool-ul de optimizare, a fost creat folosind metoda 2.
 Astfel, in urma efectuarii si repetarii simularilor, piesa originala a fost modificata pentru a putea beneficia atat de o printabilitate mai usoara, cat si de avntajele obtinute prin reducerea masei piesei, in cazul modelelor mari, tool-ul putand fi de ajutor pentru a reduce cantitatea de filament folosit.
 
 
 
 # Urmatorii pasi
 
 1. Stuctura - suportul alb e done, trebuie aliniat servo in cadru
 ax rev cu 2 rulmenti in suport, ingropat in piesa portocalie.
 piesele porticalii sunt legate structural cu 2 profile extrudate 2020 in partea de sus
 tot caruciorul este rotit de un servo. D3e adaugat o rotata dintata sudata de carucior, care see cupleaza cu roata dintata din servo (1:1). In centrul rotii dintate iese un ax identic cu cel de jos si se sprijina in suportul de sus.
 rolele vor fi statice pentru primul prototip, separate fata de falci, cu prindere cu surub M3 in centru. Falcile vor fi prinse in carucior cu surub pe post de ax
 Falcile trebuie umplute pentru ca sunt foarte fragile. 
 De facut un triunghi din piese tetrix/rev care suporta cele doua parti
 Adaugat detectorul de cod de bare in pozitie statica
 
Estimat 1st proto: final de iunie
 