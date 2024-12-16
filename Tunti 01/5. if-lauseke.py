
ika = int(input("Anna ikäsi: "))

if ika > 14:
    print("Voit suorittaa mopokortin")
else:
    vuosia = 15 - ika
    print("Odota vielä", vuosia, "vuotta.")


## Operaattorit seuraavassa linkissä:
# https://www.w3schools.com/python/gloss_python_comparison_operators.asp


if ika >= 18:
    print("Olet aikuinen")


if True:
    print("Tämä on aina tosi.")
else:
    print("Tätä ei suoriteta koskaan..")


