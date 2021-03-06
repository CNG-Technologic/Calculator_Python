from math import sqrt


def descriminant(a, b, c):
    D = b * b - 4 * a * c
    print("D = ", b, " * ", b, " - 4 * ", a, " * ", c, " = ", D)

    if D > 0:
        x1 = (-b - sqrt(D)) / (2 * a)
        x2 = (-b + sqrt(D)) / (2 * a)
        print(x1, x2)
    elif D == 0:
        x = -b / 2 * a
        print(x)
    else:
        print("Уравнение не имеет действительных корней!")


def factorial(a):
    result = 1
    if int(a) >= 1:
        for i in range(1, int(a) + 1):
            result = result * i
    return result
