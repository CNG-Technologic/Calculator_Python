from compulation.basic import summa
from compulation.basic import vicitanie
from compulation.basic import unmnozenie
from compulation.basic import delenie
from compulation.basic import koren
from data import help_text


def start_main():
    print("Что ты хочешь сделать?")
    operator = input()

    if operator == "+" or operator == "-" or operator == "*" or \
            operator == "/" or operator == "k" or operator == "?" \
            or operator == "help" or operator == "e" or operator == "е":

        if operator == "?" or operator == "help":
            help_text()

        if operator == "+" or operator == "-" or operator == "*" or operator == "/":
            a = float(input("Введи 1 число: "))
            b = float(input("Введи 2 число: "))

            if operator == "+":
                result = summa(a, b)
                print(a, " + ", b, " = ", result)

            if operator == "-":
                result = vicitanie(a, b)
                print(a, " - ", b, " = ", result)

            if operator == "*":
                result = unmnozenie(a, b)
                print(a, " * ", b, " = ", result)

            if operator == "/":
                result = delenie(a, b)
                print(a, " / ", b, " = ", result)

        if operator == "k":
            a = float(input("Введи число:"))
            result = koren(a)
            print(result)

        if operator == "е" or operator == "e":
            print("Ты действительно хочешь выйти?")
            # засунуть вызов метода для выхода

        start_main()

    else:
        print("Команда < ", operator, " > не найдена")
        start_main()
