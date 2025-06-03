---
title: Clockworks Site
description: Site-ul echipei clockworks, atat cel principal cat si admin-ul
published: true
date: 2025-05-27T15:25:50.855Z
tags: 
editor: markdown
dateCreated: 2025-05-23T15:51:46.312Z
---

# Obiective
* Crearea unui site modern care sa reprezinte clubul
* Centralizarea activitatilor clubului, in sectiunea de "Proiectele noastre"
* Prezentarea informatiilor privind organizarea echipei si membrii acesteia
* Datele noastre de contact, fiind mai usor pentru alte persoane sa ne contacteze astfel
* Public Relations & Marketing

# Etapele proiectului
*( etapele sunt descrise mai in detaliu in urmatoarea sectiunea, aici sunt doar scrise generic )*
1. Construirea unui frontend de stil portofoliu pentru site ( index )
2. Adaugarea paginii de contact
3. Desi in acest moment statice, adaugarea unei pagini pentru membri si inca una pentru proiecte, hard-coded
4. Citirea si crearea dinamica a continutului pentru cele 2 pagini in functie de fisierele JSON gasite intr-o locatie specificata
5. Introducerea unui admin, frontend + backend, din care orice membru se poate autentifica si modifica datele de pe cele 2 pagini + alte features.

# Implementarea proiectului
Initial, a fost facut site-ul de pe www.teamclockworks.ro. Datele pentru echipa si proiecte erau stocate in fisiere JSON pe domeniu.  
De exemplu, pentru a reprezenta un proiect, inainte trebuia creat un fisier JSON cu formatul:
```
{
	"title": "Sample Article 1",
  "description": "This is the description",
  "sections": ["Section 1", "Section 2", "Section 3"],
  "content": "<h1> This is the heading" </h1>\n<p>This is the next line</p>
}
```
Aceasta varianta, desi era functionala, nu era una chiar optima, deoarece era greu de modificat, trebuiau mereu modificate fisierele de pe domeniu pentru fiecare schimbare in articol,si trebuie direct pus codul de HTML, ceea ce inseamna ca majoritatea persoanelor nu ar fi putut scrie un articol de genul pentru un proiect (atat timp cat nu au un fundal intr-un domeniu precum programare). 

De aceea, pentru a simplifica si cumva automatiza in acelasi timp acest proces, am decis sa fac un admin pentru site, din care oricare membru, odata autentificat, poate adauga proiecte si manageria membrii echipei, printr-o interfata vizuala. Server-ul pe care a fost admin-ul deployed este diferit de cel pentru site-ul principal, iar domeniul pe care este expus este admin.teamclockworks.ro, un subdomeniu al celui mentionat mai sus.

Implementarea a fost una simpla, avand nevoie de cateva componente principale:
* O pagina pentru a manageria articolele si a le afisa tabular intr-un tabel (datele principale, adica titlul, descrierea, data creata) si cu butoane pentru urmatoarele actiuni: Edit, Toggle, Delete
* Un parser de markdown, facut de mine, astfel incat continutul articolelor sa fie scrise in format **markdown** si compilate in **HTML**.
* O pagina pentru a manageria membrii echipei, a le edita numele, pozele si rolurile.
* Inca o sectiune pentru statisticile site-ului, precum vizualizarile pe zi, luna si an si optiuni de a trece site-ul in modul *Under Construction*.

Pentru a stoca aceste date, le-am tinut intr-o baza de date, care, primind request-uri pe anumite endpoint-uri, raspunde cu JSON-ul necesar, fiind o arhitectura pe stil REST pentru articole.

# Date tehnice
Aceasta sectiune va intra in mai multe detalii legat de implementarea tehnica a proiectului, fiind o varianta extinsa a sectiunii anterioare. Va trece prin teme precum endpoint-urile, strucutra proiectului, securitatea site-ului si alte topicuri importante.

Frontend-ul este scris in JS pur cu HTML si CSS, desi doresc in viitor sa fac un cleanup al codului si sa il rescriu cu o librarie moderna, precum React.

Backend-ul este scris in Java, iar, deoarece initial nu am luat in calcul magnitudinea proiectului, am ales Javalin, o librarie simpla pentru crearea de servere, dar care nu se compara cu librarii precum Spring Boot. Aceasta este urmatoarea modificare pe care urmeaza sa o fac, portand codebase-ul de la backend de la Javalin la Spring Boot.

