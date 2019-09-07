# Weekly update

Dokumentti sisältää lyhyekön läpikäynnin harjoitustyön tilasta ja lisätyistä toiminnallisuuksista kyseisellä viikolla. Projektin kasvaessa dokumentaatioon tullaan sisällyttämään myös muita tiedostoja, joihin viitataan tässä viikoittaisin projektin läpikäynnissä.

## Week 7 (Final return)

Olen ihan tyytyväinen harjoitustyön lopputulokseen. Viimeisellä viikolla projektiin on lisätty kattava User authentigation, jossa on kolme roolia USER, ADMIN ja MASTER. MASTER käyttäjiä on vain yksi ja se luodaan tietokannan yhteydessä. Tätä käyttäjää ei voida myöskään poistaa. MASTER käyttäjä voi myös muuttaa USER käyttäjän ADMINIKSI tai päinvastoin ja poistaa ADMIN käyttäjän. ADMIN on taas tehty USER käyttäjien hallintaan MASTER käyttäjien lisäksi. MASTER ja ADMIN käyttäjällä on oma Käyttäjien hallinta yläpalkista. Erityisesti tästä käyttäjien varmennus-systeemistä olen tyytyväinen ja se on mielestäni suunniteltu hyvin projektin tulevaisuuden laajentamistakin varten. LLisäksi turhat ei sallitut toiminnallisuudet on piilotettu ei kirjautuneilta käyttäjiltä ja USER käyttäjiltä

Lisäksi on listätty toiminnallisuutta viestien näyttämiseen (viestin lähettämisaika ja jos muokattu niin muokkausaika, parempi viestikentän näyttöformaatti joka mukautuu ruudun kokoon) ja viestiketjujen näyttämiseen (ulkoasua hiottu, lisätty jokaisen viestiketjun lukumäärä)

Lopuksi kategorioihin on lisätty vielä oma validation funktio, jonka avulla varmistetaan että viestiä luodessa valitaan vähintään yksi kategoria. 


## Week 6

**-- Edit --** Muutama tunti meni yliaikaa, mutta vihdoin Heroku toimii. Olin nimennty Kategoria liitostaulun threadCategory, mutta jostain syystä liitostaulu toimii vain kokonaan pienellä kirjoitettuta (eli threadcategory) Herokussa. Paikallisesti omalla koneella molemmat versiot olivat. Tällä viikolla käytin tähän menessä heittämällä eniten aikaa projektiin monesta moneen taulun ja User authenticationiin liittyvien pugien takia. Projektin tulevan viimeistelyn pitäisi nyt toivonmukaan olla suoraviivaisempaa projektin hiomista jo tuttujen python/flask/sqlalchemy toiminnallisuuksien avulla. **-- Edit End --**

Projektiin on lisätty viimeiset puuttuvat isot kokonaisuudet: Kategorioiden (yksi tai useampi) liittäminen Threadiin ja User authentication käyttäjän userRole muuttujan avulla (User, Admin tai Master).

Kategoriat on lisätty erillisenä tauluna (Category) ja liitostauluna (ThreadCategory). Kategoriat lisätään Threadin luomisen yhteydessä intuitiivisesti raksittamalla laatikoista sopivat. Toimii: uuden threadin luomisessa, threadien listauksessa ja threadin poistossa. Työnalla: kategorieoiden vaihtaminen threadia muokatessa, valdiointi (min yksi kategoria). Kategoriat luodaan thread/__init__.py tiedostossa olevan event handlerin avulla tietokannan luonnin yhteydessä.

User authentication on toteutettu kurssin materiaalin malli mukaillen. Sovelluksessa on kolme käyttäjä luokkaa User, Admin ja Master. Master ja Admin käyttäjät luodaan tietokannan luonnin yhteydessä /auth/__init__.py tiedoston event handlerin avulla. Käyttäjän rekisteröityessä käyttäjätunnuksen luokaksi tulee User. Tällä hetkellä kirjautuminen vaaditaan (vähintään User) kaikkiin foorumin rakenteeseen vaikuttaviin toiminnallisuuksiin. Viikonlopun/ensi viikon aikana Muiden viestien ja ketjujen poistaminen rajataan vain admin/master käyttäjälle.

Kuten todettiin foorumin kaikki oleellisimmat rakenteet ovat nyt ainakin lähestulkoon valmiit. Tulevan viikon aikana täytyy vielä crunchata ja tehdä hieno säätöä foorumin ulkoasu ja lisätoiminnallisuuksien (threadin järjestäminen eri kriteerein, viesteihin timestamp created yms.) liittyen.

Sovellus toimii tällä hetkellä (lauantai ilta) ilman ongelmia tai virhe-ilmoituksia lokaalisesti. Jostain syystä saan kuitenkin Herokusta erroria ilmeisesti Kategoria liitostauluun liittyen. Koitan fiksata ongelman, ja joudun varmaan tekemään aika monta git commitia herokuun liittyen. Kuten sovimme sähköpostilla, sain yhden päivän lisäaikaa week 6 deadlineen.  



## Week 5

Projektissa on nyt valmiina kaikkiin kolmeen päätauluun (Account, Thread, ja Post) liittyvä perustoiminnallisuus eli kaikkien taulujen full GRUD, Threadien ja Postien oikeaoppinen näyttäminen ja taulujen järkevä käyttätyminen kun toista taulua muutetaan. Esimerkiksi jos käyttäjä poistaa viestiketjun, sovellus poistaa myös kaikki viestiketjussa olevat viestit eivätkä ne jää sovelluksen ulottumiin viemään tilaa tietokannasta. Vastaavasti, jos käyttäjä haluaa poistaa käyttäjätilinsä, poistuu samalla kaikki käyttäjän lähettämät viestit, mutta mahdollisesti aloitetut viestiketjut jäävät jäljelle.

Muita uusia ominaisuuksia:
* Etusivulle useita uusia toiminnallisuuksia (SQL queries + kuvia)
* Omat tiedot sivulle lisätty toiminnallisuutta (SQL queries)
* Otettu käyttöön Moment.js kirjasto parsimaan TIMESTAMP (käytetään tällä hetkellä omat tiedot sivulla, myöhemmin posteissa myös)
* lisätty Documentation/InstallationGuide.md
* Sovelluksessa näkyvät palkit/toiminnallisuudet toimivat järkevästi ja oikein

Kaikki viikolla 5 vaadittavien etappien pitäisi siis olla tehty (toiminnallisuuden täydentäminen, käytettävyyden viilaus, alustava asennus- ja käyttöohje). Autorisointi on vielä kesken, mutta nythän piti olla vasta aloitettu viikon 5 etapit.
Sovelluksessa on nyt useita yhteenveto kyselyitä, mutta tehdyissä ei käytetä GROUP BY komentoa. GROUP BY komentoa ei ole vielä järkeä käyttää sovelluksessa (ensi viikolla Category taulun yhteydessä asia muuttuu). Tein jo yhden "väkisin", mutta se osoittauitui hyvin vaikeaksi ja pugiseksi tapauksissa, jossa käyttäjällä ei ollut esim. yhteen viestiä tai viestiketjua. Mielestäni tässä tapauksessa olisi väärin vähentään pisteitä tällä viikolla uudestaan, vaikka ominaisuus vaaditaan viikon 4 etapeissa.



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

