# Aikaa voidaan myös vertailla:
from datetime import datetime

nyt = datetime.now()
juhannus = datetime(2020, 6, 20)

if nyt < juhannus:
    print("Ei ole vielä juhannus")
elif nyt == juhannus:
    print("Hyvää juhannusta!")
elif nyt > juhannus:
    print("Juhannus on mennyt")


# Aikaeron vertailu tapahtuu parhaiten "timedelta"-metodilla:
from datetime import timedelta
juhannus = datetime(2020, 6, 20)

viikko = timedelta(days=7)
viikon_paasta = juhannus + viikko
print("Kun viikko juhannuksesta kuluu on", viikon_paasta)

pitka_aika = timedelta(weeks=32, days=15)
print("Kun juhannuksesta kuluu 32 viikkoa ja 15 päivää on", juhannus + pitka_aika)


# Ero kellonajassa on mahdollista tarkistaa näin:
nyt = datetime.now()
keskiyo = datetime(nyt.year, nyt.month, nyt.day, hour=0, minute=0, second=0)
erotus = keskiyo - nyt
print(f"keskiyöhön on vielä {erotus.seconds} sekuntia.")


