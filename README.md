# Tietokantasovellus 2019 - Keskustelufoorumi

## Sovelluksen kuvaus

Harjoitustyössä tavoitteena on kehittää "old-school" -tyyppinen keskustelufoorumi. Käyttäjä kirjautuu tunnuksellaan foorumille, jolloin käyttäjälle avautuu näkymä kaikista viestiketjuista otsikkoineen (threads). Käyttäjä voi tämän jälkeen valita haluamansa viestiketjun tai luoda kokonaan uuden viestiketjun. Jos käyttäjä valitsee jonkun viestiketjuista, hänelle avautuu näkymä viestiketjun otsikosta ja kaikista viestiketjun viesteistä (posts). Käyttäjä voi myös samassa näkymässä osallistua keskusteluun kirjoittamalla viestiketjuun uuden postauksen.

Kun käyttäjä luo uuden viestiketjun, hänen pitää valita mihin ennalta määriteltyyn kategoriaan viesti kuuluu, näitä kategorioita (tags) tulee olla yksi tai useampi. Jos foorumimme käsittelesi esimerkiksi Playstation pelejä, tageja voisi olla esimerkiksi ps1, ps2, ps3, ps4, ps5, jrpg, rpg, platformer, puzzle, simulator, shooter, racing, sports, psDeals ja general. Kirjautuessaan sisään käyttäjällä on mahdollisuus valita kaikkien viestiketjujen näkymässä näytettävän vain ne viestiketjut, jotka on sisältä yhden tai useamman käyttäjän valitseman tagin, esimerkiksi ps3 ja ps4.

Keskustelufoorumilla on kaksi eri kättäjätyyppiä: user ja admin. Normaalikäyttäjään user nähden adminilla on mahdollisuus poistaa mikätahansa viesti tai viestiketju ja poistaa kenentahansa normaalikäyttäjän käyttäjätunnus. Mahdollisesti adminille voidaan myös lisätä myös mahdollisuuksia muuttaa viestiketjun tageja, jos ne on asetettu väärin (vastaa perinteisillä foorumeilla viestiketjun siirtämistä oikeaan aihealueeseen).

Ajan salliessa projektia voidaan laajentaa antamalla käyttäjän mahdollisuus "up votea tai down votea" yksittäisiä viestejä. Tällöin käyttäjän avatessa viestiketjun, viestit voidaan järjestetää "up votejen" mukaan ja näin saadaan sovellukseen lisää "monimutkaisia yhteenvetokyselyitä". Monimutkaisempaa toiminnallisuutta voidaan lisätä myös antamalla käyttäjälle mahdollisuus järjestää yleisnäkymässä viestiketjut tagien lisäksi esimerkiksi päivämäärän, aktiivisuuden (viestien lkm) tai viestiketjun upvotejen kokonaismäärän mukaan. Huom! Tämän kappaleen toiminnallisuudet eivät kuulu projektin ydintoimintoihin ja niitä aletaan toteutetaa vasta kun ylläolevat perustoiminnallisuudet ovat kunnossa. 


## Sovelluksen keskeisiä toimintoja

* Kirjautuminen
* Viestiketjujen näyttäminen eri kriteerein
* Viestiketjun valitseminen ja kaikkien viestien näyttäminen (eri kriteerein)
* Käyttäjä: viestiketjuun kirjoittaminen
* Käyttäjä: viestiketjun luominen
* Käyttäjä: oman viestin poistaminen
* Admin: viestin poistaminen
* Admin: viestiketjun poistaminen


## Tietokanta kaavio



## Poisrajatut toiminnallisuudet ( Vertaa moderni keskustelufoorumi)

* Käyttäjän varmentaminen (authentication)
* Yksityisviestit käyttäjien välillä
* Ryhmäviestit käyttäjien välillä
* Edellisen käyttäjän viestin lainaus tai vastaas, joka muodostaa oman alahaaran.
* Ei mahdollista asettaa väliaikaista käyttökieltoa käyttäjälle, vain permanent ban
* Ulkoaso pelkistetty vs Moderni keskustelufoorumi


## Kysymyksiä

Onko adminin oikeuksien merkitseminen User-tietotauluun omana Boolean muuttujana järkevä tapa? Ohjelmaan on tarkoituksena kovakoodata oma käyttäjätunnukseni, jota ei ole mahdollista poistaa käyttäjänpoisto -metodilla. Uuden käyttäjän tapauksessa Boolean muuttuja asetetaan aina off-tilaan. Tämän jälkeen toisella admin-käyttäjällä on toiminnallisuus, jolla valittu user-käyttäjä voidaan siirtää user-tilasta admin-tilaan, ja ohjelman metodi asettaa tällöin Boolean muuttujan on-tilaan. 


