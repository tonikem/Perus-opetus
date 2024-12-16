
# silmukassa on mahdollista käyttää else-avainsanaa.

lista = []

for item in lista:
    print("item:", item)
else:
    print("Tämä tulostetaan kuitenkin.\n")


lista = [1, 6, 9]

for item in lista:
    print("item:", item)
else:
    print("Tämä tulostetaan kuitenkin.\n")


lista = [3, 5, 9, 6, 1]

for x in lista:
    if x % 2 == 0:
        print("löytyi parillinen", x)
        break  # <- Tässä kohtaa poistutaan silmukasta, joten else-osio ei tee mitään.
else:
    print("ei löytynyt parillista.")


