---
title: Smart Trashcan
description: 
published: true
date: 2026-01-12T02:38:14.763Z
tags: mechanics, 3dprinting, project, davidcore
editor: markdown
dateCreated: 2024-11-11T20:49:35.696Z
---

# Descriere

Coșul de gunoi inteligent WALLE_E smart trashcan este un dispozitiv modern capabil să sorteze automat patru tipuri de ambalaje:

* metale – doze și conserve,

* plastic – sticle și ambalaje SGR,

* deșeuri menajere,

* sticlă – recipiente din sticlă.

Funcționarea sa nu necesită intervenție umană, aparatul utilizând o combinație de senzori pentru a identifica tipul de material introdus.

Dispozitivul asigură o detecție rapidă și precisă, contribuind la o reciclare eficientă a mai multor ambalaje într-un timp redus.
Datorită designului compact, coșul poate fi atașat unui recipient de gunoi tetracameral cu modificări minime, oferind o soluție practică și inteligentă pentru gestionarea deșeurilor.

| ![screenshot_2025-05-25_140819.png](/screenshot_2025-05-25_140819.png) |
| -- |


# Obiective

* Dezvoltarea unui coș de gunoi compact și inteligent, adaptat pentru utilizarea în spații publice, birouri, plaje sau ansambluri rezidențiale, cu scopul de a eficientiza procesul de reciclare și de a economisi timp.

* Promovarea unui comportament responsabil față de mediu și reducerea nivelului de poluare.

* Reciclarea ambalajelor generate în cadrul atelierului și crearea unei baze de date care monitorizează tipurile și cantitățile de materiale reciclate.


# Constructie

Dispozitivul este alcătuit dintr-un cilindru rotativ înclinat la 30°, integrat într-un coș de gunoi compartimentat în patru camere de depozitare, dispuse pe diagonalele structurii. Gura de acces poate fi rotundă sau pătrată, în funcție de spațiul de amplasare și de preferințele de design.

Prin designul său modular și compact, proiectul funcționează ca un accesoriu inteligent și adaptabil, ce poate fi integrat cu ușurință în diverse medii — de la spații publice și birouri până la zone rezidențiale.
  
![proiect_walle.jpg](/proiect_walle.jpg)

## Parcursul unui ambalaj prin cos

 Pentru inceput, este important sa se precizeze faptul ca cilindrul ocupa un volum adaptat pentru o sticla de 2L (aceasta reprezentand volumul maxim ce poate fi gazduit de catre ansamblu fara a exista riscul sa cedeze structura cosului din cauza greutatii excesive).
 
### 1.  SISTEMUL DE CANTARIRE
Cântarul integrat îndeplinește trei funcții esențiale:

detectarea introducerii ambalajului, activând procesul de analiză;

măsurarea masei obiectului;

stabilizarea ambalajului pe durata procesului de scanare, până la direcționarea acestuia către compartimentul corespunzător.

Mecanismul de cântărire este bazat pe un senzor de sarcină (load cell) configurat sub formă de pârghie, conectat la un amplificator digital HX711.
Prin variația rezistenței electrice generate la aplicarea unei forțe, sistemul convertește valoarea acesteia în unități de masă, oferind o citire precisă și stabilă.
 
