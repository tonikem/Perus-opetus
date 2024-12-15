
# Tiedostoon kirjoittaminen on yhtä helppoa kuin lukeminen.
# Tarvitaan vain "w" parametri, joka on lyhenne sanasta "write"
tiedosto = open("uusi_tiedosto.txt", 'w')
tiedosto.write("Moi kaikille!")
tiedosto.close()

# Yllä oleva koodi pyyhkii tiedoston tyhjäksi ja sitten kirjoittaa.
# Jos halutaan lisätä uusia tekstirivejä, täytyy käyttää toista parametria "a" niin kuin "append".
tiedosto = open("uusi_tiedosto.txt", 'a', encoding="UTF-8") # <- Täytyy olla UTF-8, jotta ääkköset näkyvät.
tiedosto.write("\nTämä tulostuu toiselle riville.")
tiedosto.close()


# Nyt tiedostossa on kaksi riviä.
# Lisää tietoa seuraavasta linkistä:
# https://www.programiz.com/python-programming/methods/built-in/open


