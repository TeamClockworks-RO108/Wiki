---
title: Smart Trashcan
description: 
published: true
date: 2025-10-17T05:38:41.615Z
tags: 
editor: markdown
dateCreated: 2024-11-11T20:49:35.696Z
---

# Descriere

Un cos de gunoi inteligent ce sorteaza intre patru ambalaje: metale, plastic, gunoi menajer si sticla.

Aparatul foloseste o combinatie de senzori, plus in viitor citire de cod de bare pentru a putea determina materialul din care este facut obiectul

Cosul trebuie sa poată procesa suficient de repede ambalajele cât sa fie considerat satisfăcător in termeni de viteza. Va fi suficient de compact cât sa poată fii atașat unui cos de gunoi usor modificat, tetracameral.

Precizia de detecție trebuie sa fie satisfăcătoare și sa acopere o gama de ambalaje suficient de mare.

| ![screenshot_2025-05-25_140819.png](/screenshot_2025-05-25_140819.png) |
| -- |


# Obiective

* Introducerea unui cos in cadrul liceului cnghs pentru a atrage mai multi oameni catre stem si pentru a trage un semnal de alarma asupra nevoii protejarii mediului.
* Construirea unui cos suficient de precis si de eficient cat sa fie satisfacator, iar eroarea sa fie pastrata la un nivel cat mai jos.
* reciclarea ambalajelor din spatiu in care operam(ICPE) pentru a putea demonstra utilitate unui astfel de cos in spatii publice (cum ar fi plaje, institutii) si birouri.


# Constructie

Cosul consta dintr-un cilindru aflat la o inclinatie de 30 de grade, cosul in sine fiind compus dintr-un cos normal, cu gura fie rotunda fie patrata, impartit in 4 camere de depozitare (metale, plastic, sticla si gunoi menajer) pe diagonale. Astfel, cilindrul reprezinta mai mult un "accesoriu".
  
|![screenshot_2025-05-25_124639.png](/screenshot_2025-05-25_124639.png)|
| -- |

## Parcursul unui ambalaj prin cos

 Pentru inceput, este important sa se precizeze faptul ca cilindrul ocupa un volum adaptat pentru o sticla de 2L (aceasta reprezentand volumul maxim ce poate fi gazduit de catre ansamblu fara a exista riscul sa cedeze structura cosului din cauza greutatii excesive).
 
### 1.  CANTARUL
Cantarul are 2 roluri importante: masoara masa inregistrata de cantar periodic, găsind media intre valorile citite când nu este aruncat nimic în cos pentru o aproximație mai exacta a baseline ului la 0 load și fiind calculat dinamic media intre valorile citite când este introdus un ambalaj in cos. De asemenea, cantarul are rolul de a tine in loc ambalajul pentru a putea fi scanat, fiind actionat de un servo ce se poate deschide ca sa permita căderea produsului intr-unul dintre cele 4 compartimente. 

 La baza cantarului sta un loadcell, aflandu-se intr-o configuratie de parghie, in combinatie cu un amplificator digital hx711. De asemenea, in timp, in functie de locație, temperatura amplificatorului digital și stabilitatea tensiunii de linie, valoarea de baza a cantarului la load 0 poate varia cu timpul. Din acest motiv, loadcell ul nu poate fi folosit cu certitudine pe post de detector de proximitate, detecatand intratrea unui ambalaj in cos, acesta fiind dependent mecanic și fizic de multi parametrii. Totusi, stabilitatea sa este ridicata, din acest motiv el poate fi folosit ca sa măsoare masa cu precizie în momentul în care știm ca a fost ceva introdus in cos, valoarea de baza inițială fiind comparata cu valoarea medie inregistrata dupa introducerea în cos a produsului.
 
