---
title: Smart Trashcan
description: 
published: true
date: 2025-05-27T18:25:03.355Z
tags: 
editor: markdown
dateCreated: 2024-11-11T20:49:35.696Z
---

# Descriere

Un cos de gunoi inteligent ce sorteaza intre patru ambalaje: metale, plastic, gunoi menajer si sticla.

Aparatul foloseste o combinatie de senzori plus citire de cod de bare pentru a putea determina materialul din care este facut obiectul

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
Cantarul are 3 roluri importante: masoara masa ambalajului introdus in cos, odata la fiecate 0.5s este verificata valoarea inregistrata de catre cantar,  verificand daca a fost introdus orice tip de obiect in cos si ultimul, tine in loc ambalajle pentru a putea fii testate si masurate.

 La baza cantarului sta un loadcell aflandu-se intr-o configuratie de parghie, in combinatie cu un amplificator digital hx711. Astfel, avand in vedere faptul ca tensiunea de linie poate varia cu timpul, sau din cauza imperfectiunilor componentelor electronice ce pot prezenta diferite variatii odata cu folosrea indelungata, la start-up se va stabili o valoare de referinta ce corespunde unui load=o, luand 6 valori inregistrate consecutiv de catre cantar si facand media aritmetica intre acestea.
 
 In momemntele in care nu este introdus niciun ambalaj in cos, se pot efectua mai multe astfel de calibrari pe parcursul zilei, avand astfel grija ca masa inregistrata de catre cos sa fie una corecta. De asemenea, se va gasi empiric un coeficient de calibrare a masei inregistrate pentru a putea compensa unghiul de 30 de grade la care este inclinat cosul.
