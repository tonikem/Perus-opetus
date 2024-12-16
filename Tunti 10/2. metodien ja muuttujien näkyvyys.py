
# Myös muuttujia voidaan kapseloida:
class Luokka:
    def __init__(self, nimi):
        self.__nimi = nimi # <- privaatti muuttuja.

    def get_nimi(self):
        return self.__nimi


olio = Luokka("Jussi")
print(olio.__nimi) # <- Johtaa virhetilanteeseen.
# Ainoa tapa päästä käsiksi olion muuttujaan on käyttää metodeja:

olio = Luokka("Jussi")
print("olio.get_nimi():", olio.get_nimi())

