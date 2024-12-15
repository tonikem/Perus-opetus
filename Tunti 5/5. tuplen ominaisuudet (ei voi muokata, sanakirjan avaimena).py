
# Luodaan sanakirja ja annetaan tuple sen avaimeksi:
sanakirja = dict()
tuple_lista = (1, 2, 3, 4)

sanakirja[tuple_lista] = 42
print("sanakirja:", sanakirja)
# Tuple näkyy avaimen paikalla.


# Tuple on muuttumaton, joten sen muokkaaminen edellyttää esim. listan luomista:
tuple_lista = list(tuple_lista)
tuple_lista[0] = "moi"
print("tuple_lista:", tuple_lista)

