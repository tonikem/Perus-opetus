

# Tutustutaan self-avainsanan käyttöön:
class Luokka:
    def __init__(self, nimi, ikä):
        self.nimi = nimi
        self.ikä = ikä

# Luokka siis ottaa vastaan kaksi muuttujaa, jotka tallennetaan
# luokan konstruktorissa sitä kutsuvalle oliolle.

# Olio luodaan siis näin:
olio = Luokka("Henna", 32)
# Olio saa arvot luokalta. Sitten ne voidaan käyttää:
print("olio.nimi:", olio.nimi)
print("olio.ikä: ", olio.ikä)

