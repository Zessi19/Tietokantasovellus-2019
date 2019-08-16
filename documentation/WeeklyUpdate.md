# Weekly update

Dokumentti sisältää lyhyekön läpikäynnin harjoitustyön tilasta ja lisätyistä toiminnallisuuksista kyseisellä viikolla. Projektin kasvaessa dokumentaatioon tullaan sisällyttämään myös muita tiedostoja, joihin viitataan tässä viikoittaisin projektin läpikäynnissä.

## Week 4

Materiaalissa edetty Osa3, Osa4, selattu Osa5 authentication
* Kirjautuneelle käyttäjälle lisätty Omat tiedot sivu (Account taulu)
  * Vaihda nimi
  * Vaihda käyttäjätunnus
  * Vaihda salasana
* Lisätty kolmas taulu Posts
* Yhdistetty kaikki kolme taulua Account, Thread, Post
  * Kaksi monimutaisempaa yhteenvetokyselyä, jotka käytetään ja näytetään käyttäjälle kun luotu viestiketju avaataan
* Thread taulu: Viestiketjua luotaessa annetaan käyttäjä luo otsikon lisäksi myös itse viestin
* Post taulu
  * Viestiketjua klikatessa kaikki ketjuun liittyvät viestit haetaan ja näytetään
  * Jokainen viesti voidaan poistaa viestin perässä olevasta painikkeesta
* Heroku: PostgreSQL otettu käyttöön
* Tietokanta taulujen rakennetta fiksattu, kaikki kolme taulua perii Base taulun (id, created, modified) ja "turha" yhteys Threadin ja Accountin välillä poistettu
* Login required lisätty kaikkiin toistaiseksi järkeviin ja pakollisiin paikkoihin eli Account tauluun liittyviin tehtäviin ja uuden viestiketjun + ekan postauksen luomiseen.
* Ulkoasua hiottu "retro tyyliin" itse css-komennoilla, viestiketjujen näkymä tulee vielä kehittymään paljon. Ensin pitää kuitenkin toteuttaa puuttuvat toiminnot
* README.md tietokantakaavio kuva päivitetty!
* Koska Post taulun priority muuttujalla ilmaistaan aloituspostausta (mahdollistaa adminille mahdollisuuden voi luoda uusi aloituspostauks tai sen yläpuolella näkyvä "Sticky" postaus)


Harjoitustyö eteni tällä viikolla aika lailla suunnitelmien mukaan. Keskustelufoorumissa on nyt kolme keskeisintä taulua + perittävä Base taulu, jotka on yhdistetty toisiinsa tietokantakaavion osoittamalla tavalla. Viikon isoin ja hieman ulospäin näkymätön muutos oli tietokantataulu rakenteen päivitys, missä Account, Thread, Post ensin perivät Base taulun ja "turha" yhteys Account ja Thread taulun välissä on poistettu. Yhteyden poisto selkeyttää esim. tapausta missä käyttäjätili poistetaan ja kaikki käyttäjän viestit halutaan poistaa. Tällöin käyttäjän luomia threadeja ei kuitenkaan tarvii poistaa tai asiasta ei muodostu ongelmaa (threadi jäisi ilman käyttäjää -> pitäisi tehdä jokin deleted user hässäkkä, joka on liian paljon tämän projektin laajuuteen).

Nyt käyttäjän luodessa uusi viestiketju, täytyy hänen luoda myös aloitusviesti. Viestiketjujen nimeä klikatessa avautuu näkymä kaikista ketjun viesteistä (toistaiseksi vain 1 tai 0 viestiä). Vaikka viestejä olisi vain yksi eli aloitusviesti, tekee ohjelma kaksi toimivaa SQL kyselyä, joilla haetaan ensin Threadin tiedot ja sitten kaikki Threadiin liittyvät viestit, jotka on järjestetty ensin priorityn mukaan (aloituspostaus 1, muuut postaukset 0) ja sitten luomisajan mukaan. Lisäksi kaikki käyttäjät voivat poistaa viestin, jolloin pelkästään threadi jää jäljelle (kaikilla admin oikeudet toistaiseksi).

HUOM! Koska Post toiminnallisuutta ollaan lisäämässä, jouduttaan luonnollisesti muuttumaan myös viestiketjujen toiminnallisuutta. Tällä hetkellä kannattaa ensin poistaa viestiketjusta kaikki viestit ja vasta sitten itse viestiketju. Muuten yhteys viestiketjun viesteihin katoaa ja ne jäävät turhaan viemään tilaa tietokannasta. Tämä tullaan korjaamaan heti kunhan yksittäisten viestien toiminnallisuus on ensin saatu valmiiksi. Tässä pitää rakentaa pohja ensin (Viestit) ja vasta sitten fiksata Viestiketjut taas kuntoon.

Account taulun toiminnallisuus alkaa näyttää jo hyvältä. Käyttäjä voi katsoa omia tietojansa ja vaihtaa rekisteröityä nimeä, käyttäjätunnusta tai salasanaa. Poista käyttäjätiliä painaessa ei kuulu tapahtua vielä mitään (html button painike). Voidaan asettaa käyttöön vasta kun Thread ja Post toiminnallisuudet OK.


Linkit korjattu/siistitty README.md


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

