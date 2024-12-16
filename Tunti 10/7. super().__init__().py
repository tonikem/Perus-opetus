
# self-avainsanalla luotuja muuttujia voidaan periyttää luokalta toiselle:
class Kirja:
    def __init__(self, nimi, kirjailija):
        self.nimi = nimi
        self.kirjailija = kirjailija


class Gradu(Kirja):
    def __init__(self, nimi, kirjailija, arvosana):
        super().__init__(nimi, kirjailija)
        self.arvosana = arvosana


gradu = Gradu("Olio-ohjelmointi", "Pekka", 4)
print("gradu.nimi:", gradu.nimi)
print("gradu.arvosana:", gradu.arvosana)
print("gradu.kirjailija:", gradu.kirjailija)


