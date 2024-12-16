

# Moduuleja tarvitaan, kun ei haluta keksiä pyörää uudelleen.
# Esim. voitaisiin tehdä keskiarvon laskeva ohjelma sum- ja len-funktioilla.
# On kuitenkin mahdollista suorittaa se valmiilla kirjastolla "statistics":

import statistics

# Nyt kirjastoa voidaan käyttää vaikkapa listan keskiarvon laskemiseen:
print(statistics.mean([1, 3, 5, 7, 9, 11, 13]))

# Melko yleinen kirjasto on "math". Siitä saa esim. piin likiarvon:

import math
print(math.pi)

# Muita yleisiä kirjastoja ovat "sys" ja "os":
import os, sys
print("sys.version:", sys.version) # <- Tulostaa python tulkin version
print("os.curdir:", os.curdir) # <- Tulostaa nykyisen hakemiston "."

