
# Luodaan lista ja lisätään alkioita
lista = ["Eka alkio"]
lista.append("Toinen alkio")
lista.append("Kolmas alkio")
print("lista:", lista)

# Asetetaan uusi alkio paikalle [1]
lista.insert(1, "Uusi alkio")
print("lista:", lista)

# Popistetaan viimeinen, eli kolmas alkio
lista.pop()
print("lista:", lista)

# Poistetaan uusi alkio
lista.remove("Uusi alkio")
print("lista:", lista)

# Luodaan uusi lista ja järjestetään se
lista = ['b', 'c', 'a']
lista.sort()
print("lista:", lista)

