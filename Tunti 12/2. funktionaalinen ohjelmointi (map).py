# Luodaan sekava lista:
lista = [42, "merkkijono", True, 67.4]
print("lista", lista, '\n')

# Funktionaalisesta ohjelmoinnista olikin puhetta tunnin 11 osiossa 6.
# Siihen kuuluu myös olennaisesti for- ja while-silmukoiden välttäminen.
# Silmukan voi välttää käyttämällä iteroivia funktioita:

items = map(lambda x : x * 2, lista) # <- kertoo jokaisen alkion kahdella.

for item in items:
    print("item:", item)
print()

# Lukuja voi myös suodattaa "filter" funktiolla:
luvut = [1, 2, 3, 5, 6, 4, 9, 10, 14, 15]

parilliset = filter(lambda luku: luku % 2 == 0, luvut)

for luku in parilliset:
    print("luku:", luku)
# Nyt vain parilliset tulostetaan.


