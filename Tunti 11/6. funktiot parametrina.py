
# Eräs ohjelmointiparadigma on nimeltään "Funktionaalinen ohjelmointi".
# Siinä yhtenä periaatteena on se, että funkitoita viedään eteenpäin parametreina.
# Alla esimerkki kahdesta funktiosta, joista ensimmäinen saa parametriksi toisen:
def funktio(funktio2):
    funktio2()

def funktio2(nimi="Jesse"):
    print("Nimi:", nimi)

funktio(funktio2)
# "funktio" ei tee mitään muuta kuin kutsuu funktiota "funktio2".
# "funktio2" tulostaa nimen. Näin funktioita voidaan siirrellä.

