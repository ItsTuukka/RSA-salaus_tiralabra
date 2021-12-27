# Käyttöohje

Ohjelma on toteutettu ja testattu Python versiolla 3.8.

## Ohjelman käynnistäminen

Lataa ohjelma [täältä](https://github.com/ItsTuukka/RSA-salaus_tiralabra/releases/tag/v.1.0). Mene ohjelman hakemistossa `sovellus` -kansioon ja asenna riippuvuudet komennolla:

```
poetry install
```

Nyt voit käynnistää sovelluksen komennolla:

```
poetry run invoke start
```

Ohjelman muut komentorivikomennot löydät [README](https://github.com/ItsTuukka/RSA-salaus_tiralabra#readme) -tiedostosta ja ne kaikki suoritetaan `sovellus` -kansiossa.

## Käyttöliittymä

Ohjelman käyttöliittymä näyttää tältä:

![ui](https://github.com/ItsTuukka/RSA-salaus_tiralabra/blob/master/dokumentaatio/kuvat/ui.png)

## Ohjelman käyttäminen

1. Luo avainpari. 
  - Syötä haluttu avaimen pituus. 
      - Syöte pitää olla luku 500-5000 väliltä. 
      - Ohjelma ilmoittaa vääristä syötteistä.
  - Paina nappia `Luo avainpari`.
  - Ohjelma ilmoittaa avainten onnistuneesta luonnista.

2. Salaa haluttu viesti.
  - Syötä viesti, jonka haluat salata.
      - Ohjelma ilmoittaa, jos viestiä ei voi salata.
  - Onnistuneesti salattu viesti tulee salattuna näkyviin `Salattu viesti` laatikkoon ja automaattisesti kopioidaan purettavaksi.

3. Pura salattu viesti.
  - Syötä salattu viesti, tämä boksi täyttyy automaattisesti kun salaat viestin.
      - Ohjelma ilmoittaa, jos vietiä ei voida purkaa.
  - Onnistuneesti purettu viesti tulee näkyviin `Purettu viesti` laatikkoon

Voit poistua ohjelmasta painamalla oikeassa yläkulmassa olevaa punaista raksia.
