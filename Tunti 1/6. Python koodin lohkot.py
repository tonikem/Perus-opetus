
vuosi = 1942

if vuosi < 2000:
print("Tämä ei ole oikeassa lohkossa!")
# Tuottaa virheen "IndentationError: expected an indented block after 'if' statement on line 4"
else:
    print("Tämä on oikeassa lohkossa.")


# if-lauseke vaatii, että suoritettava koodi on sisennetty omassa lohkossaan.


if vuosi == 1942:
  print("Tämä on sisennetty 2 välilyönnillä.")


if vuosi > 1917:
  print("Tämä toimii..")
    print("Mutta tämä ei toimi.") # <- "IndentationError: unexpected indent"



