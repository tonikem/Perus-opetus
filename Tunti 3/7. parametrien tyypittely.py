
## Linkkejä tyypittelyyn liittyen:
# - https://docs.python.org/3/library/typing.html
# - https://stackoverflow.com/questions/2489669/how-do-python-functions-handle-the-types-of-parameters-that-you-pass-in


def funktio(x: int, y: float, z: str):
    print(x, y, z)

# Kutsutaan funktiota:
funktio(1, 2.5, "merkkijono")

# Merkkijonojen tulostus ei epäonnistu muulla kuin string-arvolla, mutta IDE antaa varoituksen:
funktio(1, 2.5, True)
funktio(1, 2.5, 3.14)


# Luodaan uusi funktio, mutta tällä kertaa tarkistetaan z-muuttujan tyyppi:
def funktio(x: int, y: float, z: str):
    if not isinstance(z, str):
        raise TypeError("Tämä tuottaa virheilmoituksen.")
    print(x, y, z)


# Kutsutaan funktiota (epäonnistuu):
funktio(1, 2.5, 3.14)


