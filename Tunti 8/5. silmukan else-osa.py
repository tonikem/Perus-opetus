
# silmukassa on mahdollista käyttää else-avainsanaa.

lista = []

for item in lista:
    print("item:", item)
else:
    print("Lista oli tyhjä, ei printattavaa..")


lista = [3, 5, 9, 7, 1]

for x in lista:
    if x % 2 == 0:
        print("löytyi parillinen", x)
        break
else:
    print("ei löytynyt parillista.")


