

# Sanakirja voidaan luoda myös alla olevalla tavalla:
sanakirja = {
    "x": 12,
    "y": 13,
    "z": 14
}

# Avainten poistaminen tapahtuu seuraavasti:
del sanakirja["x"]
print("sanakirja:", sanakirja)
# Sanakirjasta puuttuu niin avain kuin arvokin.


# Pelkästään arvon poistaminen onnistuu näin:
sanakirja["y"] = None
print("sanakirja:", sanakirja)
# Nyt avain löytyy, mutta sen arvo on kadonnut.

