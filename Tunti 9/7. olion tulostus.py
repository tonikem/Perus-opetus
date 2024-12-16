
# Olion tulostaminen onnistuu helposti, mutta se ei kerro oikein sen sisällöstä.
# Luodaan luokka, jolla on muuttujia ja sitten tehdään funktio __str__().
# Tämä metodi kutsutan aina kun luokasta otetaan str-olio, eli merkkijono.
# Katsotaan miten tämä onnistuu:
class Luokka:
    x = 1
    y = 3
    def __str__(self):
        return f"Luokka: x={Luokka.x} y={Luokka.y}"


olio = Luokka()
print(olio)
# Tulostus näyttää nyt paljon paremmalta.

