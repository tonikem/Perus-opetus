
# Tehdään sitten luokka, jossa on metodeja (luokan funktioita):
class Luokka:

    def luokan_metodi(self): # <- self-sana on pakko lisätä, että metodi toimii.
        print(f"Tulostetaan luokan nimi: \"{self.__class__.__name__}\"")

    def toinen_metodi(self):
        print("Tämä on toinen metodi")


olio = Luokka()
olio.luokan_metodi()
olio.toinen_metodi()


# self-avainsanan toimintaan palataan seuraavalla tunnilla.
# Tarvitsee vain tietää, että se viittaa Luokasta tehtyyn olioon.

