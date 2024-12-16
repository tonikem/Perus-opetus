
# Funktioihin on joskus hyvä lisätä oletusparametrejä:
def tulosta_kirjain(kirjain='a'):
    print(f"Kirjain: {kirjain}")


tulosta_kirjain('b')
tulosta_kirjain('c')
tulosta_kirjain() # <- tulostaa kirjaimen 'a', koska ei ole annettu parametria.


