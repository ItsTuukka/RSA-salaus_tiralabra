# Määrittelydokumentti

## Projekti

Toteutan projektina ohjelman, joka käyttää RSA-salausta viestin salaamiseen. Salaus perustuu isojen alkulukujen muodostamiseen ja niillä tiettyjen laskutoimitusten tekemiseen.

Valitsin RSA-salauksen projektin aiheeksi, koska aivan pintapuolista raapaisua lukuunottamatta, se on minulle täysin uusi aihe ja se vaikuttaa mielenkiintoiselta. Tavoitteena on tuottaa ohjelma joka saa syötteeksi viestin, jonka se salaa, sekä pystyy purkamaan alkuperäiseen muotoonsa.

## Projektin kielet

Projektin ohjelmointikielenä toimii Python ja dokumentaatio kielenä Suomi. En tällä hetkellä hallitse muita ohjelmointi kieliä. Englanti on hyvin hallussa, joten vertaisarviointi onnistuu myös sillä.

## Projektissa käytettävät algoritmit ja tietorankeet

### Tietorakenteet

RSA-salaus perustuu erittäin suurien alkulukujen löytämiseen, eikä projektissa tarvita suurempia tietorankentaita kuin yksittäisiä muuttujia.

### Algoritmit

- Miller-Rabin algoritmi
  - Tarkka testi joka tarkistaa, onko käsiteltävä luku alkuluku vai ei.
  - Algoritmi käy testattavan luvun läpi k kertaa, ja todennäköisyys että testin hyväksymä luku ei ole alkuluku on 4^-k.

- Eratostheneen seula
  - Luo kaikki alkuluvut parametriin n asti.
 
## Tavoitteena olevat aikavaativuudet

- Miller-Rabin algoritmi
  - Aikaavituus: O(k log^3 n), missä k on läpikäyntien määrä ja n on testattava luku.

- Eratostheneen seula
  - Aikavaativuus: O(n log log n), missä n on luku johon asti alkulukuja generoidaan.

## Opinto-ohjelma

Opiskelen tietojenkäsittelytieteen kandidaatin tutkintoa (TKT).

## Lähteet

- https://en.wikipedia.org/wiki/RSA_(cryptosystem)
- https://en.wikipedia.org/wiki/Primality_test
- https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test
- https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
