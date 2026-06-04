---
title: Workshop Requirements
description: This is a temporary page with instructions for the Software recruits regarding the workshops in the following week.
published: true
date: 2026-06-04T01:09:10.832Z
tags: 
editor: markdown
dateCreated: 2025-05-26T10:37:54.261Z
---

# Intro
Hello World! Va rugam, in zilele urmatoare, sa efectuati toate cerintele descrise mai jos, raportate la fiecare workshop.

**TERMEN LIMITA: 28 MAI 2025**

Dupa cum ati vazut si in afis, niste cerinte de baza ar fi:
 * Cunostinte de baza de C/C++ (functii, instructiuni de baza, if-else, while)
 * Laptop cu Windows 10/11 (sau Linux!) cu un port USB tip A disponibil si acces administrator (pentru instalarea Arduino IDE). 

# 28 MAI 2025 (14:30-15:30) -> Introducere

In aceasta zi va vom prezenta echipa, functiile acesteia, scopul, viziunea si asteptarile pe care le vom avea de la voi. Dupa prezentare, va putem ajuta sa va instalati soft-urile necesare.

# 29 MAI 2025 (15:00-19:00) -> Workshop Arduino
## Arduino IDE

Mergeti pe [pagina oficiala](), descarcati installer-ul penttru sistemul vostru de operare. Rulati-l cu optiunile default.

La prima pornire, va va cere instalarea a catorva drivere. Acceptati instalarea lor. 

Mentiune pentru utilizatorii de Linux! s ar putea sa nu aveti acces la port-urile necesare de upload. In acest caz executati in terminal: 
```bash
# pentru Debian, Ubuntu, RHEL, OpenSUSE, CentOS, Fedora
sudo usermod -a -G dialout `whoami`
# pentru Arch, Manjaro
sudo usermod -a -G uucp `whoami`

# dati un reboot ca sa se poata aplica schimbarile
sudo reboot
````

[Tutorial Step-byStep](https://randomnerdtutorials.com/programming-raspberry-pi-pico-w-arduino-ide/)



## Raspberry Pico

Deschideti Arduino IDE, mergeti la File -> Preferences si adaugatu urmatorul URL in `Additional baords manager URLs`:
```bash
https://github.com/earlephilhower/arduino-pico/releases/download/global/package_rp2040_index.json
```

Apasati OK. Deschideti board manager (iconita a 2-a din meniul din stanga) si scrieti in search box `pico`.
Instalati `Raspberry Pi Pico/RP2040/RP2350`.

## Cum configurez sa uploadez cod pe placa?

Vom face acest pasi impreuna in ziua workshop-ului.

Mergeti la Tools -> Board -> Raspberry Pi Pico/RP2040/RP2350 -> selectati Raspberry Pi Pico
Puneti placa in modul de programare: Apasati pe Reset(R) in timp ce tineti apasat butonul de Boot(B)
Selectati placa in Tools -> Port -> optiunea cu `UF2`
```
B. -> R. -> R^ -> B^
```
Apasati pe butonup de upload (Sageata orientata spre dreapta din stanga-sus a ferestrei)


## Java Development Kit

Mergeti pe [aceasta pagina](https://www.azul.com/downloads/?package=jdk#zulu) si descarcati installerul (din partea stanga).

In acest meniu al installer-ului, bifati `Set JAVA_HOME variable`:

![workshop-java-install.png](/Archive/Workshops/workshop-java-install.png)

Continuati cu optiunile default.

## IntelliJ IDEA IDE

Mergeti pe [aceasta pagina](https://www.jetbrains.com/idea/download/?section=windows), descarcati installer-ul pentru varianta Community (scrollati in jos! sectiunea cu fundal negru!)

Rulati installer-ul. Puteti modifica optiunile dupa cum va place.

## Simulatorul virtual_robot

Acesta este proiectul in care vom lucra in ultimul workshop. TBD



# 30 MAI 2025 (15:00-19:00) -> Simulator Autonomie FTC
