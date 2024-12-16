
# On mahdollista määrittää funktio luokan sisällä,
# mutta myös toisen funktion sisällä:

def f():
    def sisäinen_funktio():
        print("Terveisiä funktion \"f()\" sisältä.")

    sisäinen_funktio()


f()



