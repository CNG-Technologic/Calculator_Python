from start.MainStart import start_main

print("Калькулятор Python Alpha 1.2")


def start_void():
    print("1 - старт \n2 - выход")
    start_operator = input()

    if start_operator == "1":
        start_main()
    elif start_operator == "2":
        print("Завершение работы")
    else:
        print("Комманда < ", start_operator, " > не найдена")
        start_void()


start_void()
