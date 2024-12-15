# Tuodaan ensin random-kirjasto:
import random as r

# Nyt voimme käyttää satunnaisuutta koodissamme:
print(r.random()) # <- Tulostaa luvun 0-1 väliltä.

# choice-funktiolla voidaan valita satunnainen alkio:
lista = ['a', 'b', 'c', 'd']
print(r.choice(lista))

# seed-arvon asettaminen poistaa satunnaisuuden:
r.seed(42)
print(r.randint(0, 10))
# Nyt satunnaisuus ei enää toimi, koska siemenarvo on aina sama.
# Siksi siemenarvon tulisi olla jokin muuttuva arvo.

# Satunnaisuus palautuu kun siemenarvo on eri joka kerralla.
# Esim. ajan käyttö toimii tässä hyvin:
import time as t
siemen = t.time()

r.seed(siemen)
print(r.randint(0, 10))
# Ja nyt satunnaisuus toimii taas!


# random-kirjastolla voidaan myös sekoittaa listoja:
sanat = ["omena", "banaani", "appelsiini"]
r.shuffle(sanat)
print("sanat:", sanat)


# Lisää tietoa: https://www.random.org/randomness

