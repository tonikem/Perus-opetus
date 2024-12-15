from pymupdf.table import snap_edges

# Sanakirjassa avaimen täytyy olla muuttumaton tietorakenne kuten merkkijono.
# Katsotaan miten käy, jos asetamme avaimeksi muuttuvan tietorakenteen, kuten listan:

sanakirja = dict()
lista = [1, 2, 3]
sanakirja[lista] = 0  # <- TypeError: unhashable type: 'list'
print("sanakirja:", sanakirja)
# print-funktiota ei koskaan suoriteta, koska ohjelma pysähtyy ennen sitä.

# Sama ongelma piilee muissa muuttuvissa tietorakenteissa.

# Hassuin esimerkki on käyttää yhtä sanakirjaa toisen avaimena:
sanakirja1 = dict()
sanakirja2 = dict()

sanakirja1[sanakirja1] = 24
print("sanakirja1:", sanakirja1)

# Sanakirjaa voi muutella kuten haluaa, joten se ei kelpaa avaimeksi.

