
# Sanakirja sisältää avaimia ja arvoja:
sanakirja = {}
sanakirja['Juho'] = 35
sanakirja['Jesse'] = 42
sanakirja['Veeti'] = 13
print("sanakirja:", sanakirja)


# Sanakirjan avaimiksi kelpaa mikä tahansa muuttumaton arvo:
listat = {}
listat[5.6] = [1, 2, 3]
listat[True] = [7, 8, 6]
listat[0x601] = [5, 2, 3]
print("listat:", listat)


# Myös "dict()" funktio kelpaa sanakirjaa luodessa:
uusi_sanakirja = dict()
uusi_sanakirja['moikka'] = "kaikille"
print("uusi_sanakirja:", uusi_sanakirja)


