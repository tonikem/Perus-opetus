

lista = [1, 2, 3, 4]
lista2 = lista  # <- Luodaan viittaus listaan "lista"

lista[0] = 10
lista2[1] = 42  # <- Muutetaan listaa "lista2", joka viittaa listaan "lista"

print("lista: ", lista)
print("lista2:", lista2, '\n')
# Nyt nähdään, että muutos tapahtuu myös listalla "lista"


