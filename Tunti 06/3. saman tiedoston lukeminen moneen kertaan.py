

tiedosto = open("tiedosto.csv")
print(tiedosto.read())
print(tiedosto.read())
tiedosto.close()

# print-fuktioita on kaksi, mutta CSV tulostuu vain kerran. Mikä mättää?
# Syy on siinä miten tiedostojen käsittely toimii pythonissa.
# Sisällön voi lukea vain kerran, jonka jälkeen tulostuu tyhjää.
# Siksi onkin hyvä lukea tiedoston sisältö johokin muuttujaan talteen.


# Tiedosto voidaan kuitenkin lukea kahteenkin kertaan.
tiedosto1 = open("tiedosto.csv")
tiedosto2 = open("tiedosto.csv")
#print(tiedosto1.read())
#print(tiedosto2.read())

# Yleensä tämä ei ole hyvä käytäntö. Lisää tästä myöhemmillä tunneilla.