Pentru calcularea masei, un coeficient de calibrare este stabilita empiric prin pasarea unei greutăți de 100g în ansamblu și înregistrarea diferenței valorii de referinta. în funcție de aceasta diferența, se calculează m/dif pentru a stabili un coeficient ce este apoi transcris în cod.
|![screenshot_2025-05-25_131221.png](/screenshot_2025-05-25_131221.png)| ![load-cell-diagram-72.png](/load-cell-diagram-72.png)|
| -- | -- |

 [Mai multe detalii referitoare la functionarea unui load cell](https://learn.sparkfun.com/tutorials/getting-started-with-load-cells/all)
 
### 3. Detectorul de metale
 
1. Folosim un detector de metale custom format dintr-o bobina ce incojoara cilindrul.


##### Circuit custom de detectie metale

Circuitul consta dintr-un filtru LR highpass prin care trece un pulse train. Inductorul este format dintr-o bobina cu un diametru de aprox. 10-11cm si aprox. 50 de ture de cupru cu diametru de 0.4mm (L aprox.= 625 uH).
  Pe urma, semnalul trece printr-o dioda simpla de semnal la care este legat un condensator de poliester de 10nf.
  
  La introducerea unui obiect metalic in intriorul detectorului, inductanta fie scade, fie creste, caz in care valoarea de referinta de pe condensator de eprox. 530mV se va modifica. Precizia detectorului se bazeaza cel mai mult pe geometria ambalajului, nu pe masa acestuia sau grosimea materialului metalic. Astfel, pentru acuitate marita este nevoie ca linile campului magnetic sa fie perpendiculare pe suprafata metalica, o doza de aluminiu (grosime de aprox. 0.11mm) inregistrand de exemplu o valoare de cca. 500mV (diferenta de 30mV fata de valoarea de referinta), pe cand o greutate de 100g din aluminiu introdusa in cos, ce are o suprafata expusa detectorului mult mai mica comparativ cu suprafata dozei, inregistreaza o valoare de doar cca. 528mV (2mV diferenta).
  Amplificatorul digital folosit este tot hx711, fiind folosita setarea de gain de 32biti.

| ![schema circuitului](/aaa.webp) |

Din teste am observat urmatoarele valori:
 * Tensiune de referinta: 500.7mV
 * Tensiune de detectie: 529.7mV
 

  
Astfel, legand valoarea condensatorului la un amplificator digital, se poate obtine precizie mai mare pentru obiecte metalice mai mici si, de asemenea, se poate comunica valoarea mai departe raspberry pi-ului.
Avantajele detectorului sunt multe: precizie mai ridicata, comparativ cu senzorul inductiv, design mai compact, lipsa nevoii de a stii exact locatia ambalajului in cos etc.
Un dezavantaj ar fi riscul ca obiectul reciclat sa ramana blocat in cadrul detectorului, lucru ce a fost rezolvat din cod prin "impringerea" ambalajului in momentul soratrii de catre "falcile" ce suporta greutatea ambalajului. De asemenea, se poate mari usor diametrul detectorului si poate fi adaugat un fillet/chamber pe partea interioara pentru a putea impune ambalajului sa alunece/rastogoleasca in mmentul inclinarii cilindrului.
  
  
### 4. Cititorul de coduri de bare
  
  Va trebui testat un cititor de coduri de bare omnidireectional care sa poata citi codul de bare in tlap ce ambalajul se roteste, la o distanta relativ mica fata de ambalaj si in conditii de iluminiare led ce pot fi aranjate pentru o citire optima. De asemenea, cititorul va fi actionat de un servo sau un electromagnet cat sa dea sweep la toata suprafata ambalajului.
  
### 5. Lidar
  
  Urmeaz sa fie testat un lidar kic cu precizie de 64 de pixeli [VL53L7CX](https://www.robofun.ro/vl53l7cx-time-of-flight-8-8-zone-wide-fov-distance-sensor-carrier-with-voltage-regulator-350cm-max.html?gad_source=1&gad_campaignid=20383925641&gclid=Cj0KCQjw_dbABhC5ARIsAAh2Z-SsQSl8gLTzo1tBTG-PHYMbIrvgGt-ZnvaIW4blQK0FZV3CvSHxr8AaAv7REALw_wcB). Cu acest senzor se masoara dimensiunile ambalajului.

  ![drawing1.jpg](/drawing1.jpg)

note post teste: lidarul are suport doar pentru librărie de python și de c++, neexistând nici o librărie ce implementează pi4j. Din acest motiv, am înlocuit lidar ul cu un simplu senzor de distanta tof de la rev de 2m, acesta citind suficient de  precis distanta catre vârful ambalajului care sa nu afecteze detectie. in versiunile viitoare, codul va fi cel mai probabil rescris în c++ sau python, iar lidar ul va fi folosit în detrimentul senzorului de la rev pentru precizia sa mai ridicata de detectie.

Senzorul de distanta mai are și un al 2lea rol: acesta functioneaza și ca senzorul de proximitate. senzorul, fiind amplasat in partea superioara a cilindrului, la întrarea ambalajelor în ansamblu, este destul de sensibil la orice introducerea în cos al unui ambalaj, indiferent de mărimea acestuia, in cod valorile inregistrate de acest senzor fiind folosite pentru începerea procesului de detecție. De asemenea, daca ambalajul introdus este prea mic/usor pentru a putea fi detectat de alt senzor, înregistrarea intrarea unui astfel de ambalaj in ansamblu de catre senzorul tof permite sortarea acestuia în compartimentul de gunoaie menajere.

# Metoda de detectie

Senzorul de distanta va masura schimbarea valorii de referinta si raspberry pi-ul va incepe sa efectueze restul de teste.

Senzorul capacitiv de proximitate care se afla in contact cu ambalajul va avea, de asemenea, un rol in detectia lichidului in interiorul ambalajului, acesta fiind respins la menajere în cazul detectiei pozitive a lichidului. Senzorul capacitiv, pe scurt, masoara schimbarea constantei dielectrice din mediul înconjurător senzorului, acționând ca un switch atunci când aceasta valoare se schimba. lichidele, metalele și orice ambalaj conductiv poate fi detectat de senzor. v_out al senzorului este, initial, aproximativ 20V, egala cu valoarea voltajului furnizat de sursa (lrs 50-24 meanwell). Senzorul foloseste un optocuplor și câteva rezistoare pentru a schimba voltajul de ieșire de la 20v la 3.3v când e high, și aprox. 600mv low. Astfel, este folosit nivelul de voltaj logic necesar pentru detectia raspberry pi ului. Ambalajul este "împins" de senzor de 2 ori pentru a asigura un contact bun pentru detectia lichidului in ambalaj.

 Pe baza inaltimii inregistrate, se va stabili daca produsul este de tip sticla/pahar, sau daca este un ambalaj.
  
  
  Daca ambalajul este de tip sticla/pahar, atunci cosul va incepe sa actioneze rolele aflate pe partea inferioara a cilindrului, cititorul de coduri de bare incepand sa dea sweep la suprafata sticlei, citind un potential cod de bare aflat pe acesta. Daca exista un cod de bare, atunci el va fi cautat in baza de date publicata de returo pentru codurile de bare de tip EAN aflate in programul [SGR](https://returosgr.ro/sites/default/files/2023-11/Coduri-EAN-Registrul-Ambalajelor.pdf). Daca codul de bare se afla in sistem, atunci acesta poate fi numai de tip plastic, sticla sau metal. Avand metode de detectie precise atat pentru sticla cat si pentru metale, ambalajul poate fi numai de tip plastic. Aceasta metoda de detecție nu a fost implementata în prototip, dar va fi inclusa în următoarea versiune a proiectului.
  
De asemenea, daca codul de bare citit nu se afla dinainte in sistem, atunci dupa ce este stabilit materialul din care acesta este facut, se va adauga codul intr-o categorie separata, corespunzatoare materialului din care este facut ambalajul. Astfel, baza de date se poate extinde, permitand o sortare mai eficienta.
  
Avand atat masa produsului cat si inaltimea acestuia se va afla o constanta, `k = masa/inaltime (g/cm)`. Pentru ambalajele din sticla, k va fi mai mare decat pentru ambalaje de aceeasi inaltime. Astfel, sticla poate fi separata cu precizie de restul ambalajelor.

In acelasi timp, detectorul de metale va incepe sa functioneze, citind datele primite de la acesta. Daca valoarea inregistrata difera fata de valoarea de referinta, atunci ambalajul va fi categorisit ca fiind metal, fiind trimis in compartimentul de metale. Din fericire, atat senzorul inductiv cat si detector de metale poate diferentia atat metalele feroase, cat si cele neferoase, putand fii cu usurinta diferentiate.
  
Daca ambalajul nu este nici metal, nici sticla, iar ambalajul nu are un cod de bare corespunzator atunci, cantarul de va da in partea stanga aprox. 60 de grade pentru a permite produsului sa cada in interiorul structurii de sustinere

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
 
 1. Sturctura - suportul alb e done, trebuie aliniat servo in cadru
 ax rev cu 2 rulmenti in suport, ingropat in piesa portocalie.
 piesele porticalii sunt legate structural cu 2 profile extrudate 2020 in partea de sus
 tot caruciorul este rotit de un servo. D3e adaugat o rotata dintata sudata de carucior, care see cupleaza cu roata dintata din servo (1:1). In centrul rotii dintate iese un ax identic cu cel de jos si se sprijina in suportul de sus.
 rolele vor fi statice pentru primul prototip, separate fata de falci, cu prindere cu surub M3 in centru. Falcile vor fi prinse in carucior cu surub pe post de ax
 Falcile trebuie umplute pentru ca sunt foarte fragile. 
 De facut un triunghi din piese tetrix/rev care suporta cele doua parti
 Adaugat detectorul de cod de bare in pozitie statica
 
Estimat 1st proto: final de iunie
 