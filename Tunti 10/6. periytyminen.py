

# Nyt päästään yhteen haastavimmista aiheista olio-ohjelmoinnissa, eli perintä.
# Luokka voi periä ominaisuuksia (muutujia/metodeja) toiselta luokalta.

# Aloitetaan esimerkillä:
class Henkilö:
    x = 1
    def tulosta_nimi(self, nimi):
        print("Nimesi on:", nimi)
# Tämä luokkka määrittää muuttujan "x" ja metodin "tulosta_nimi"


# Sitten luodaan perivä luokka "Oppilas":
class Oppilas(Henkilö):
    pass # Tänne ei tule mitään.


# Nyt voidaan luoda instanssi luokasta "Oppilas":
olio = Oppilas()
olio.tulosta_nimi("Joonas")
print("olio.x:", olio.x)
# Kuten huomataan, luokan "Oppilas" olio pääsee käsiksi luokan "Henkilö" muuttujiin ja metodeihin.
# Tätä on perintä olio-ohjelmoinnissa. Se on keskeinen aihe monissa kielissä kuten: Java, C++, C#, jne.


