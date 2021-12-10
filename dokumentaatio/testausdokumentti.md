# Testausdokumentti

## Yksikkötestaus

Yksikkötestaus suoritetaan automaattisesti unittestiä käyttäen.

### Sovelluslogiikka

Pienistä alkuluvuista vastaavaa `small_primes` -luokkaa testataan omassa luokassaan. `TestSmallprimes` -testiluokka vertaa `small_primes` -luokan `generate_list` -metodin tuottamaa listaa ja vertaa sitä tunnettuun listaan alkuluvuista.

RSA-avainparin generoimisesta vastaava `key_generator` -luokka testataan omassa luokassaan. `TestKeyGenerator` -testiluokka testaa alkuluvun etsimiseen tarkotettuja metodeja tunnetulla alkuluvulla sekä tunnetulla yhdistetyllä luvulla.

RSA-avaimen tallentamisesta ja hallinnoimisesta vastaava `rsa_key` -luokka testataan omassa luokassaan. `TestRsaKey` -testiluokka testaa avaimen moduluksen ja eksponentin palauttamista.

Viestin salaamisesta vastaava `encrypt` -luokka testaan omassa luokassaa. `TestEncrypt` -testiluokka testaa viestin salaamista ja salaamisoperaation eri vaiheita.

Salatun viestin purkamisesta vastaa `decrypt` -luokka testataan omassa luokassaan. `TestDecrypt` -testiluokka testaa viestin purkamista ja purkuoperaation eri vaiheita.

## Testikattavuus

Testien haarautumakattavuus on 94%. Raportista on jätetty ulkopuolelle käyttöliittymän koodi.

![coverage](https://github.com/ItsTuukka/RSA-salaus_tiralabra/blob/master/dokumentaatio/kuvat/rsa_coverage.png)

## Järjestelmätestaus

Sovellusta testattu järjestelmätasolla manuaalisesti oikeilla syötteillä, eikä ongelmia ole havaittu. Vääriin/viallisiin syötteisiin ei ole vielä varauduttu.

## Suorituskykytestaus

Suorituskykyä on testattu generoimalla eri pituisia avainpareja ja ottamalla keskiarvo kymmenestä suorituskerrasta. Sovelluksessa käytetään avaimen pituutena 2048 bittiä, joka on tällä hetkellä suositeltu pituus RSA-avaimelle. 

Avaimen pituus bitteinä | Keskiarvo (10 suorituskertaa)|
-----|----------|
1024 | 0,078s
2048 | 0,702s
4096 | 8,785s

## Testien suorittaminen

Ohjelman testit voi suorittaa komennolla

```
poetry run invoke test
```

Testikattavuusraportin saa luotua komennolla 

```
Raportti generoituu sovellus/htmlcov/index.html tiedostoon.

