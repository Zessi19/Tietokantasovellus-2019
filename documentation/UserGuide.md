# Keskeiset käyttötapaukset

Käymme tässä dokumentaatiossa läpi sovelluksen keskeiset käyttötapaukset ja samalla perehdymme sovellukseen koodin tasolla. Sovelluksen rakenne on jaetti osiin, jossa ensin kerrotaan osan käyttäjälle näkyvät toiminnallisuude ja tämän jälkeen käydään samat toiminnallisuudet läpi koodin tasolla. 

Huom! Sovelluksella on kolme eri käyttäjä luokkaa: USER, ADMIN, MASTER. Sovellukseen on luotu valmiiksi ADMIN ja MASTER käyttäjät (katso README.md) ja näillä luokilla on toiminnallisuuksia, jotka on rajattu pois "tavalliselta" USER käyttäjältä.

# Etusivu (yläpalkki)

* Kaikille käyttäjille (kirjautunut/kirjautumaton) näkyy tilastot keskustelufoorumista
  * Käyttäjien lkm
  * Viestiketjujen lkm
  * Viestien lkm
* Ulkoasuun liitetty kaksi kuvaa (Link + Mario), sijaitsevat /static/images/ hakemistossa

#### Koodi
* SQL kyselyt kutsutaan /views.py tiedoston funktiosta index()
* Jokaisesta kysely toteutettu staticmethod -funktiona joka sijaitsee /thread OR post OR auth/models.py
   * Kysely laskee yksinkertaisesti COUNT(*) kutsulla kyseisen tietotaulun rivien lukumäärän.

# Kirjautuminen, rekisteröinti ja käyttäjätiedot

* **Rekisteröidy (USER taso):** yläpalkki -> "Rekisteröidy": Syötä nimi, username, 2 x salasana 
  * **Validation:** Nimi: pituus (2,50), Username: pituus (2,20), Salasana: pituus (8,50), Salasanojen pitää täsmätä, username ei saa olla jo olemassa

* **Kirjaudu:** -> yläpalkki "Kirjaudu" 
  * Syötä username ja salasana
  * **Validation:** Virhe ilmoitus, jos käyttäjää + salasana yhdistelmää ei löydy tietokannasta 

* **Kirjaudu ulos:** yläpalkki -> Kirjaudu ulos -> redirect (viestiketjujen näkymä)

* **Omat tiedot:** yläpalkki Omat tiedot -> näkymä käyttäjä tiedoista
   * **Muuta Nimi:** Nimi -> Vaihda palkki -> validointi yhtenevä rekisteröinnin kanssa
   * **Muuta Käyttäjätunnus:** Käyttäjätunnus -> Vaihda palkki -> validointi yhtenevä rekisteröinnin kanssa
   * **Muuta Salasana:** Salasana -> Vaihda palkki -> validointi yhtenevä rekisteröinnin kanssa
   * **Poista käyttäjätili: Poistaa käyttäjätilin ja kaikki käyttäjän lähettäätä viestit.** Käyttäjän aloittamat viestiketjut säilytetään, mutta aloitusviestit poistetaan.
   
* **Hallinnoi käyttäjiä (ADMIN ja MASTER)**
  * Yläpalkki, Omat tiedot alla
  * **ADMIN**
     * Näkymä kaikista rekisteöidyistä USER käyttäjistä, mahdollisuus poistaa käyttäjä, poisto yhtenevä "Poista käyttäjätili" kanssa
  * **MASTER**
     * Sama kuin ADMIN, mutta USER käyttäjien lisäksi ADMIN käyttäjät näkymät
     * Mahdollistaa vaihtaa USER status ADMIN statukseksi tai päinvastoin

#### Koodi
* Koodi /auth/ hakemistossa
* Tehty omat SQL kyselyt (count_user_threads, count_user_posts) laskemaan kyseisen käyttäjän perustamien viestiketjujen ja viestien lukumäärän
  * näkyy Omat tiedot sivulla
* Oma validiation Form ja funktio nimen, käyttäjätunnuksen ja salasanan vaihtamiseen
* Materiaalin malliin nähden /root/init.py tiedoston user authentication funktioon (login_required) on tehty pieni muutos. Nyt funktiolla annetaan argumenttina lista käyttäjä rooleista, jotka sallitaan. Jos halutaan sallia ADMIN ja MASTER, annetaan funktiolle parametrina -> login_required(roles=["ADMIN", "MASTER"])
  * Authentication toimii mielestäni hyvin ja sitä käytetään joka puolella sovellusta
* Hallinoitaessa muita käyttäjiä, kutsutaan omia SQL kyselyitä list_users() tai list_users_and_admins(), joilla haetaan näytettävä data muista käyttäjistä.
* MASTER käyttäjä luodaan tietokannan perustamisen yhteydessä ja sitä ei voi poistaa (rajattu pois authenticationilla)
* Oman käyttäjän poistaminen ja ADMIN tai MASTER oikeudella toisen käyttäjän poistaminen on eritettty eri funktioiksi.
   * Oli minusta näin selkeämpää, esimerkiksi lopputilanteen käsittely kannalta ja estämällä MASTER poistamasta itseään yms.


