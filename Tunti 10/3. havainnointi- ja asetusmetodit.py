
# Yksi Python-kielen erikoisuus on asetus- ja havainnointimetodit.
# Niistä esimerkki alla:
class Lompakko:
    def __init__(self):
        self.__rahaa = 0 # <- privaattimuuttuja.

    # Havainnointimetodi
    @property
    def rahaa(self):
        return self.__rahaa

    # Asetusmetodi
    @rahaa.setter
    def rahaa(self, rahaa):
        if rahaa >= 0:
            self.__rahaa = rahaa


olio = Lompakko()
print("olio.rahaa:", olio.rahaa)

olio.rahaa = 30.50
print("olio.rahaa:", olio.rahaa)

# Nyt rahaa-muuttujaa voidaan muutella viittaamalla suoraan muuttujaan.


