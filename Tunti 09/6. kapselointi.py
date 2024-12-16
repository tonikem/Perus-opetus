
# Luokkien metodeja on joskus hyvä kapseloida, eli piilottaa:
class KapseloituLuokka:

    def __piilotettu_funktio(self):
        print("Piilotettua metodia kutsuttu.")

    def get(self):
        KapseloituLuokka.__piilotettu_funktio(self)


olio1 = KapseloituLuokka()
olio1.get()

olio2 = KapseloituLuokka()
olio2.__piilotettu_funktio()
# Viimeinen metodikutsu johtaa virheeseen, koska metodi on piilotettu.
# Vain luokan sisältä voidaan päästä käsiksi piilotettuun metodiin.