Baza noastra de date este PostgreSQL, deoarece ne trebuia o baza de date relationala, iar alegerea a fost facuta intre Postgres si MySQL. 

Endpoint-urile si metodele folosite sunt urmatoarele:

|	Action | Articles | Team Members* | 
|-| -------- | ------------ |
| *get* | **GET** /articles/id/content | / |
| *getAll* |  **GET** /articles | **GET** /team |
| *create* |  **POST** /articles/ | **POST** /team |
| *delete* |  **DELETE** /articles/id/content | / |
| *update* |  **PUT** /articles/id/content | **PUT** /team/id |

*\* (Partea de management a echipei nu se mai face prin arhitectura REST, astfel incat nu se poate obtine un singur membru din baza de date. De asemenea, membrii nu pot fi stergi, ci doar setati inactivi.)*

## Structura proiectului 
```
src
  main
    	java
      	article
        	--> clase legate de Articole, precum entitatiile si repo-ul
          
        auth
        	--> clase legate de Autentificare, atat prin logare cu user + parola cat si prin OAuth cu contul
          de discord.
          
       controllers
       		--> pentru a simula separarea din Spring Boot pe diferite controllere, fiecare controller pentru 
          fiecare entitate este aflat in acest package
          
       db
       		--> contine clasa primara de Database, care este injectata in fiecare repo. Se ocupa de 
          connection pool
          
       parser
       		--> clasa ce contine algoritmul de parsing pentru markdown -> html
          
       server
       		--> aplicatia principala, entry point-ul
          
       stats
       		--> clase de calcule cu statisticile site-ului
          
       team
       		--> la fel ca la articole, pentru membrii echipei
          
       util
       		--> clase utile diverse
   	resources
      	--> fisierele statice, template-urile pentru Server Side Rendering (SSR)
```

## SSR
Am ales ca pentru paginile de frontend din admin sa facem server side rendering, deoarece am considerat ca este optiunea mai rapida. Pentru a atinge acest scop, am folosit *Mustache* si plugin-urile pentru Javalin pentru SSR.

## Securitate
Pentru securitatea site-ului, am implementat OAuth si mentinem sesiunile de logare prin JWT-uri (Javascript Web Token), avand ca provider serviciul **Authentik**. Pentru a te loga cu succes cu discord, ai nevoie atat sa fii pe server-ul clubului, cat sa ai si rolul de membru. Prin intermediul claselor din package-ul **auth**, refresh-ul la tokene se face automat odata expirate. Astfel, fiecare endpoint mai are ca parametru tipul sau, o valoarea de tip Enum, fiind ori *Role.LOGGED_IN* ori *Role.OPEN*, fiecare reprezentand stare de autentificare necesara pentru ca request-ul sa returneze continutul dorit.

## Debugging, logging
Aplicatia are un sistem puternic de logging datorita librariei SLF4J, astfel incat sunt constant trimise log-uri pentru fiecare actiune a sa, precum orice autentificare in sistem, request trimis sau eroare a bazei de date; toate vor fi afisate.

## Deployment
Pentru deployment, noi am folosit docker, creand un container pentru aplicatia data si expunand-o pe portul :8080 a server-ului. Astfel, toate dependency-urile sale sunt adaugate in configurarea containerului, asigurand compatibilitate. De exemplu, libraria ffmpeg care este folosita de catre Java prin call-uri la terminal pentru a crea automat, pentru fiecare imagine pusa pentru fiecare membru, o versiune de 20x20px pentru loading rapid si crearea unui placeholder rapid, blurat, pana imaginile complete se incarca ( pentru zone cu retele slabe ).

# Preview Site
![site.png](/site.png)

# Viitorul proiectului
Roadmap-ul arata astfel:
1. Rescrierea backend-ului pentru admin folosind Spring Boot si, astfel, implementand JPA cu Hibernate, pentru a elimina necisitatea de a scrie manual comenzile de SQL si pentru a ne folosi de feature-urile puternice din modulul Spring Data
2. Rescriere frontend admin cu React.JS, pentru un cod cat mai modular, si eliminand SSR-ul, deoarece continutul de date nu este destul incat sa trebuiasca viteza mai mare a acestei solutii, numarul de elemente fiind de ordinul zecilor.
3. Implementare Prometheus pentru colectarea statisticilor, inlocuind varianta de acum manuala
4. Completarea acestei pagini cu mai multe detalii, precum structura bazei de date pentru tabelele importante.
