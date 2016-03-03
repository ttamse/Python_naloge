# -*- encoding: utf-8 -*-

def glavno_mesto(seznam, drzava):
    return seznam[drzava]

def preveri_odgovor(drzava, mesto):
    if mesto == glavno_mesto(dict, drzava):
        print "Odgovor je pravilen"
        return True
    else:
        print "Odgovor ni pravilen"
        return False

dict = {"Slovenija": "Ljubljana", "Hrvaska": "Zagreb", "Avstrija": "Dunaj", "Italija": "Rim"}
score = 0
print "To je igra ugibanja glavnih mest ... za otroke ... tako da je v slovenščini (brez šumnikov sicer)."
for drzava in dict:
    print "Ugani glavno mesto države", drzava
    odgovor = raw_input()
    if preveri_odgovor(drzava, odgovor) == True:
        score += 1
print "To je vse. Tvoj rezultat: ", score

