
# Ajan käsittely on yksi tärkeimmistä asioista ohjelmoinnissa.
# Aikaa voidaan käsitellä monella eri tavalla ja yksiköllä.
# Päivien käsittelyyn toimii moduuli "datetime":

from datetime import datetime

aika = datetime.now()
print(aika) # <- Tulostaa päivän ja kellonajan.


# Aikaoliota voidaan käyttää jonkin hetken esittämiseen:
aika = datetime(1952, 12, 24)
print(aika) # <- Vuosi on 1952. Kellonaikaa ei olla määritelty.