# Viestiketjut (Threads)

* **Uusi viestiketju: (USER, ADMIN, MASTER)** yläpalkki -> "Aloita uusi keskustelu"
  * **Validation:** Otsikko (min 2, max 100 merkkiä), Viesti (min 2, max 4000 merkkiä), Kategoriat (täytyy valita vähintään yksi kategoria)
* **Näytä viestiketjut:** yläpalkki -> "Näytä keskustelut"
  * Viestiketjussa näkyy nimen lisäksi myös kategoriat ja ketjun viestien lkm
  * **Poista viestiketju: (ADMIN, MASTER)** Palkki viestiketjun otsikon perässä, **Poistaa viestiketjun ja kaikki ketjussa olevat viestit.**
  * **Muokkaa viestiketjun otsikkoa (ADMIN, MASTER):** Palkki viestiketjun otsikon perässä
    * **Validation:** Sama kuin ketjua luotaessa

* **Avaa viestiketju:**
    * klikkaa viestiketjun nimeä

#### Koodi
* Koodi /threads/ hakemistossa
* Thread, Category ja liitostaulu ovat kaikki samassa models.py
  * Netin mallissa näin, en onnistunut siirtämään Categoryä omaan kansioon
* Forms.py tiedostossa itse tehty validator, joka tarkistaa että vähintään yksi 7 kategoriasta on valittu ketjua luotaessa
* **"Näytä viestiketjut"** 2 x SQL kysely:
  * **get_default_threadList():** palauttaa listan listoja, jossa sisempi sisältää yhden Threadin tiedot (id, topic ja [catgegories])
    * Järjestetään lähetysajan mukaan
  * **post_count():** palauttaa listan listoja, joissa sisempi sisältää tiedot (Thread.id, Threadin viestien lkm)
    * Tässä tehdään haluttu "monimutkainen yhteenvetokysely" eli COUNT() ja GROUP BY
  * Ennen hmtl sivulle lähetystä tulokset yhdistetään vielä yhdeksi  
* **Avaa viestiketju** 2 x SQL kysely
  * **get_thread(threadId)** palauttaa listan avattavan Threadin tiedoista
  * **posts_in_thread(threadId)** palauttaa listan listoja, jossa sisemmällä aina yhden viestin tiedot
* Poistettaessa viestiketju (thread_remove) tehdään taas oma SQL kysely, jolla haetaan kaikki poistettavan viestiketjun viestit, jotka poistetaan myös että ne eivät jää täyttämään tietokantaa
* Koodissa on yritetty kommentoida tärkeimmät kohdat ja listojen yhteydessä on merkattu mitä mikäkin indeksi sisältää


# Viestit (Posts)
* Viesteissä näytetään lähettäjän käyttäjänimi, lähetysaika, ja itse viesti
  * Jos viestiä on muokataan, ilmestyy näkyviin myös muokkausaika
* **Uusi viesti (USER, ADMIN, MASTER):** Avaa viestiketju, palkki "Uusi viesti" sekä ketjun alussa että lopussa
  * Laitettu tahallaan sekä viestiketjun alkuun ja loppuun, jotta pitkän ketjun tapauksessa ei tarvitse rullata uudestaan loppuun
* **Muokkaa viestiä:** Avaa viestiketju, palkki "Muokkaa"
  * **USER:** omat viestit
  * **ADMIN ja MASTER:*** kaikki viestit
* **Poista viesti:** Avaa viestiketju, poista palkki viestin perässä
  * **USER:** omat viestit
  * **ADMIN ja MASTER:*** kaikki viestit
  
#### Koodi
* Koodi /posts/ hakemistossa
* Valitettavasti moment.js ei toiminutkaan viestien sisällä, vaikka sain sen toimimaan Omat tiedot sivulla (Ongelma str muotoisessa listassa vs suora current_user.created kutsu)
  * Viesteissä siis ruma Timestamp formaatti ja GTM aika
  * Omat tiedot sivulla kiva formaattu ja Suomen aika 
  
# Ulkoasu
* HTML templates hakemistossa /templates/
* CSS ja kuvat hakemistossa /static/
* Ulkoasuassa melko pelkistetty ja karkea tyyli
  * Koin tämän mielekkäämmäksi lähestymistavaksi, koska tämä pakotti minut oppimaan enemmän HTML/CSS:stä ensimäistä websovellustani tehdessä
  * Seuraavassa tulen käyttämään valmista kirjastoa, jolloin ulkoasustakin on helpompi saada nätimpi
  * Linkit on jätetty tahallaan sinisiksi
    * Koitin muita värejä + ei alle viivausta, mutta ainakin omaan silmään tämä yllätäen teki vaikeammaksi hahmottaa sovelluksen toimintaa näin ulkoasultaa karkeassa tapauksessa 
  




