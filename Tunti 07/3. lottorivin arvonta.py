import random as r


arvotut_numerot = set()

while len(arvotut_numerot) < 7:
    uusi_numero = r.randint(1, 40)
    if uusi_numero in arvotut_numerot:
        continue
    else:
        arvotut_numerot.add(uusi_numero)


print("arvotut_numerot:", sorted(arvotut_numerot))


