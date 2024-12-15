
# Virheitä voi nostaa raise-avainsanalla.
# Esim:

def funktio():
    raise InterruptedError("Oma virheviesti.")
    print("Tätä ei tulosteta..")

funktio()

# Kuten huomataan, ei mitään tulostu ruudulle virheilmoituksen jälkeen.
# Tähän syynä on se, että virheiden on tarkoitus pysäyttää suoritus.
# Ei olisi mielekästä, jos jonkin virheen annettaisiin pysyä järjestelmässä ilman keskeytystä.
# Virheet joudutaan käsittelemään tavalla tai toisella.


