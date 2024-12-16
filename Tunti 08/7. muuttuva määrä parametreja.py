import statistics as s


def listan_kerääminen(*lista):
    print("sum(lista):", sum(lista))
    print("s.mean(lista):", s.mean(lista))
    print("s.median(lista):", s.median(lista))


listan_kerääminen(1, 2, 3, 42, 100)


