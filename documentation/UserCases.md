# Keskeiset käyttötapaukset

Sovelluksen käyttö ja toiminnallisuuksien toteutus tapahtuu "yläpalkissa" olevien nimettyjen linkkien avulla ja tutkittavalla sivulla aukeavien toiminnallisuuksien kautta. Alla on kuvattu reittit tällä hetkellä toteutettujen toiminnallisuuksien suorittamiseen. 

# Authentication/Login (Kirjautuminen ja käyttäjä)
* **Rekisteröidy:** yläpalkki "Rekisteröidy" -> Syötä nimi, username, 2 x salasana (Nimi pituus (2,50), Username pituus (2,20), Salasana pituus (8,50), Salasanojen pitää täsmätä, username ei saa olla jo olemassa) -> "Rekisteröidy" -> redirect (Kirjaudu)

* **Kirjaudu:** yläpalkki "Kirjaudu" -> Syötä username, salasana (Virhe ilmoitus, jos käyttäjää + salasana yhdistelmää ei löydy tietokannasta) -> "Kirjaudu" -> redirect (Threads list) 

* **Kirjaudu ulos:** yläpalkki Kirjaudu ulos -> redirect (Threads list) 

# Threads (Viestiketjut)
* **Uusi viestiketju:** yläpalkki "Aloita uusi keskustelu" -> Otsikko (min 2, max 100 merkkiä), -> "Luo viestiketju" -> redirect (Threads List)
* **Listaa viestiketjut:** yläpalkki "Näytä keskustelut"
  * **Poista viestiketju:** Palkki viestiketjun otsikon perässä
  * **Muokkaa viestiketjua (otsikko)** Palkki viestiketjun otsikon perässä, Otsikko (min 2, max 100 merkkiä), näkymä vanhaan otsikkoon
