# Tietokantasovellus 2019 - Keskustelufoorumi

## Linkit
* [Heroku:](https://tsoha-keskustelufoorumi-jj.herokuapp.com/) 
  * Käyttäjätunnukset (rooli : käyttäjätunnus):
     * MASTER: master
     * ADMIN: admin 
     * USER: aku, hessu
  * Kaikkien tunnusten salasana: ankkalinna 
  * Helppo rekisteröidä myös oma USER käyttäjä
  
* Sovelluksen tila, [weeklyUpdate:](https://github.com/Zessi19/Tietokantasovellus-2019/blob/master/documentation/WeeklyUpdate.md)

* Asennusopas: [InstallationGuide.md](https://github.com/Zessi19/Tietokantasovellus-2019/blob/master/documentation/InstallationGuide.md)
* Käyttöopas + Kommentteja sovelluksesta: [UserGuide.md](https://github.com/Zessi19/Tietokantasovellus-2019/blob/master/documentation/UserGuide.md)

## Sovelluksen kuvaus

Harjoitustyössä tavoitteena on kehittää "old-school" -tyyppinen keskustelufoorumi. Käyttäjä kirjautuu tunnuksellaan foorumille, jolloin käyttäjälle avautuu näkymä kaikista viestiketjuista otsikkoineen (threads). Käyttäjä voi tämän jälkeen valita haluamansa viestiketjun tai luoda kokonaan uuden viestiketjun. Jos käyttäjä valitsee jonkun viestiketjuista, hänelle avautuu näkymä viestiketjun otsikosta ja kaikista viestiketjun viesteistä (posts). Käyttäjä voi myös samassa näkymässä osallistua keskusteluun kirjoittamalla viestiketjuun uuden postauksen.

Kun käyttäjä luo uuden viestiketjun, hänen pitää valita mihin ennalta määriteltyihin kategorioihin viestiketju kuuluu, näitä kategorioita (tags/categories) tulee olla yksi tai useampi. Koska foorumi käsittelee Nintendo pelejä, on tageiksi valittu pääasiassa Nintendo eri konsoleita (yleinen, retro, Wii, WiiU, Switch, DS, 3DS). Kun viestiketju on luotu, käyttäjä näkee viestiketjujen listauksessa kunkin viestiketjun nimen, valitut kategoriat ja viestiketjun viestien lukumäärän.

Keskustelufoorumilla on kolme eri käyttäjätyyppiä: USER, ADMIN ja MASTER. Normaalikäyttäjään USER nähden adminilla on mahdollisuus poistaa ja muokata mitätahansa viestiä tai viestiketjun nimeä ja poistaa kenentahansa normaalikäyttäjän käyttäjätunnus. Normaalikäyttäjällä on mahdollisuus muokata ja poistaa vain itse kirjoittamiaan viestejä (ei kuitenkaan mahdollista poistaa tai muokata edes itse aloittamiaan viestiketjuja). MASTER käyttäjiä on vain yksi ja se luodaan tietokannan perustamisen yhteydessä. ADMIN käyttäjän valtuuksien lisäksi MASTER käyttäjä voi myös poistaa myös minkätahansa ADMIN käyttäjä, sekä muuttaa USER käyttäjän statuksen ADMIN käyttäjäksi tai päinvastoin.

Kirjautuessaan käyttäjä aukeaa mahdollisuus siirtyä käyttäjätietojen näkymään (Omat tiedot). Siellä käyttäjän on mahdollista muuttaa nimeään, käyttäjätunnusta ja salasanaansa ja halutessaan myös poistaa käyttäjätunnuksensa. 


(**Edit:** Tämän kappaleen toiminnallisuuksia ei ole keretty vielä toteuttaa kuten alunperin arvelinkin.) Ajan salliessa projektia voidaan laajentaa antamalla käyttäjän mahdollisuus "up votea tai down votea" yksittäisiä viestejä. Tällöin käyttäjän avatessa viestiketjun, viestit voidaan järjestetää "up votejen" mukaan ja näin saadaan sovellukseen lisää "monimutkaisia yhteenvetokyselyitä". Monimutkaisempaa toiminnallisuutta voidaan lisätä myös antamalla käyttäjälle mahdollisuus järjestää yleisnäkymässä viestiketjut tagien lisäksi esimerkiksi päivämäärän, aktiivisuuden (viestien lkm) tai viestiketjun upvotejen kokonaismäärän mukaan. Huom! Tämän kappaleen toiminnallisuudet eivät kuulu projektin ydintoimintoihin ja niitä aletaan toteutetaa vasta kun ylläolevat perustoiminnallisuudet ovat kunnossa.


## Sovelluksen keskeisiä toimintoja (User stories)

* Kirjautuminen
* Viestiketjujen näyttäminen (luomisjärjestyksessä)
* Viestiketjun valitseminen ja kaikkien viestien näyttäminen (lähetysjärjestyksessä)
* USER: viestiketjuun kirjoittaminen
* USER: oman viestin muokkaus ja poisto
* USER: viestiketjun luominen
* USER: Omien tietojen näyttäminen, muokkaus ja käyttäjätilin poisto
* ADMIN/MASTER: kaikkien viestien muokkaus ja poisto
* ADMIN: USER käyttäjien hallinta
* MASTER: USER ja ADMIN käyttäjien hallinta

USER toiminnot mahdollisia tietenkin myös ADMIN ja MASTER käyttäjille. Kolme ensimmäistä ei vaadi kirjautimista.


## Tietokanta kaavio
![](documentation/tietokantakaavio.png)

Tietokantakaaviossa ydintoiminnallisuutta käsittelevät ja **sovelluksessa totetutetut tietotaulut on valkoisia**. Projektin alussa suunniteltu, mutta myöhemmin pois rajattu äänestytoiminnallisuuden Votes-tietotaulu on merkitty keltaisella. Tietotaulujen atribuutit seuraavat Tietokantojen perusteet -kurssin notaatiota. Tietokantakaavion nuolet Base taulusta Account, Thread ja Post tauluihin tarkoittaa että nämä kolme taulu perivät (eli sisältävät) Base taulun atribuutit.

Dokumentaatio-ohjeissa pyydetään kirjoittaan näkyviin käytetyt CREATE_TABLE lauseet tietokannalle. En aivan ymmärrä tarvetta tälle, koska websovellusta tehtäessä käytetään ymmärtääkseni lähes aina apukirjastoja ja esim. nyt sqlalchemy tapauksessa tietokantataulut määritellää python luokkina tietyssa formaatissa. CREATE TABLE lauseet kirjoitetaan muodossa,

CREATE TABLE table_name (
    column1 datatype,
    column2 datatype,
    column3 datatype,
   ....
)

jossa "columnN" on tietotaulun atribuutin nimi, ja datatype on sen tyyppi, jonka notaatio/tuki voi kaiketi riippua myös tietokannan hallinta järjestelmästä (esim. onko "string" VARCHAR tai mikä TIMESTAMP formaatteja tietokannanhallintajärjestelmä toimii)?

Itse tehtyjä SQL-kyselyitä sovelluksessa on useita niitä käydään tarkemmin läpi käyttötapausten yhteydessä.

## Poisrajatut toiminnallisuudet ( Vertaa moderni keskustelufoorumi)

* Käyttäjän varmentaminen sähköpostilla tai salasanan "hashing".
* Yksityisviestit käyttäjien välillä
* Ryhmäviestit käyttäjien välillä
* Muiden käyttäjien viestin lainaus tai vastaus tiettyyn viestiin josta muodostuu oman alahaaran.
* Ei mahdollista asettaa väliaikaista käyttökieltoa käyttäjälle, vain permanent ban (käyttäjän poisto)
* Ulkoasu pelkistetty vs Moderni keskustelufoorumi

## Projektin rakenne

/Root/
* **auth** (Account table, käyttäjätili functionality)
  * forms.py
  * models.py
  * vierws.py
* **threads** (Thread table, Category table + liitostaulu, viestiketju toiminnallisuus)
  * forms.py
  * models.py
  * vierws.py
* **posts**
  * forms.py
  * models.py
  * vierws.py
* **static** (css-formats ja etusivun kuvat)
* **"sälä"** (moment.js, init.py yms.)

## Yhteenveto sovelluksen tilasta

Kokonaisuudessaan olen tyytyväinen sovelluksen tilaan. Sovelluksessa toimii lähes kaikki projektin alussa tai aikana tärkeäksi todetut ydintoiminnallisuudet. Ainoastaa kaksi pientä toiminnallisuutta jäi toteuttamatta: kategorioiden muokkaus ja viestin created/modified timestampin formatointi. Timestampin formatointi toimii oikein Omat tiedot sivulla moment.js kirjaston avulla, jossa otin kirjaston ensin käyttöön. Tarkoituksena oli formatoida timestamp samaan tapaaan jokaisen viestin yhteydessä, mutta osoittautui että moment.js ei toimi string tyyppiseen listaan, jonka viestit hakeva SQL-kysely palauttaa. Moment.js toimii kuitenkin edelleen oikein Omat tiedot sivulla.

Sovelluksen toiminnallisuuden kommentointi on lisätty käyttötapausten yhteyteen käyttöoppaassa (linkki alussa). Käyttöoppaas käydään läpi alue kerrallaan keskustelufoorumin toimintaa käyttäjän näkökulmasta sekä sovelluksen toteutusta koodi ja SQL-kyselyiden tasolla.

Lyhyesti todettuna sovelluksesta pitäisi löytyä kaikki arvosanaan 5 edellyttettävät "monimutkaisuus vaatimukset:" 
* Vähintään kolme tietokohdetta (4 + liitostaulu)
* Vähintään 2 x GRUD (3 x GRUD + 0.75 = Category)
* Yksi tai useampi monesta moneen -suhde (Category)
* Vähintään kaksi useampaa taulua käyttävä yhteenvetokysely (useita)







