

## Listoista annetaan aina viittaus kopioidun arvon sijaan.
## Tämä näkyy siinä, kun käytetään listoja lohkojen sisällä:
def lisaa_alkio(lista: list):
    lista.append(10)

lista = [1, 2, 3]
print("lista = [1, 2, 3]: ", lista)

lisaa_alkio(lista)
print("lisaa_alkio(lista):", lista) # <- Näin tulosteesta näkyy, että uusi arvo on ilmestynyt listaan.


