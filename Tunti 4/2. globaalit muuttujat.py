
## Globaalit muuttujat ovat vaarallisia.
## Niiden käyttöä tulee välttää, jos mahdollista.

## Esimerkki globaalista muuttujasta:
muuttuja = 3 # <- Näin ylös (riville 6) sijoitettu muuttuja on kaikkien käytössä.


# Parametri on kirjoitettu väärin alla olevassa funktiossa.
def funktio(muutuja):
    print("funktio:", muuttuja)
    # Tämän takia tulostuukin globaali muuttuja. Globaali muuttuja voi häiritä ohjelman toimintaa
    # ja sitä voi käyttää mistä tahansa, joten arvo voi heitellä epätoivotulla tavalla.


x = 42
funktio(x)

# Paras tapa on aina merkata globaalin muuttujan käyttö seuraavasti:
def funktio2():
    global muuttuja
    # Muutetaan globaalin muuttujan arvoa.
    muuttuja = 24
    print("funktio2:", muuttuja)


funktio2()


# Sitten tulostetaan muuttujan arvo:
print("muuttuja:", muuttuja)
# Huomataan, että arvo on muuttunut.


# Kokeillaan vielä muuttaa arvoa ilman global-avainsanaa:
def funktio3():
    muuttuja = 78
    print("funktio3", muuttuja)


funktio3()

# Sitten tulostetaan muuttujan arvo:
print("muuttuja:", muuttuja)
# Tässä huomataan, että globaalin muuttujan arvo ei ole muuttunut funktion ulkopuolella.


