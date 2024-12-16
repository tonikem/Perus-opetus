
# Setti alustetaan seuraavasti:
setti = set()
setti.add("Toni")
setti.add("Veeti")
setti.add("Tuomo")
print("setti:", setti, '\n')

# Setillä ei oletuksena ole järjestystä.
# Se on myöskin muuttuva tietorakenne, eli ei kelpaa avaimeksi.


# Looppaaminen onnistuu näin:
for nimi in setti:
    print("nimi:", nimi)
print()


# Setti käy myös merkkijonojen tarkisteluun:
if "x" in {"x", "y", "z"}:
    print("X löytyy setistä!")

