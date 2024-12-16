

# Otetaan esimerkki, jossa luetaan luku käyttäjältä:
x = int(input("Anna kokonaisluku: "))

# Sitten katsotaan mikä on jakojäännös modulo 2 jälkeen:
if x % 2 == 0:
    print("parillinen")
else:
    print("pariton")

# Tämä on hyvä tapa tarkistaa onko luku parillinen, mutta koodia on mahdollista lyhentää:
print("parillinen" if x % 2 == 0 else "pariton")

# Myös funktio on mahdollista tiivistää yhdelle riville:
def funktio(): return "Moi"

print(funktio())



