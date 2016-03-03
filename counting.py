# -*- encoding: utf-8 -*-

def add(x, y):
    vsota = x + y
    return vsota

def calculator(num1, num2, operation):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1-num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        return num1 / num2

def delez(populacija, vzorec):
    delez = float(vzorec) / float(populacija) * 100
    return round(delez,2)

def main():
    x = input("Vnesi število za populacijo: ")
    y = input("Vnesi število za vzorec: ")
    print "Delež je: ", str(delez(x, y)) + '%'

if __name__ == "__main__":
    main()

