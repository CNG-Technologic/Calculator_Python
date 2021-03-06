from compulation.basic import summa
from compulation.basic import vicitanie
from compulation.basic import unmnozenie
from compulation.basic import delenie
from compulation.basic import koren
from common.data import help_text
from compulation.more import descriminant
from compulation.more import factorial
from compulation.basic import stepen


def start_main():
    print("Что ты хочешь сделать?")
    operator = input()

    if operator == "+" or operator == "-" or operator == "*" or \
            operator == "/" or operator == "k" or operator == "d" \
            or operator == "f" or operator == "!" or operator == "s" \
            or operator == "?" or operator == "help":

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

        if operator == "s":
            a = float(input("Введи число: "))
            b = float(input("Введи степень: "))
            result = stepen(a, b)
            print(result)

        if operator == "d":
            a = float(input("Введи чсло а: "))
            b = float(input("Введи число b: "))
            c = float(input("Введи число c: "))
            descriminant(a, b, c)

        if operator == "f" or operator == "!":
            a = float(input("Введи число a:"))
            rest = factorial(a)
            print(rest)

        start_main()

    elif operator == "e" or operator == "е":

        if operator == "е" or operator == "e":
            print("Ты действительно хочешь выйти?")
            full_exit()

    else:
        print("Команда < ", operator, " > не найдена")
        start_main()


def full_exit():
    print("1 - да \n2 - нет")
    start_oper = input()

    if start_oper == "2":
        start_main()
    elif start_oper == "1":
        print("Завершение работы...")
    else:
        print("Команда < ", start_oper, " > не найдена")
        full_exit()
