

nimi = "Erkki"
ika = 39


## Tämä toimii kyllä....
print("Hei " + nimi + " ikäsi on " + str(ika) + " vuotta" )


## Mutta on olemassa parempi tapa muotoilla merkkijonot:
print(f"Hei {nimi} ikäsi on {ika} vuotta")


## Toinen niksi on muuttaa separaattoria print-funktiossa:
print("Hei", nimi, "ikäsi" + "on", ika, "vuotta", sep="")


## Myös lukuja pystyy muotoilemaan:
luku = 1/3
print(f"Luku on {luku:.2f}") # <- Tulostaa vain 2 ensimmäistä desimaalia


