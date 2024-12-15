

merkkijono = "Tämä on merkkijono"


# Tulostetaan kaikki paitsi ensimmäinen kirjain:
print("merkkijono[1:]:", merkkijono[1:])


# Tulostetaan 4 ensimmäistä kirjainta:
print("merkkijono[0:4]:", merkkijono[0:4])


# Tulostetaan osajono väliltä 8-18:
print("merkkijono[8:18]:", merkkijono[8:18])


# Tulostetaan koko merkkijono:
print("merkkijono[:]:", merkkijono[:])


# Tulostetaan viimeiset 4 kirjainta:
print("merkkijono[-4:]:", merkkijono[-4:])


# Tulostetaan merkkijono eri järjestyksessä:
print("merkkijono[::-1]:", merkkijono[::-1])


# Koitetaan muuttaa merkkijonoa. Se epäonnistuu.
merkkijono[0] = 'A'

# Merkkijonot ovat muuttumaton tietorakenne.
# Niiden alkioita ei voi muuttaa.


