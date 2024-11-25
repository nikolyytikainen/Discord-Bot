# discordBot
Yksinkertainen discord botti, joka on vielä kehitysvaiheessa. Botti hakee mm. Counter-Strike 2 pelin kolmannen osapuolen faceit-palvelusta pelaajan datan ja esittelee dataa, kun bottia kutsutaan komennolla.
## Käytössä olevia "järkeviä" komentoja:
*   !faceitstats (pelaajan nimi) : Hakee faceit-palvelusta pelaajan datan ja näyttää pelaajan elopisteet, voitto%, pelattujen otteluiden määrän, K/D ration, viiden viimesimmän ottelun tuloksen.
*   !faceitfinder (steamcommunity profile url) : Hakee faceit-palvelusta pelaajan datan steamcommunity profiilin urlin avulla ja näyttää pelaajan elopisteet, voitto%, pelattujen otteluiden määrän, K/D ration, viiden viimesimmän ottelun tuloksen.
*   !noppa : perinteinen noppaheitto, arpoo luvun 1-6.
*   !kolikko : Kruuna vai klaava?
*   !casesimu : Case opening simulaattori, jossa samat prosentuaaliset mahdollisuudet avata "esineitä", kuin Counter Strike 2 pelissä.
*   !casestats : Näyttää avattujen laatikoiden määrän, sekä montako mitäkin harvinaisuutta on avattu.
### Asennus
Jos haluat asentaa tämän botin, sinun täytyy ensin luoda oma [Discord Bot](https://discord.com/developers/applications) ja kirjautua tai luoda käyttäjä [Faceit developer palveluun](https://developers.faceit.com/), sekä luoda oma apikey. 

1. Repositorion kloonaus
2. Projektin avaaminen esim. Visual Studio Code
3. Dependencies asennus
   - pip install discord.py
   - pip install requests
4. Faceit apikey sekä discord botin token
   - luo .env tiedosto sekä luo discordToken ja faceitApiKey tässä muodossa `discordToken = YOUR_DC_TOKEN` ja `faceitApiKey = YOUR_FACEIT_APIKEY`
   - Discord botin token ja botti [Discord developers](https://discord.com/developers/applications)
   - Faceit apikey [Faceit developers](https://developers.faceit.com/)
5. Suorita ohjelma
#### Tiedetyt ongelmat
*   !faceitfinder ei löydä faceitprofiilia, jos steamcommunity profiilin urlissa on id. Esim. https://steamcommunity.com/id/testAccount1233312321
