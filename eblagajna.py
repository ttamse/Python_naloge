

def cena(podatki, izdelek):
    return podatki[izdelek]

def main():
    cenik_izdelkov = {"moka": 0.80, "jajca": 2.00, "jabolka": 0.69}
    izdelek = raw_input("Za informacijo o ceni vnesi izdelek: ")
    print "Cena je (EUR): ", cena(cenik_izdelkov, izdelek)

if __name__ == "__main__":
    main()

