

# Toistaiseksi ei olla paneuduttu virheiden käsittelyyn.
# Se on kuitekin yksi tärkeimmistä aiheista ohjelmoinnissa.
# Kokeillaan seuraavaksi perinteistä nollalla jakamista:
x = 1
y = 0
print(x / y)
# Näytölle tulostuu: "ZeroDivisionError: division by zero"

# Mikä neuvoksi? Ohjelma ei pysty jatkamaan ilman virheen käsittelyä.
# Kokeillaan ottaa virhe kiinni omassa lohkossaan:
try:
    print(x / y)
except ZeroDivisionError:
    print("Nollalla ei voi jakaa!")

# except-avainsanaa seuraa "ZeroDivisionError", mutta se vaidaan jättää poiskin:
try:
    print(x / y)
except:
    print("Nollalla ei voi jakaa!")

# Nyt kuitenkin try-except tarkistaa kaikki virheet ja antaa vastaukseksi "Nollalla ei voi jakaa!",
# vaikka virhe ei koskisikaan nollalla jakamista. On siis hyvä määrittää virhetyyppi try-except kohdalla.


# Virheitä useimmiten tarkistetaan ketjuttamalla tarkistuksia:
try:
    print(x / y)
except ZeroDivisionError:
    print("Nollalla ei voi jakaa!")
except IndexError:
    print("Indeksi on väärin")
except IndentationError:
    print("Lohkon sisennys on väärin")
except BufferError:
    print("Puskuri ylivuotaa!")

# Virheilmoituksiin voi tutustua linkistä: https://www.tutorialsteacher.com/python/error-types-in-python