|![screenshot_2025-05-25_131221.png](/screenshot_2025-05-25_131221.png)| ![load-cell-diagram-72.png](/load-cell-diagram-72.png)|
| -- | -- |

 [Mai multe detalii referitoare la functionarea unui load cell](https://learn.sparkfun.com/tutorials/getting-started-with-load-cells/all)
 
### 3. Detectorul de metale
 
1. Sistemul utilizează un detector de metale personalizat, constând într-o bobină care înconjoară cilindrul coșului.

### Circuit de detecție metale

Detectorul se bazează pe un filtru LR high-pass (L – inductor, R – rezistor), alimentat cu un semnal AC de aproximativ 10 kHz.
Inductorul este o bobină cu diametru de 10–11 cm, formată din aproximativ 100 de spire de cupru de 0,4 mm (inductanță ≈ 625 μH).

Semnalul indus trece printr-o diodă de semnal, urmată de un condensator de poliester de 100 nF, care stabilește valoarea de referință a tensiunii (aprox. 530 mV).

Introducerea unui obiect metalic modifică inductanța bobinei, determinând schimbarea tensiunii pe condensator. Detectorul se bazează mai ales pe forma ambalajului, nu pe greutatea sau grosimea materialului. Pentru precizie sporită, câmpul magnetic trebuie să fie perpendicular pe suprafața metalică.

Această configurare permite sortarea corectă a ambalajelor de aluminiu considerate „gunoi menajer”, fără a le confunda cu dozele metalice.

Amplificatorul digital HX711 este utilizat pentru măsurători, cu un gain de 32 biți, asigurând o detecție precisă.

|![schema circuitului](/aaa.webp)| ![detectormetale_walle.jpg](/detectormetale_walle.jpg)|
| -- | -- |
   
### 5. Lidar
  
  Urmeaza sa fie testat un modul lidar cu precizie de 64 de pixeli [VL53L7CX](https://www.robofun.ro/vl53l7cx-time-of-flight-8-8-zone-wide-fov-distance-sensor-carrier-with-voltage-regulator-350cm-max.html?gad_source=1&gad_campaignid=20383925641&gclid=Cj0KCQjw_dbABhC5ARIsAAh2Z-SsQSl8gLTzo1tBTG-PHYMbIrvgGt-ZnvaIW4blQK0FZV3CvSHxr8AaAv7REALw_wcB). Cu acest senzor se masoara dimensiunile ambalajului.

  ![drawing1.jpg](/drawing1.jpg)

**Note post-teste:**

Lidarul utilizat are suport doar pentru librării Python și C++, neexistând nicio librărie care să implementeze Pi4J. Din acest motiv, am înlocuit lidarul cu un senzor de distanță TOF de la REV, cu rază de acțiune de 2 m. Acesta măsoară suficient de precis distanța până la vârful ambalajului, fără a afecta procesul de detecție.

În versiunile viitoare, codul va fi cel mai probabil rescris în C++ sau Python, iar lidarul va fi folosit în locul senzorului TOF, pentru precizia mai ridicată a detecției.

**Roluri senzor TOF:**

Senzorul de distanță are și un al doilea rol: funcționează și ca senzor de proximitate. Amplasat în partea superioară a cilindrului, la intrarea ambalajelor, senzorul detectează introducerea oricărui obiect în coș, indiferent de dimensiune. Valorile înregistrate de senzor sunt folosite în cod pentru a iniția procesul de detecție.

De asemenea, dacă ambalajul introdus este prea mic sau ușor pentru a fi detectat de alt senzor, semnalul generat de TOF permite sortarea acestuia în compartimentul de gunoi menajer.

### 5. Senzor capacitiv de proximitate
Acest senzor are rolul de a detecta prezența lichidelor în interiorul ambalajelor. Procesul este automatizat, astfel încât, după ce se stabilește că ambalajul este de tip „sticlă”, ansamblul începe să impungă sticla, pentru a facilita contactul dintre senzor și ambalaj.

În cazul în care este detectat lichid în interiorul sticlei, aceasta este direcționată imediat către compartimentul de gunoi menajer, fără a fi nevoie de intervenție manuală. Cu toate acestea, pentru o reciclare cât mai corectă, utilizatorii vor fi rugați să scoată orice lichid din sticle înainte de introducerea acestora în ansamblu.

Senzorul capacitiv funcționează prin detectarea schimbării indicelui dielectric din mediul înconjurător. Materialele conductive, precum metalele sau apa, au o constantă dielectrică mult mai ridicată, ceea ce permite senzorului să identifice prezența lichidului.

**Notă tehnică:**

* V_out inițial al senzorului: aproximativ 20 V, egal cu tensiunea furnizată de sursa LRS-50-24 Meanwell.

* Senzorul utilizează un optocuplor, semnalul de intrare fiind furnizat de output-ul senzorului capacitiv (0/20 V).

* Semnalul trece printr-o configurație simplă cu tranzistor NPN, alimentat cu Vcc = 3,3 V (asigurat de Raspberry Pi), ceea ce permite obținerea unui nivel de ieșire sigur de 0/3,3 V, compatibil cu GPIO-urile plăcii de dezvoltare.

|![051135_5_522_1024x1024.webp](/051135_5_522_1024x1024.webp)|![whatsapp_image_2025-11-02_at_18.25.12_2e654ebd.jpg](/whatsapp_image_2025-11-02_at_18.25.12_2e654ebd.jpg)|
| -- | -- |
	

# Metoda de detectie

  Cântarul măsoară schimbarea treptată a valorii de referință în momentul introducerii unui obiect în ansamblu. În acest fel sunt evitate măsurătorile false aproape de zero sau schimbările bruște, care pot fi cauzate fie de introducerea unui ambalaj cu masă mare, fie de variații tranzitorii ale tensiunii sursei. Aceste variații sunt verificate de două ori pentru a stabili natura lor.

Schimbările relativ mici, sub un prag stabilit empiric, sunt considerate rezultatul introducerii unor ambalaje ușoare, precum șervețele sau hârtie mototolită. Acestea sunt detectate imediat și trimise mai departe prin circuitul de scanare.

În continuare, este măsurată înălțimea ambalajului, pentru a determina dacă acesta este de tip menajer (ambalaje ușoare: hârtie mototolită, șervețel, celofan) sau sticlă (doze, sticlă de sticlă/plastic etc.).

Dacă înălțimea ambalajului este sub un prag de aproximativ 40 mm, acesta este sortat automat la gunoi menajer.

Altfel,  *procesul de scanare continuă*.

În același timp, este măsurată masa ambalajului și este pusă în raport cu înălțimea acestuia, calculându-se o constantă:

Această constantă ajută la determinarea naturii ambalajului:

Ambalajele mai grele, precum sticlele de sticlă, au valori mai mari ale lui k, comparativ cu sticlele de plastic sau ambalajele din carton.

Pragul numeric empiric, T, stabilit după multiple teste, este egal cu 0,5.

**Intervale tipice pentru k:**

* Sticle de plastic: 0,15 – 0,3

* Sticle de sticlă: 0,7 – 2,5

* Ambalaje menajere: < 0,1

* Ambalaje cu lichid plin: > 2,5 (sunt sortate automat la menajere)

Astfel, sistemul poate să sorteze cu precizie sticlele de sticlă față de alte materiale și să elimine corect ambalajele ușoare sau pline cu lichid.


|![chatgpt_image_nov_2_2025_07_01_45_pm.png](/chatgpt_image_nov_2_2025_07_01_45_pm.png)|![chatgpt_image_nov_2_2025_07_13_04_pm.png](/chatgpt_image_nov_2_2025_07_13_04_pm.png)|
| -- | -- |


”

În același timp, detectorul de metale începe să funcționeze, citind datele primite. Dacă valoarea înregistrată diferă de valoarea de referință, ambalajul este clasificat ca metalic și trimis în compartimentul corespunzător. Atât senzorul inductiv, cât și detectorul de metale pot diferenția metalele feroase de cele neferoase, fiind astfel ușor de identificat.

* Dacă ambalajul este menajer, cântarul se rotește aproximativ 60° spre stânga, pentru ca produsul să cadă în interiorul structurii de susținere.

* Dacă ambalajul este sticlă, cilindrul se rotește 90° spre stânga, în timp ce falcile acționează pentru a împinge și depozita obiectul.

* Dacă ambalajul este metal (doză), cilindrul se rotește 90° spre dreapta pentru a sorta ambalajul în compartimentul destinat metalelor.

* Dacă ambalajul este sticlă de plastic, falcile ce susțin obiectul se deschid, lăsând ambalajul să cadă în interior.
![screenshot_2025-05-25_135908.png](/screenshot_2025-05-25_135908.png)

  
|![screenshot_2025-05-25_141411.png](/screenshot_2025-05-25_141411.png)|![screenshot_2025-05-25_141800.png](/screenshot_2025-05-25_141800.png)|
| -- | -- |
  




# Folosirea optimizarii topologice in design
Piciorul de susținere a fost optimizat topologic, utilizând uneltele de simulare din Fusion 360, pentru a reduce masa și a obține rezistența structurală maximă.


|![screenshot_2025-05-13_202210.png](/screenshot_2025-05-13_202210.png)|![screenshot_2025-05-25_161333.png](/screenshot_2025-05-25_161333.png)|![screenshot_2025-05-25_161348.png](/screenshot_2025-05-25_161348.png)|
| -- | -- | -- |

Aceasta structura, comparativ cu piciorul de raft din [proiectul de cercetare](https://wiki.teamclockworks.ro/en/Projects/optimizare-topologica) pentru tool-ul de optimizare, a fost creat folosind metoda 2.
 Astfel, in urma efectuarii si repetarii simularilor, piesa originala a fost modificata pentru a putea beneficia atat de o printabilitate mai usoara, cat si de avntajele obtinute prin reducerea masei piesei, in cazul modelelor mari, tool-ul putand fi de ajutor pentru a reduce cantitatea de filament folosit.
 
 
 # In context social
 
 Echipa noastră, Clockworks, promovează conștientizarea importanței protecției mediului, dezvoltând proiecte precum WALLE_E Smart Trashcan pentru a genera un impact real atât în comunitate, cât și în mediul STEM. „Viitorul se scrie prin ideile tale. Transformă‑le în soluții care contează și lasă‑ți amprenta asupra generației tale.” Această viziune devine concretă prin proiecte care transformă tehnologia într-un aliat al planetei, reducând poluarea și încurajând reciclarea responsabilă.

Viziune și integrare în comunități
Proiectul WALLE_E poate fi integrat în spații rezidențiale sau publice, cu scopul de a limita poluarea mediului, în special în zone unde reciclarea conștientă nu este încă posibilă. Imaginează-ți un complex rezidențial în care locatarii aruncă ambalajele într-un coș inteligent, iar acestea sunt sortate automat și eficient – reducând risipa, economisind timp și resurse.
La o scară mai largă, proiectul poate atinge o performanță satisfăcătoare, similară cu cea a echipamentelor RVM utilizate de companii consacrate, însă la un nivel mai mic, care are potențial de creștere în viitor. Această flexibilitate face ca sistemul să fie accesibil și scalabil, oferind o alternativă practică pentru comunități și spații rezidențiale, cu posibilitatea de a fi îmbunătățit și extins pe măsură ce tehnologia și cerințele comunității evoluează.
Mai mult, spre deosebire de sistemele actuale care acceptă doar anumite tipuri de ambalaje, WALLE_E are potențialul de a sorta orice tip de material – plastic, metal, sticlă sau gunoi menajer – crescând semnificativ gradul de reciclare și flexibilitatea implementării.

Context european și relevanță
În Europa, studiile arată că schemele de returnare a ambalajelor (DRS) cresc considerabil ratele de reciclare: în Germania, de exemplu, 98% dintre recipiente sunt colectate prin astfel de programe, în timp ce media de reciclare a deșeurilor municipale în UE este sub 50%. Aceasta evidențiază potențialul major de creștere și necesitatea unor soluții inovative la nivel local.
Proiectul WALLE_E Smart Trashcan se înscrie direct în acest context, oferind o soluție descentralizată, accesibilă și eficientă, care poate sprijini comunitățile în atingerea unor rate de reciclare similare cu cele ale programelor industriale, dar într-un mod integrat, educativ și prietenos cu utilizatorul.

Impactul asupra mediului și comunității
Prin utilizarea WALLE_E, impactul proiectului este multiplu:


Reducerea deșeurilor care ajung la groapa de gunoi sau sunt incinerate, protejând mediul înconjurător;


Creșterea gradului de reciclare în spații publice și rezidențiale, unde infrastructura tradițională este limitată;


Educație și responsabilizare – fiecare ambalaj introdus devine un act de conștientizare și implicare;


Accesibilitate economică – un sistem inteligent cu cost redus comparativ cu aparatura industrială;


Scalabilitate reală – de la un bloc, la un cartier sau comunitate extinsă, proiectul poate fi multiplicat rapid și eficient.


Prin aceste beneficii, WALLE_E nu doar facilitează reciclarea, ci și creează o cultură a responsabilității ecologice, influențând pozitiv comportamentul comunităților și generând un impact durabil.

Concluzie
WALLE_E Smart Trashcan demonstrează că tehnologia poate transforma reciclarea dintr-o obligație într-o experiență integrată și responsabilă, care să devină parte din viața cotidiană. Acest proiect combină:


Inovație tehnologică – sortare inteligentă a ambalajelor;


Impact ecologic – reducerea deșeurilor și protecția mediului;


Rol educativ – stimularea unui comportament responsabil;


Eficiență economică – accesibilitate și scalabilitate.


Proiectul arată că protecția mediului poate fi realizată cu mijloace inteligente, eficiente și accesibile, demonstrând că fiecare ambalaj sortat corect reprezintă un pas către un viitor mai verde și sustenabil.

Viitorul nu este predestinat. El se construiește prin ideile și acțiunile noastre, prin soluții care contează și prin amprenta pe care alegem să o lăsăm generațiilor viitoare.

 # Urmatorii pasi
 
* (versiuni viitoare:) In interior se va afla o pereche de perii/rotite ce au rolul sa preseze usor ambalajul. Un microfon aflat in partea superioara a structurii de sustinere va recepta sunetul produs. Pe urma, cu ajutorul unei librarii de python va fi efectuata o analiza fourier a sunetului (fft), fiind astfel diferentiate sunetele produse de ambalaje din carton fata de ambalaje din pastic. Cartonul produce un sunet de intensitate mai mica si frecventa mai joasa, pe cand plasticul produce un sunet mai intens si de frecenta mai inalta, astfel reprezentand o metoda ce merita explorata si posibil implementata pentru sortarea plasticului vs cartonului.

* In cazul in care ambalajul este de tip carton, acesta va fi trecut mai departe prin perii, fiind sortat in compartimentul pentru gunoaie menajere. Sticla, fiind mai rezistenta, va cadea in interiorul cilindrului, "falcile" ce mentin structura deschizandu-se la 45 de grade fiecare pentru a permite ca ambalajul sa cada in interior. Astfel, periile nu trebuie sa aiba putere foarte mare, acestea presand doar usor ambalajul.
 