
# Aikaa on mahdollista muotoilla asettamalla tietynlainen merkkijono:
from datetime import datetime
aika = datetime.now()
print(aika.strftime("%d.%m.%Y"))
# %d = päivä
# %m = kuukausi
# %y = vuosi


# Voimme järjestää aikaa miten tahansa:
aika = datetime.now()
print(aika.strftime("%Y-%m-%d__%H-%M-%S"))

# Lisää aikamoduulista: https://docs.python.org/3/library/time.html#time.strftime

