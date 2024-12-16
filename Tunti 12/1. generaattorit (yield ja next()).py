
# yield-avainsanaa voidaan käyttää generaattorin määrittelyssä.
# Esim. "laskuri" tuottaa lukuja niin pitkään kuin maksimi saavutetaan.
def laskuri(maksimi):
    luku = 0
    while luku <= maksimi:
        yield luku
        luku += 1

# funktion "laskuri" kutsuminen palauttaa generaattorin:
luvut = laskuri(2)
print("Eka arvo:", next(luvut))
print("Toka arvo:", next(luvut))
print("Kolmas arvo:", next(luvut))

# Maksimin saavutettua "next()" tuottaa virheilmoituksen:
print("Neljäs arvo:", next(luvut))


# Kätevämpi tapa on käyttää for-looppia:
luvut = laskuri(5)
for luku in luvut:
    print("luku:", luku)


