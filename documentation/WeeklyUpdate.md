# Weekly update

Dokumentti sisältää lyhyekön läpikäynnin harjoitustyön tilasta ja lisätyistä toiminnallisuuksista kyseisellä viikolla. Projektin kasvaessa dokumentaatioon tullaan sisällyttämään myös muita tiedostoja, joihin viitataan tässä viikoittaisin projektin läpikäynnissä.

## Week 3

Materiaalissa edetty kohtaan Osa3 2.4/2.5, sovelluksessa toimii
* Lomakkeet validoivat syötteen
* Rekisteröityminen + Kirjautuminen
* GRUD Threads tietotaulu
* 2 x tietotaulua Threads ja Account/User

Kesken
* Tietotaulujen yhdistäminen (polkujen suojaaminen järkevä miettiä tämän yhteydessä)
* PostgreSQL (Heroku käyttää viimeviikon mallia)


Tämä viikko sujui ennen kaikkea Python Flask-kirjastoon tutustuessa. Onneksi deadline-taulukossa tällä viikolla vaadittiin vasta 3 viikon materiaalin aloitusta, ei kaikkien etappien suoritusta. Varsinkin alkuviikosta käytin paljon aikaa Flaskin testailuun ja parantelin Threads tietotauluun liittyvää koodia. Taulukun otsikoilla on nyt täysi GRUD ja otsikon muokkaaminen tapahtuu nyt erillisessä näkymässä. Lisäksi projektiin on liitetty User/Account tietotaulu, jonka rakenne seuraa materiaalin ohjetta. Tämän avulla sovellukseen on nyt mahdollista rekisteröityä, kirjautua sisään (username näkyy yläreunassa boldattuna) ja kirjautua ulos.

Käytin tällä viikolla myös huomattavasti aikaa lomakkeiden syötteen validoinnin järkevään toimintaan, validointia tehdään jokaisen lomakkeen ohella ja siinä on käytetty toiminnallisuuksia myös kurssimateriaalin ulkopuolelta. Esimerkiksi salasanan pitää olla vähintään 8 merkkiä, enintään 50 ja se pitää syöttää kaksi kertaa yhtenevästi. Lisäksi rekisteröityessä lomake tarkastataa mm. että rekisteröity käyttäjätunnus ei ole jo varattu

Ensi viikolle / 1. Koodikatselmus
* Account/User tietokantaan GRUD (Omat tiedot sivu, mahdollisuus muokata tietoja, mahdollisuus poistaa käyttäjä, yhteenvetokyselyt total topics ja post käyttäjälle)
* Post tietotaulu, mahdollisuus nähdä viestiketjun otsikko ja postit, lähettää viestiketjuun viesti
* Ulkoasun viilaus jo suurimmaksiosaksi tehty, siirryn Bootstrappiin Demo tilaisuuteen mennessä, nyt tärkeintä saa perustoiminnallisuus kuntoon





## Week 2

Sovelluksen koodaamisen aloitus. Keskustelufoorumin ensimmäiseksi toteutettavaksi tietotauluksi valittiin Thread-taulu (otsikko, keskustelun aihe), joka on sopivasti hyvin samankaltainen esimerkki-sovelluksen Task-taulun kanssa. Keskustelufoorumilla on nyt etusivu, mahdollisuus listata kaikki keskustelunaiheet, lisätä uusi keskustelun aiheet, sekä muokata keskustelun aiheen nimeä. Toisin sanoen Thread tietotaulusta voi hakea tietoa, tauluun voi lisätä tietoa ja taulun tietoa voi muokata. Lisäksi sovellus on testattavissa myös Herokussa. Materiaalin toiminnallisuuksien lisäksi sovelluksen ulkoasua on muokattu application/static/ kansiossa olevalla .css tiedostolla fiksummaksi (väliaikainen ratkaisu, vaihdetaan materiaalin Bootstrap-kirjastoon aikanaan).

Ensi lisään dokumentaatioon uuden tiedoston, johon listaan päivitän aina sovelluksen kaikki sen hetkiset toiminnallisuudet ja "käyttöohjeet". Tällä hetkellä sovelluksen ollessa vielä yksin sovelluksessa helppoa liikkua selkeästi nimettyjen linkkien välityksellä. Kun sovellukseen lisää uuden Threadin, tulee uuden threadin kanssa samalle riville myös tekstilaatikko ja muokkaa painike. Nyt käyttäjä voi vaihtaa threadin nimeä kirjoittamalla uuden nimen laatikkoon ja painamalla painiketta. Tämä ominaisuus tullaa myöhemmin rajaamaan vain admin-käyttäjälle.   

