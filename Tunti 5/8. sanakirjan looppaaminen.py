
# Sanakirjan looppaaminen ei ole aivan yhtä intuitiivinen kuin listojen, tuplejen tai  settien.

# Perus silmukka toimii näin:
sanakirja = {
    "a": 1,
    "b": 2,
    "c": 3
}
for x in sanakirja:
    print("x:", x)
print()

# Näytölle tulostuu avaimet. Miten arvot saadaan mukaan?
# Tarvitaan apufunktio:

for val in sanakirja.values():
    print("val:", val)
print()

# Nyt näemme arvot. Mutta onko molempia mahdollista tulostaa?
# Kyllä. Apufunktio "items()" auttaa tässä:

for key, val in sanakirja.items():
    print(key, val)

# Huomaa kuinka "items()" palauttaa tuplen.

