
# Yksinkertainen luokka esimerkki:
class MinunLuokka:
    pass

# Luokasta voidaan tehdä instanssi:
olio = MinunLuokka()
print(olio)  # "<__main__.MinunLuokka object at 0x000002782B5E70E0>"
# Tulostus näyttää mm. sen missä muistiosoitteessa olio sijaitsee.


# Luokkaan voidaan lisätä muuttujia näin:
class ToinenLuokka:
    x = 3

# Nyt voidaan tulostaa muuttuja luokkaviittauksen avulla:
print("ToinenLuokka.x:", ToinenLuokka.x)


