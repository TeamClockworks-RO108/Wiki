---
title: Workshop Programare
description: 
published: true
date: 2026-06-04T01:09:08.987Z
tags: 
editor: markdown
dateCreated: 2025-04-29T20:20:18.524Z
---

# Programare


Program:
25 Mai - Deadline formular inscriere
28 Mai, Liceul Sincai, Ora 14:30-15:30 - Prezentarea echipei si a concursului
29 Mai, Atelier Clockworks, Ora 15:00-19:00 - Workshop programare Arduino
30 Mai, Atelier Clockworks, Ora 15:00-19:00 - Workshop programare FTC in simulator virtual

Atelierul Clockworks este situat in incinta cladirii ICPE, etaj 3. In zilele de workshop, ne vom intalni intre ora 15:00 si 15:15 la receptia cladirii ICPE.

Formular: https://docs.google.com/forms/d/e/1FAIpQLSfUUuDzVNZZBCBtwiiLE_ph4vlG7i90e13gFdcmk43_eMpObA/viewform?usp=dialog

Capacitate maxima: 12 persoane (in ziua 2 se lucreaza in echipe de 2).

## Requirements
 * Cunostinte de baza de C/C++ (functii, instructiuni de baza, if-else, while)
 * Laptop cu Windows 10/11 (sau Linux!) cu un port USB tip A disponibil si acces administrator (pentru instalarea Arduino IDE). La nevoie, putem oferi o singura statie de lucru daca cineva nu are. 

## Materiale
Avem piese cat de 6 rig-uri  
 * 6 GroundStudio Jade Pico (comandate)
 * 12 Servomotoare SG90 (comandate)
 * 12 butoane simple (de mers la Conex si luat de acolo)

De proiectat un mic rig cu extensie linara si un claw 

## Day 1

Introducere
Prezentare(max 1h) in care prezentam echipa, FTC, viziunea nostra. 

## Day 2

Workshop in mediul Arduino in care participantii vor invata sa controleze un robot format din:
 * 1 Buton
 * 2 Servomotoare (Gripper + extensie liniara, glisiera)
 * RPi Pico 

Ne vedem toti la receptie - 15:00 - 15:15. Urcam sa facem atelierul. 
Incheiem ideal la 19:00.
Pauza de relaxare (20 de min) - 16:30 -> 17:00. Va comanda Alex pizza inainte sa ajunga lumea ca sa fie disponibila in caz de foame. 


### Condfiguratie hardware

| Device | Pin  | 
| ------ | ---- |
| Buton  | 12   |
| Servo  | 21   |
| LED    | 25   |
| XBee Receive (DOUT)  | 5 |
| XBee Transmit (DIN) | 4 |

Baud rate XBee: `9600`

## Cum configurez sa uploadez cod pe placa?

Vom face acest pasi impreuna in ziua workshop-ului.

Mergeti la Tools -> Board -> Raspberry Pi Pico/RP2040/RP2350 -> selectati Raspberry Pi Pico
Puneti placa in modul de programare: Apasati pe Reset(R) in timp ce tineti apasat butonul de Boot(B)
Selectati placa in Tools -> Port -> optiunea cu `UF2`
```
B. -> R. -> R^ -> B^
```
Apasati pe butonup de upload (Sageata orientata spre dreapta din stanga-sus a ferestrei)


#### Structura unui program pe Arduino

Vom scrie 2 functii asemanatoare functiei principala `main` cu care sunteti familiari: `setup` si `loop`. Prima ruleaza o singura data, cand porneste placa. Functia `loop` este apelata la infinit, pana cand placa este oprita (ramane fara alimentare - nu exista "oprirea" programului).

```arduino

void setup() {
	// Code that runs once, at the start of the program
}

void loop() {
	// This function runs indefinetely until power is turned off
}

```


#### Cum citim un buton?

```arduino
// In setup, daca butonul se afla pe pinul 3:
pinMode(3, INPUT_PULLUP);

// In loop
// Observati negatia (!): Butonul este legat a.i. valoarea data este negata, iar noi facem dubla negatie!
boolean value = !digitalRead(12);
// Acum putem lua decizii pe baza variabilei value
```

#### Cum scriem valoarea unui led?

```arduino
// In setup, daca led-ul se afla pe pinul 3:
pinMode(3, OUTPUT);

// In loop
boolean value = true; // Inlocuiti cu o valoare calculata in functie de cerintele voastre
digitalWrite(3, value);

// Sau, valori hardcodate:
digitalWrite(3, true);
digitalWrite(3, false);
```

#### Cum astept un timp, urmand ca dupa sa fac alta actiune?

Pentru a astepta, folosim functia `delay`, specificand timpul in milisecunde (1000ms = 1s). Exemplul urmator porneste un led, asteapta 1 secunda, dupa il stinge. 

```arduino
digitalWrite(3, true);
delay(1000);
digitalWrite(3, false);

```

#### Cum comandam un servo?

