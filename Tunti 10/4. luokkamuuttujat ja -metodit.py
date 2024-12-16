

class MinunLuokka:
    luokka_muuttuja = 12

    def __init__(self):
        pass

    @classmethod
    def luokka_metodi(cls): # <- Huomaa, että self-sanaa ei tässä käytetä.
        print(f"Tämä on metodi luokalle: \"{cls.__name__}\"")


# Luokkametodia voidaan kutsua olion tai luokan viittauksen kautta:
olio = MinunLuokka()
olio.luokka_metodi()
MinunLuokka.luokka_metodi()


