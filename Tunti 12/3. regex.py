import re

# Säännölliset lauseet, eli "regular expression" on melko haastava aihe ohjelmoinnissa.
# Sen opetteluun kannattaa käyttää paljon aikaa.
# "Regular expressions", tai "Regex" lyhyesti, on tapa etsiä ja validoida merkkijonoja.

# Aloitetaan yksinkertaisella esimerkillä:
txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
print("x:", x)
# x on re-olio, joka kertoo minkälainen match tuli.


# Kokeillaan sitten "findall" funkiota:
txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)
# Nyt löytyy kaksi "ai" merkkijonoa


# Lisää tietoa linkistä: https://www.w3schools.com/python/python_regex.asp


