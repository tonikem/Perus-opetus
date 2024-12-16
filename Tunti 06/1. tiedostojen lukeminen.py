

# Tiedostoja luetaan "open()" funktiolla.
# Yksi tapa avata tiedosto on tämä:
tiedosto = open("1. tiedostojen lukeminen.py")
print(tiedosto.read())
tiedosto.close() # <- Muista sulkea teidosto.
print()

# Aika hassua. Nyt olemme avanneet nykyisen tiedoston ja sisältö on tulostettu terminaaliin.
# Tiedoston voi myös avata with-avainsanalla:
with open("1. tiedostojen lukeminen.py") as tiedosto:
    print(tiedosto.read())
    # with-avainsanan käyttö ei edellytä tiedoston sulkemista erikseen.
    # Tiedosto sulkeutuu kun tullaan ulos lohkosta.
# Eli nyt.
print()

# Tiedoston sisältö voidaan lueka myös rivi kerrallaan:
with open("1. tiedostojen lukeminen.py") as tiedosto:
    for line in tiedosto:
        # Tarkistetaan, että rivi alkaa #-merkillä
        if line[0] == '#':
            # Tulostetaan ilman välilyöntejä ja "\n"-merkkiä "strip()" metodilla:
            print(line.strip())

