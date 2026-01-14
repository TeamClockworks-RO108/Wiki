---
title: Keepers
description: 
published: true
date: 2025-10-28T02:03:02.923Z
tags: 
editor: markdown
dateCreated: 2025-05-15T07:01:34.241Z
---

# Descriere
Keepers este o aplicatie de inventariat, open-source, multiplatform, care poate ajuta organizatiile sa isi tina evidenta inventarului intr-un mod usor.
# Obiective

* Vom putea tine cont de toate materialele clubului, fie ca sunt implicate sau nu intr-un proiect.
* Notificari pentru stocuri minime sau epuizate
* Sistem de autentificare cu roluri diferentiate (admin, angajat etc.)
* Actualizarea stocurilor in timp real


# Etapele Proiectului 

I.    Frontend
II.   Cuplarea frontend-ului la un api pentru o baza de date MOCK
III.  Backend
IV.   Testarea aplicatiei
V.    Implementarea compatibilitatii cu Android si IOS.

# Cum implementam? 

Implementarea aplicatiei se face folosind Android Jetpack Compose Multi Platform pentru realizarea interfetei grafice si a logicii de prezentare. Frontend-ul este conectat la un API documentat cu Swagger, care faciliteaza testarea si integrarea. Backend-ul utilizeaza o baza de date SQL pentru stocarea si gestionarea datelor, asigurand un sistem robust si scalabil.

# Progres

Proiectul a fost conceput in noiembrie si pus in activitate in ianuarie. 

 ## FrontEnd
 
 Front end-ul a fost realizat initial in Jetpack Compose Multiplatform, insa datorita unor librarii de android native, acesta a trebui sa fie recent refacut pentru a isi putea pastra proprietatile de multi-platform. Navigatia si alte concepte simplificate pe android au fost reimplementate pentru o aplicatie cu adevarat comutabila intre platforme 
 
 ### Global Data
 Global Data constituie o clasa care contine toate tranzitiile de la un ecran la altul. Informatia furnizata este preluata de navigator care initiaza apoi schimbarile de un @Composable la altul.
 
 ```

    companion object {
        @Composable
        fun Navigator(navController: NavHostController) {
            NavHost(
                navController = navController,
                startDestination = "HomeScreen",
            ) {
                composable(route = "HomeScreen") {
                    Home().Display()
                }
                composable(route = "InventoryScreen") {
                    Inventory().Display()
                }
                composable(route = "ProfileScreen") {
                    Profile().Display(navController)
                }
            }
        }
    }
    }

```
 ### Home
 
 Interfata asta permite accesul la celelalte doua interafte principale: Inventarul si Pagina de profil. In versiuni viitoare, insa, pagina de profil va fi implementata in cadrul celei de Home pentru simplitate si o navigatie mai usoara. 
 
 
 
 
![keepers-main-view.png](/keepers-main-view.png)

### Inventar

La baza Composable ului de Inventar se afla un DissmissibleDrawer care permite navigatia usoare intre search bar si pagina informativa a itemului selectat. In versiunea de prototip aceasta prelua informatii dintr o clasa de date globale si le introducea intr un LazyColumn pentru a permite realizarea unei liste de itemi. Slide ul interafata de searching si item ul propriu zis se face automat atunci cand un titlu este selectat. 

### Functia de Search din Inventar
Functia de instant text searching se foloseste de proprietatile variabilelor de actionate de MutableStateOf si sunt folosite pentru a evalua constant orice similaritate intre textul sample introdus de utilizator si title, tag-ul sau keyword-urile itemilor. 

![screenshot_20250525_170230.png](/screenshot_20250525_170230.png)

### Paginile individuale
Fiecare obiect va avea pagina lui care va putea fi modificata de persoanele autorizate, in mod normal, membrii clubului. In varianta de prototip insa pagina va fi doar vizualizabila si va putea fi modificata numai interactionaand in mod direct cu baza de date. 

In variante finale va exista un buton de '+' pentru a creea un entry prin care ori declari o modificare in cantitate ori declarari ca un numar din itemii respectivi vor fi utilizati intr un proiect sau eliberat din alt proiect. De asemenea va exista si un buton de 'history' care va afisa fiecare entry pentru a tine mai eficient cont si a centraliza detaliile componentelor tehnice care apartin clubului. 

## Cuplarea FrontEnd-ului la BackEnd -ul MOCK





