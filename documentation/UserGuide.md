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

* **Uusi viestiketju:** yläpalkki "Aloita uusi keskustelu" -> Otsikko (min 2, max 100 merkkiä), Viesti (min 2, max 4000 merkkiä) -> "Luo viestiketju" -> redirect (Threads List)
* **Näytä viestiketjut:** yläpalkki "Näytä keskustelut"
  * **Poista viestiketju:** Palkki viestiketjun otsikon perässä, **Poistaa viestiketjun ja kaikki ketjussa olevat viestit.**
  * **Muokkaa viestiketjua (otsikko):** Palkki viestiketjun otsikon perässä, Otsikko (min 2, max 100 merkkiä), näkymä vanhaan otsikkoon

* **Avaa viestiketju:** klikkaa viestiketjun nimeä


# Posts (Viestit)
* **Uusi viesti:** Avaa viestiketju, palkki "Uusi viesti" sekä ketjun alussa että lopussa
* **Muokkaa viestiä:** Avaa viestiketju, palkki "Muokkaa"
* **Poista viesti:** Avaa viestiketju, poista palkki viestin perässä -> redirect(viestiketju)



