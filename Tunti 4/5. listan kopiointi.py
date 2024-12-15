

# Luodaan lista
lista = [1, 2, 3, 4]
kopio = lista[:]  # <- Luodaan kopio listasta.

lista[0] = 10
kopio[1] = 42 # Nyt muutetaan vain kopioitua listaa.

print("lista:", lista)
print("kopio:", kopio, '\n')
# Kopio on eri muistiosoitteessa, joten sen muuttaminen ei vaikuta alkuperäiseen listaan.


