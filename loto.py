# -*- encoding: utf-8 -*-

from random import randint

def loto_stevilke(stevilo):
    iter = 0
    stevila = []
    while iter < stevilo:
        st = randint(1, 39)
        if st in stevila:
            """Do nothing"""
        else:
            stevila.append(st)
            iter += 1
    stevila.sort()
    return stevila

koliko = input("Koliko številk rabiš? ")
print loto_stevilke(koliko)