```arduino
// Includem libraria de servo
#include <Servo.h>

// Declaram global un obiect de tip servo
Servo myservo; 

// In setup, daca servo-ul este pe pinul 3:
myservo.attach(3);

// In loop
// Valorile pe care le putem comanda pe servo sunt numere intregi de la 0 la 180
myservo.write(30);

// Dam si alta comanda
myservo.write(150);
```

#### Cum comunic pe o retea XBee?

```arduino
// Includem libraria necesara
#include <SoftwareSerial.h>

// Creem un obiect global cu parametrii: pin receptie, pin transmisie
SoftwareSerial xbee(5, 4);

// In setup, pornim portul de transmisie si specificam rata de transmisie
xbee.begin(9600);

// In loop (sau unde avem nevoie)
// Transmitem o linie de date
xbee.println("Hello from the other side")

// Cum citim?
xbee.available() // ne spune daca avem caractere in coada de citire
xbee.read() // citeste un caracter (char) si il elimina din coada de citire
// Vedem mai jos cum compunem functiile astea doua sa citim linii intregi
```

#### Cum afisez date pe consola?

Ca sa deschidem consola, apasam pe iconita dreapta-sus ce are o lupa pe ea.

```arduino
// In setup, initializam consola cu viteza de transmisie
Serial.begin(9600);

// Oriunde dupa initializare, putem afisa:
int value = 53;
Serial.print("Valoarea este: ")
Serial.println(value);
```

#### Cum citesc linii primite de la consola sau alta conexiune seriala?

Putem citi linii intregi de pe orice conexiune seriala:
* Consola (`Serial`)
* XBee (`xbee`, de tip `SoftwareSerial`)

Trebuie sa citim caracter cu caracter, sa acumulam intr-un array si cand primim `\n` sau `\0` sa incheiem linia.

```arduino
// declaram un array de caractere si o variabile in care contorizam cate caractere am primit
// totul global
char recvString[100];
int recvLength = 0;

// In loop
while (Serial.available) {
	char c = xbee.read(); // Citim urmatoarul caracter
  if (c == '\n') c == 0; // Inlocuim newline cu null, pentru a termina string-ul
  recvString[recvLength++] = c; // Adaugam caracterul la string
  if (c == 0) {
  	// Daca c este null, inseamna ca s-a primit toata linia. Putem procesa inputul:
    if (!strcmp(recvString, "off") { /* fa ceva! */ }
    if (!strcmp(recvString, "on") { /* fa ceva! */ }
    recvLength = 0; // Resetam pentru citirea urmatoarei linii
  }
}
```

> Daca folosim `delay` in interiorul functiei `loop`, sectiunea de citit linii din conexiunea seriala poate **pierde** caractere deoarece dimensiunea buffer-ului intern este extrem de mica! Trebuie sa facem temporizari fara `delay`!
{.is-danger}


#### Cum temporizez actiuni fara sa blochez bucla?

```arduino
// Folosim o variabila globala in care pastram momentul de la care incepe temporizarea
unsigned long previousMillis = 0;

// In loop
// Obtinem timpul curent cu functia millis()
unsigned long currentMillis = millis();

// Verificam daca timpul a expirat
if (currentMillis - previousMillis >= 1000) {
	// Daca vrem ca temporizarea sa se intample la infinit, resetam
  previousMillis = currentMillis;
  // Daca vrem sa se intample doar o data, setam previousMillis la valoarea de overflow (-1)
  
  // Facem actiunea
  digitalWrite(3, true);
}
```

### Cunostinte invatate:
 * Led (`digitalWrite`)
 * Servo
 * Butoane (`INPUT_PULLUP`, `digitalRead`)
 * Topoligii de a scrie codul (cu delay...) 

## Day 3

Vom lucra intr-un simulator de robot care ne permite sa programam in java cu API-ul de FTC.
Simulatorul se gaseste [aici](https://gitlab.com/clockworks2/virtual_robot). Vor avea nevoie sa aiba instalat IntelliJ IDEA Community Edition si o versiune de java 11+.


Robot TankDrive (tip hardware Arm Bot)
Ce le dam sa faca:
1. Sa faca o navigatie autonoma, bazata pe timp.
2. Sa actioneze servo uri de pe robot si sa preia un game element etc.


## Day 4+
Interviuri de feedback online (telefon sau discord... TBD)



## Altele

#### Testbench gripper

```arduino
#include <Servo.h>
#include <SoftwareSerial.h>


bool state;
bool btn;

Servo myservo; 
SoftwareSerial xbee(5, 4);

void setup() {
  myservo.attach(21);
  pinMode(12, INPUT_PULLUP);
  pinMode(25, OUTPUT);
  xbee.begin(9600);

}

void loop() {

  if (xbee.available()) {
    xbee.read();
    state = !state;
  }

  bool bt = digitalRead(12);
  if (btn != bt) {
    btn = bt;
    if (bt) {
      state = !state;
      xbee.print('o');
    }
  }
  if (state) {
    myservo.write(0);
  } else {
myservo.write(80);


  }
  digitalWrite(25, state);

  delay(10);


}
```