|![screenshot_2025-05-25_131221.png](/screenshot_2025-05-25_131221.png)| ![load-cell-diagram-72.png](/load-cell-diagram-72.png)|
| -- | -- |

 [Mai multe detalii referitoare la functionarea unui load cell](https://learn.sparkfun.com/tutorials/getting-started-with-load-cells/all)
 
### 3. Detectorul de metale
 
Exista doua optiuni in aceasta privinta: 
1. Folosim un senzor inductiv de proximitate super PINDA 
2. Folosim un detector de metale custom format dintr-o bobina ce incojoara cilindrul.

##### Senzorul inductiv

Senzorul indcutiv este un senzor mic ce poate fi amplasat in partea inferioara a cilindrului, mai sus de buza cantarului

Astfel, in momentul cand o doza sau alt obiect metalic cade in interiorul cosului, senzorul detecteaza prezenta obiectului metalic, fie el feros sau neferos. Dezavantajul in aceasta abordare ar fi faptul ca senzorul este limitat sa se afle la o distanta mai mica de cca. 2.5mm fata de suprafata detectata, iregularitatile prezentate de forma ambalajelor putand reprezenta un factor critic ce trebuie luat in considerare pentru a elabora un design fiabil.
 
|![screenshot_2025-05-25_152142.png](/screenshot_2025-05-25_152142.png)|![da.jpg](/da.jpg)|
| -- | -- |


Din aceasta cauza, pentru a avea siguranta ca senzorul este suficient de aproape de ambalaj trebuie implementat un servo lineat de care este legat senzorul, putand fi miscat cativa centimetri in sus pentru a lovi ambalajul si a-l impunge, asigurand o detectie sigura. Din cauza dimensiunii unui astfel de servo, design-ul nu este usor de implementat pentru a acomoda o astfel de schimbare. De asmenea, din cauza rigiditatii cablului senzorului inductiv, acesta nu se poate plasa in centrul cilindrului fara a se lovi de axul pe care este sprijinit cilindrul. Din cauza asta, ar trebui lungit corpul de sprijin al cilindrului, cat si distanta de la ax la baza inferioara a cilindrului. Pentru un design simplist, se poate introduce senzorul in interiorul cadrului ce sprijina falice, precum si restul ansamblului, nefiind folosit vreun servo in plus sau fiind nevoie de modificare dimensiunilor cilindrului. Totusi, nu poate fi garantata precizia detectiei pentru metale. 

[Datasheet senzor](https://files.pepperl-fuchs.com/webcat/navi/productInfo/pds/70134664_eng.pdf)


##### Circuit custom de detectie metale

Circuitul consta dintr-un filtru LR highpass prin care trece un pulse train. Inductorul este format dintr-o bobina cu un diametru de aprox. 10-11cm si aprox. 50 de ture de cupru cu diametru de 0.4mm (L aprox.= 625 uH).
  Pe urma, semnalul trece printr-o dioda simpla de semnal la care este legat un condensator de poliester de 10nf.
  
  La introducerea unui obiect metalic in intriorul detectorului, inductanta fie scade, fie creste, caz in care valoarea de referinta de pe condensator de eprox. 530mV se va modifica. Precizia detectorului se bazeaza cel mai mult pe geometria ambalajului, nu pe masa acestuia sau grosimea materialului metalic. Astfel, pentru acuitate marita este nevoie ca linile campului magnetic sa fie perpendiculare pe suprafata metalica, o doza de aluminiu (grosime de aprox. 0.11mm) inregistrand de exemplu o valoare de cca. 500mV (diferenta de 30mV fata de valoarea de referinta), pe cand o greutate de 100g din aluminiu introdusa in cos, ce are o suprafata expusa detectorului mult mai mica comparativ cu suprafata dozei, inregistreaza o valoare de doar cca. 528mV (2mV diferenta).

| ![schema circuitului](/aaa.webp) |

Din teste am observat urmatoarele valori:
 * Tensiune de referinta: 500.7mV
 * Tensiune de detectie: 529.7mV
 

  
Astfel, legand valoarea condensatorului la un amplificator digital, se poate obtine precizie mai mare pentru obiecte metalice mai mici si, de asemenea, se poate comunica valoarea mai departe raspberry pi-ului.
Avantajele detectorului sunt multe: precizie mai ridicata, comparativ cu senzorul inductiv, design mai compact, lipsa nevoii de a stii exact locatia ambalajului in cos etc.
Un dezavantaj ar fi riscul ca obiectele reciclate sa ramana blocate in cadrul detectorului, lucru ce poate fi rezolvat prin compactarea inductorului intr-un disc cu inaltime mai mica, mai compact, pastrand precizia detectorului. De asemenea, se poate mari usor diametrul detectorului si poate fi adaugat un fillet/chamber pe partea interioara pentru a putea impune ambalajului sa alunece/rastogoleasca in mmentul inclinarii cilindrului.
  
  Analizand aceste optiuni cu tot cu avantaje si cu dezavantaje, cred ca este mai usor si mai fiabil sa se implementeze detectorul de metale custom in detrimentul senzorului inductiv.
  
### 4. Cititorul de coduri de bare
  
  Va trebui testat un cititor de coduri de bare omnidireectional care sa poata citi codul de bare in tim ce ambalajul se roteste, la o distanta relativ mica fata de ambalaj si in conditii de iluminiare led ce pot fi aranjate pentru o citire optima. De asemenea, cititorul va fi actionat de un servo sau un electromagnet cat sa dea sweep la toata suprafata ambalajului.
  
### 5. Lidar
  
 Urmeaz sa fie testat un lidar kic cu precizie de 64 de pixeli [VL53L7CX](https://www.robofun.ro/vl53l7cx-time-of-flight-8-8-zone-wide-fov-distance-sensor-carrier-with-voltage-regulator-350cm-max.html?gad_source=1&gad_campaignid=20383925641&gclid=Cj0KCQjw_dbABhC5ARIsAAh2Z-SsQSl8gLTzo1tBTG-PHYMbIrvgGt-ZnvaIW4blQK0FZV3CvSHxr8AaAv7REALw_wcB). Cu acest senzor se masoara dimensiunile ambalajului.

  ![drawing1.jpg](/drawing1.jpg)


# Metoda de detectie

Pentru a limita curentul consumat de catre cos, singurul senzor functional in permanenta va fi cantarul. Astfel, in momentul in care este introdus un ambalaj in anasamblu, cantarul va masura schimbarea valoarei de referinta si raspberry pi-ul va incepe sa efectueze restul de teste.

Lidar-ul va incepe sa masoare distanta de la senzor la ambalaj, fiind astfel calculata inaltimea ambalajului. Precizia lidar-ului este suficient de satisfacatoare cat o variatie de cativa centimetri sa nu afecteze performanta cosului. De asmenea, se va efectua media aritmetica intre cateva valori consecutive pentru a scadea eroarea introdusa de catre senzor. Pe baza inaltimii inregistrate, se va stabili daca produsul este de tip sticla/pahar, sau daca este un ambalaj.
  
  
  Daca ambalajul este de tip sticla/pahar, atunci cosul va incepe sa actioneze rolele aflate pe partea inferioara a cilindrului, cititorul de coduri de bare incepand sa dea sweep la suprafata sticlei, citind un potential cod de bare aflat pe acesta. Daca exista un cod de bare, atunci el va fi cautat in baza de date publicata de returo pentru codurile de bare de tip EAN aflate in programul [SGR](https://returosgr.ro/sites/default/files/2023-11/Coduri-EAN-Registrul-Ambalajelor.pdf). Daca codul de bare se afla in sistem, atunci acesta poate fi numai de tip plastic, sticla sau metal. Avand metode de detectie precise atat pentru sticla cat si pentru metale, ambalajul poate fi numai de tip plastic.
  
De asemenea, daca codul de bare citit nu se afla dinainte in sistem, atunci dupa ce este stabilit materialul din care acesta este facut, se va adauga codul intr-o categorie separata, corespunzatoare materialului din care este facut ambalajul. Astfel, baza de date se poate extinde, permitand o sortare mai eficienta.
  
Avand atat masa produsului cat si inaltimea acestuia se va afla o constanta, `k = masa/inaltime (g/cm)`. Pentru ambalajele din sticla, k va fi mai mare decat pentru ambalaje de aceeasi inaltime. Astfel, sticla poate fi separata cu precizie de restul ambalajelor.

In acelasi timp, detectorul de metale va incepe sa functioneze, citite datele primite de la acesta. Daca valoarea inregistrata difera fata de valoarea de referinta, atunci ambalajul va fi categorisit ca fiind metal, fiind trimis in compartimentul de metale. Din fericire, atat senzorul inductiv cat si detector de metale poate diferentia atat metalele feroase, cat si cele neferoase, putand fii cu usurinta diferentiate.
  
Daca ambalajul nu este nici metal, nici sticla, iar ambalajul nu are un cod de bare corespunzator atunci, cantarul de va da in partea stanga aprox. 60 de grade pentru a permite produsului sa cada in interiorul structurii de sustinere

![screenshot_2025-05-25_135908.png](/screenshot_2025-05-25_135908.png)

In interior se va afla o pereche de perii/rotite ce au rolul sa preseze usor ambalajul. Un microfon aflat in partea superioara a structurii de sustinere va recepta sunetul produs. Pe urma, cu ajutorul unei librarii de python va fi efectuata o analiza fourier a sunetului (fft), fiind astfel diferentiate sunetele produse de ambalaje din carton fata de ambalaje din pastic. Cartonul produce un sunet de intensitate mai mica si frecventa mai joasa, pe cand plasticul produce un sunet mai intens si de frecenta mai inalta, astfel reprezentand o metoda ce merita explorata si posibil implementata pentru sortarea plasticului vs cartonului.

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
 