

summa = 0

while True:
    luku = int(input("Anna luku (0 murtaa silmukan): "))

    if luku == 0:
        break

    if luku >= 10:
        print("Lukua ei tallenneta, koska kutsutaan \"continue\"")
        continue

    summa += luku


print ("summa:", summa)


