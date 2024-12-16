
# Funktioiden tapaan parametrien oletusarvot toimivat luokissa:
class Luokka:
    def __init__(self, x=2, y=3):
        self.x = x
        self.y = y
    def __str__(self):
        return f"Luokka: x={self.x} y={self.y}"


olio1 = Luokka()
olio2 = Luokka(y=1)
olio3 = Luokka(3, 4)

print(olio1)
print(olio2)
print(olio3)


