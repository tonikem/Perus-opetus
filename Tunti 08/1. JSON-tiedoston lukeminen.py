import json


with open("tiedosto.json") as tiedosto:
    data = tiedosto.read()


kurssit = json.loads(data)

for kurssi in kurssit:
    print("Kurssi:", kurssi)


print("\nkurssit[0]['nimi']:", kurssit[0]['nimi'])
print("kurssit[1]['periodit']:", kurssit[1]['periodit'])


