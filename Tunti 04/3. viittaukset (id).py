

lista = [1, 2, 3]
print("id(lista):", id(lista))
merkkijono = "Tämäkin on viittaus"
print("id(merkkijono):", id(merkkijono), '\n')

# Mitä terminaaliin tulostuu? Satunnaisia numeroita?
# Kyseessä on muuttujan osoite tietokoneen muistissa.
# Alla tulostetaan funktion "print" osoite muistissa:
print("id(print):", id(print), '\n')


# Yleensä samoilla arvoilla on sama osoite muistissa.
# Seuraavassa esimerkissä tarkastellaan tätä.
x = 1
y = 1
print("id(x):", id(x))
print("id(y):", id(y), '\n')

# Näin tulostuu sama numeroarvo,
# koska muuttujat osoittavat samaan osoitteeseen muistissa.


# Muistiosoitteita esitetään perinteisesti hexadesimaaleina:
print("hex(id(x)):", hex(id(x)), '\n')


###  Lisää tietoa hexadesimaaleista löytyy Googlesta hakusanalla: "hexadecimal"  ###


# Lopuksi katsotaan miten käy kun lukua inkrementoidaan kymmenellä.
luku = 1
print("luku = 1:\t", id(luku))
luku += 10
print("luku += 10:\t", id(luku), '\n')

# Mitä ihmettä? Muistiosoitteet saavat nyt eri arvot..
# Python toimii näin ja jokainen luvun muutos luo oikeasti uuden luvun muistiin.
# Esim. luku 1 on yhä samassa osoitteessa:
print("id(1):\t\t", id(1))


# Lisää muistiosoitteista täältä: https://en.wikipedia.org/wiki/Pointer_%28computer_programming%29

