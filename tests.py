from counting import add
from counting import calculator
from counting import delez
from eblagajna import cena

def testing_add():
    assert add(2, 3) == 5
    return "add() passed successfully"

def testing_function_calculator():
    assert calculator(3, 4, "*") == 12
    return "testing_function_calculator() passed successfully"

def testing_delez():
    assert delez(120, 30) == 25
    return "testing_delez() passed successfully"

def testing_e_blagajna():
    izdelki = {"kruh": 1.99, "mleko": 0.89, "sir": 2.99}
    assert cena(izdelki, "kruh") == 1.99
    return "testing_e_blagajna() passed successfully"

print testing_e_blagajna()
