
vuosi = int(input("Anna vuosi: "))

if vuosi == 2025:
    print("Vuosi on 2025")
elif vuosi == 2024:
    print("Vuosi on 2024")
elif vuosi == 2023:
    print("Vuosi on 2023")
else:
    print("Vuosi on jokin muu kuin 2023-2025")


if vuosi > 1900 and vuosi < 2050:
    print("Vuosi on väliltä: 1900-2050")


if 1900 < vuosi < 2050:
    print("Tämä vertailu tuottaa saman tuloksen kuin ylhäällä.")


## Hyvä myös opetella or-operaattorin käyttö:
# https://www.geeksforgeeks.org/python-or-operator'


