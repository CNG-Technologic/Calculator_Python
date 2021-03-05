from start.MainStart import start_main


def start_void():
    print("1 - старт \n2 - выход")
    start_operator = input()

    if start_operator == "1":
        start_main()
    else:
        print("Завершение работы")


def if_start():
    print("1 - да \n2 -нет \nТак же работает Y/N (yes/no)")
    start_oper = input()

    if start_oper == "нет" | start_oper == "2" | start_oper == "n" | start_oper == "NO":
        start_main()
    else:
        print("завершение работы...")