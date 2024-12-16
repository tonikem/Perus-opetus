
# CSV on yleinen tekstitiedostojen tallennusmuoto.
# Sen lukeminen toimii seuraavasti:

with open("tiedosto.csv") as tiedosto:
    for rivi in tiedosto:
        print(rivi.strip())


