# RSA-salaus

Helsingin yliopiston Aineopintojen harjoitustyö: Tietorakenteet ja algoritmit

## Dokumentaatio

- [Määrittelydokumentti](https://github.com/ItsTuukka/RSA-salaus_tiralabra/blob/master/dokumentaatio/maarittelydukumentti.md)
- [Testausdokumentti](https://github.com/ItsTuukka/RSA-salaus_tiralabra/blob/master/dokumentaatio/testausdokumentti.md)
- [Toteutusdokumentti](https://github.com/ItsTuukka/RSA-salaus_tiralabra/blob/master/dokumentaatio/toteutusdokumentti.md)
- [Käyttöohje](https://github.com/ItsTuukka/RSA-salaus_tiralabra/blob/master/dokumentaatio/kayttoohje.md)

## Viikkoraportit

- [Viikko 1](https://github.com/ItsTuukka/RSA-salaus_tiralabra/blob/master/dokumentaatio/viikkoraportti1.md)
- [Viikko 2](https://github.com/ItsTuukka/RSA-salaus_tiralabra/blob/master/dokumentaatio/viikkoraportti2.md)
- [Viikko 3](https://github.com/ItsTuukka/RSA-salaus_tiralabra/blob/master/dokumentaatio/viikkoraportti3.md)
- [Viikko 4](https://github.com/ItsTuukka/RSA-salaus_tiralabra/blob/master/dokumentaatio/viikkoraportti4.md)
- [Viikko 5](https://github.com/ItsTuukka/RSA-salaus_tiralabra/blob/master/dokumentaatio/viikkoraportti5.md)
- [Viikko 6](https://github.com/ItsTuukka/RSA-salaus_tiralabra/blob/master/dokumentaatio/viikkoraportti6.md)

## Release

Löydät sen täältä [täältä](https://github.com/ItsTuukka/RSA-salaus_tiralabra/releases/tag/v.1.0).

## Komentorivikomennot (suoritetaan sovellus kansiossa)

#### Riippuvuuksien asennus

```
poetry install
```

#### Ohjelman voi suorittaa komennolla 

```
poetry run invoke start
```

#### Ohjelman testit voi suorittaa komennolla

```
poetry run invoke test
```

#### Testikattavuusraportin saa luotua komennolla

```
poetry run invoke coverage-report
```

Raportti generoituu sovellus/htmlcov/index.html tiedostoon.

#### Pylint tarkistus komennolla

```
poetry run invoke lint
```
