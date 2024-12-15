## Operaattori	Merkitys	                Esimerkki	Tulos
#  +            Yhteenlasku	                2 + 4	    6
#  -	        Vähennyslasku           	10 - 2.5	7.5
#  *	        Kertolasku	                -2 * 123	-246
#  /	        Jakolasku (liukuluku)	    9 / 2	    4.5
#  //	        Jakolasku (kokonaisluku)	9 // 2	    4
#  %	        Jakojäännös             	9 % 2   	1
#  **	        Potenssi                	2 ** 3  	8


x = 4
y = 3

print("x + y =", x + y)

print("x - y =", x - y)

print("x * y =", x * y)

print("x / y =", x / y)

print("x // y =", x // y)

print("x % y =", x % y)

print("x ** y =", x ** y)


# Lasketaan painoindeksi
pituus = float(input("Anna pituus: "))
paino = float(input("Anna paino: "))

pituus = pituus / 100
bmi = paino / pituus ** 2

print(f"Painoindeksi on {bmi}")

