

# Alkioita voi suodattaa listakoosteen if-osoiossa:
lista = [670, 435, 2134, 234, 853, 1243254, 21, 51232, 2137, 1012, 1212, 322]
parilliset = [alkio for alkio in lista if alkio % 2 == 0]
parittomat = [alkio for alkio in lista if alkio % 2 != 0]

print("parilliset:", parilliset)
print("parittomat:", parittomat)
# Muodostettiin kaksi koostetta, ensimmäisessä parilliset ja toisessa parittomat alkiot.


# Tässä esimerkissä suodatetaan kaikki vokaalit merkkijonosta:
merkkijono = "Hei kaikille!"
vokaalit = [merkki for merkki in merkkijono if merkki in "aeiouyåäö"]
print(f'Sanan "{merkkijono}" vokaalit:', "".join(vokaalit))

