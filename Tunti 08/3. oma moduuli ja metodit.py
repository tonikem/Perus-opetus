
# Oma moduuli importataan samoin kuin muutkin moduulit:
from utils import yhteenlasku, vähennyslasku,kertolasku

# Myös on mahdollista käyttää wildcard-muotoa "*":
from utils import *


# Näytölle tulostuu lause "Tämä tulostuu aina kun moduuli importataan.."
# Kuitenkaan seuraava tulostus, "Tämä tulostuu vain, jos utils.py on pääohjelma.", ei näy importatessa.


# Nyt voimme käyttää oman moduulin funktioita:
print(yhteenlasku(1, 3))
print(vähennyslasku(2, 9))
print(kertolasku(2, 1))


