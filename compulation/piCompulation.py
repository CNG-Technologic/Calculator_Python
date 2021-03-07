import math
from compulation.basic import summa
from compulation.basic import vicitanie
from compulation.basic import unmnozenie
from compulation.basic import delenie
from compulation.basic import stepen


def pi_void():
    operator = input("Что ты хочешь сделать? ")

    if operator == "+":
        a = get_data()
        print(math.pi, " + ", a,  " = ", summa(math.pi, a))

    if operator == "-":
        a = get_data()
        print(math.pi, " - ", a, " = ", vicitanie(math.pi, a))

    if operator == "*":
        a = get_data()
        print(math.pi, " * ", a, " = ", unmnozenie(math.pi, a))

    if operator == "/":
        a = get_data()
        print(math.pi, " / ", a, " = ", delenie(math.pi, a))

    if operator == "s":
        a = get_data()
        print(math.pi, " в степени ", a, " = ", stepen(math.pi, a))


def get_data():
    a = float(input("Введи значение: "))
    return a
