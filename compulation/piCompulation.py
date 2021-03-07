import math
from compulation.basic import summa
from compulation.basic import vicitanie
from compulation.basic import unmnozenie
from compulation.basic import delenie
from compulation.basic import stepen
from common.data import hel_pi_text


def pi_void():
    operator = input("\nЧто ты хочешь сделать? ")

    if operator == "+" or operator == "-" or operator == "*" or operator == "/" or operator == "s" or operator == "?":
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

        if operator == "?":
            hel_pi_text()
            pi_void()


    else:
        print("Команда <", operator, " для рабыты с числом пи не найдена")
        pi_void()


def get_data():
    a = float(input("Введи значение: "))
    return a
