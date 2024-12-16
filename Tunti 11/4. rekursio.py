

# Tähän mennessä on opittu luomaan omia funktioita.
# Näissä funktioissa on mahdollista kutsua muita funktiota.

# Mikä saattaa yllättää on se, että funktio voi myös kutsua itseään:
def funktio():
    print("Rekursiivinen funktio")
    funktio()


funktio()
# Tämä johtaa virheeseen: "RecursionError: maximum recursion depth exceeded"
# Virhe tulee koska Python ei anna rekursion jatkuvan loputtomiin.


