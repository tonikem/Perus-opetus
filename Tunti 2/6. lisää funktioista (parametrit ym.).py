
## 1.
def summa(x, y):
    print("Parametrien summa on", x + y)

summa(1, 2)
summa(y=2, x=1)


## 2.
def paluuarvo():
    return "Tämä merkkijono palautuu funktiosta."

muuttuja = paluuarvo()
print(muuttuja)


## 3.
def summa(a, b):
    return a+b

def erotus(a, b):
    return a-b

tulos = erotus(summa(5, 2), summa(2, 3))
print("Vastaus on", tulos)


