---
title: Clockworks Site
description: Detalii privind dezvoltarea site-ului echipei
published: true
date: 2026-01-30T20:20:20.726Z
tags: programming, project
editor: markdown
dateCreated: 2025-05-23T15:51:46.312Z
---

# Admin-ul site-ului Clockworks
<br>

## Scurta introducere (About)
Un proiect esential pentru orice fel de organizatie este site-ul lor. Reprezinta prezenta lor online, oferind tuturor acces la observarea reusitelor si proiectelor lor, membrii si orice alte detalii ce necesita a fi publicate. 

Majoritatea site-urilor consista dintr-un simplu frontend, avand un backend care doar raspunde cu fisiere statice, deobicei acesta fiind automatizat, gata facut prin web servere precum Nginx sau Apache (Apache fiind ceea ce folosim si noi pentru frontend-ul site-ului principal).

O mare problema la site-uri statice de genul este ca orice modificare mica necesita un re-deploy facut la tot site-ul, sau cel putin la fisierele modificate si cele adaugate. De asemenea, niciun membru care nu este pe profilul tehnic nu poate modifica site-ul (sau, cel putin, nu poate cu usurinta), avand ca rezultat necesitatea de a apela constant la un programator.

De aceea, de anul trecut, a aparut initiativa de a face un dashboard pentru site-ul principal, numit “admin”. Prin intermediul sau, am vrut sa facilitam tuturor membrilor, indiferent de domeniul lor, sa poata modifica anumite sectiuni de interes ale site-ului, in special sectiunea de membrii si de articole pentru proiectele noastre (aceasta fiind o zona unde anumite evenimente mai importante pot fi vizualizate). 

## Versiunea veche (Prima varianta)
Intial, din cauza lipsei de experienta, backend-ul pentru primul admin a fost facut folosind Javalin, la sfatul unui mentor, deoarece era simplu de folosit, avand builder-like pattern-uri pentru crearea endpoint-urilor. Desi a reprezentat un inceput foarte rapid, a devenit din ce in ce mai greu de intretinut cu cat proiectul a scalat, ajungand la fisiere extrem de mari pentru initializarea server-ului si a endpoint-urilor. Pentru a simplifica cat de cat codul, codul s-a impartit in mai multe clase, in care fiecare clasa primea ca si parametru in constructor instanta server-ului Javalin, iar apoi acesta isi adauga endpoint-urile sale (ex: “TeamController” isi adauga la server GET “/team/{id}” si POST “/team”). Desi asta a ajutat un pic la intretinerea codebase-ului si a redus complexitatea pe care o aducea fiecare multime de endpoint-uri, tot nu era o soluitie viabila. 

Nu vom intra in detalii prea mult despre fosta arhitectura, dar modelul vechi folosea ca strategie Server Side Rendering, frontend-ul pentru admin fiind facut cu HTML, CSS si JS Vanilla (inca o greseala, creand iarasi un codebase greu de modificat, citit si testat), folosind Mustache, insemnand ca fisierele erau generate odata cu primirea request-ului. Desi in teorie, SSR este mult mai rapid ca alternativele in care client-ul trimite request-uri la backend pentru date, era extrem de greu de testat si de facut design-ul la frontend. Vom avea o comparatie completa intre Sistemul Vechi si Sistemul Nou.

Datorita tuturor acestor probleme, am decis ca e necesar un refactor complet, atat la frontend-ul admin-ului, cat si la backend-ul sau.

## Sistemul nou
Noul sistem e alcatuit din 3 componente importante principale: backend-ul, frontend-ul si automatizarea deployment-ului, despre care vom vorbi un pic la finalul articolului.

Pentru frontend, deoarece am realizat problema cu fosta arhitectura, am renuntat la ideea de SSR, creand un SPA (Single Page Application) in schimb cu React in TypeScript, astfel beneficiand de type system-ul sau, oferindu-ne un mod de detectare a erorilor la compile time si de a scrie cod mult mai lizibil. Observatie, SPA inseamna doar ca aplicatia este continuta total intr-un singur fisier de HTML, unul singur de JS (compilat din TS) si unul singur de CSS, dar totusi poti simula diferite pagini prin React folosind librarii precum React Router, simuland astfel, folosind History API-ul, pagini diferite si navigarea ce e prezenta in oricare site.

Acum, pentru motivul principal pentru care s-a si facut aceasta tranzitie la un sistem nou, backend-ul; a fost dezvoltat in Java, dar de data asta folosind Spring Boot, o librarie mult mai matura si potrivita pentru proiecte mari, beneficiand de un ecosistem de librarii bogat. Astfel, ne-am folosit de foarte multe Quality of Life improvements fata de Javalin. Dar, poate cel mai important improvement din lista a fost Spring Security, permitandu-ne sa cream un pipeline de securitate cu OAuth 2.0, cu un provider extern configurat de noi cu Authentik care acorda accesul prin intermediul Discord oricarui membru ce detine un anumit rol in comunitatea noastra.

Puteti vizualiza mai jos, prin diagrama facuta, arborele de decizie ce reprezinta procesul de autentificare.

![admin.darkl.drawio.png](/Projects/admin.darkl.drawio.png)


De asemenea, pe langa improvement-urile aduse la backend, am facut un CI/CD pipeline pentru a facilita un deployment mai usor al admin-ului pe server-ul echipei. Astfel, folosind GitHub Actions, am creat un job care ruleaza odata cu orice push pe branch-ul de productie, si executa apoi urmatorii pasi:

![ci_cd.drawio_(1).png](/Projects/ci_cd.drawio_(1).png)

Odata cu implementarea unui CI/CD pipeline pentru admin, am implementat inca un pipeline pentru deployment asemanator si pentru frontend-ul site-ului principal, dar in loc de a folosi SSH, am folosit protocolul FTP pentru a face transferul de date.
