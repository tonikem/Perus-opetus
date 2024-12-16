
# Rekursiota käytettäessä tarvitaan paluuarvoja:
def kertoma(luku: int | float):
    if luku < 2: return 1
    return luku * kertoma(luku - 1)


print("kertoma(9):", kertoma(9))
print("kertoma(30.5):", kertoma(30.5))


