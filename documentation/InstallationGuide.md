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
