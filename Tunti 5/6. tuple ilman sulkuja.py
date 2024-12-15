
# Tuple voidaan esittää myös ilman sulkuja:
x = 1, 2, 3
print("x:", x)


# Tuple ilman sulkuja(tai niiden kanssa) on yleinen tapa palauttaa funktiolta useita arvoja kerralla:
def tuple_funktio(x, y):
    yhteenlasku = x + y
    vähennyslasku = x - y
    return yhteenlasku, vähennyslasku

# Tuple puretaan seuraavasti muuttujiin:
yhtlasku, vählasku = tuple_funktio(1, 2)
print("yhteenlasku:", yhtlasku)
print("vähennyslasku:", vählasku)


