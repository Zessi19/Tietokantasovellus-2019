# Installation Guide

Lyhyt opas projectin käyttämän python virtuaaliympäristön asentamiseen ja projektin käynnistämiseen.
<br/><br/>

**1.** Ladataan GitHub projekti zip-tiedostona, puretaan se paikallisti ja mennään sovelluksen juurihakemistoon
  * unzip -a file_name.zip
  
**2.** Luodaan virtuaalinen python ympäristö (project root)
  * python3 -m venv venv
  
**3.** Aktivoidaan virtuaaliympäristö (project root)
  * source venv/bin/activate
  
**4.** Asennetaan virtuaaliympäristöön sovelluksen käyttämät kirjastot (project root)
  * pip install -r requirements.txt
 
**5.** Käynnistetään sovellus (project root)
  * python3 run.py
  
 Sovellus toimii root/init.py tiedoston määrityksen vuoksi sekä paikallisesti SQLAlchemyä sekä Herokussa Postgres hallintaohjelmaa käyttäen. Herokun käyttöön kannattaa tutustua tarkkemmin itse saitin kautta, mutta lyhyesti todettuna git:n käyttöönoton ja Heroku tunnusten jälkeen sovellus saadaan Herokuun:
 
 /root/
 
 * **1:** heroku config:set HEROKU=1
 * **2:** heroku addons:add heroku-postgresql:hobby-dev
 * **3:** git add .
 * **4:** git commit -m "Add Heroku"
 * **5:** git push heroku master
 * **Bonus:** Resetoi Heroku tietokanta: heroku pg:reset DATABASE_URL
