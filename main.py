import math
import time


def user_action():
    user_act = input('Хотите продолжить(c), выйти в меню(m), закрыть программу(e)?: ')

    if user_act == 'e' or 'E':
        quit()

    elif user_act == 'm' or 'M':
        main_menu()

    elif user_act == 'c' or 'C':
        calculator()

    else:
        print('Ошибка, программа закроется через 5 секунд!!!')
        time.sleep(5)
        quit()


def main_menu():
    print("Здравствуйте, можете писать в обоих регистрах, но на английской раскладке!!!\n"
          "Функции которые вам доступны: Калькулятор(с) Площадь(s) Обьём(v)")
    function = input("Введите букву функции которая вам нужна: ")

    if function == 'c' or 'C':
        calculator()

    elif function == 's' or 'S':
        square()

    elif function == 'v' or 'V':
        volume()


def calculator():
    while True:
        print("Вы можете начать работу с калькулятором(calc) Или посмотреть действия(help)")
        user_say = input("")

        if user_say == "calc":
            calc = input("Введите пример: ")
            print("Ответ: " + str(eval(calc)))
            user_action()

        if user_say == "help":
            print(
                "Знак вписывайте между числами для операции\n "
                "A + B — сумма\n "
                "A - B — разность\n "
                "A * B — произведение\n "
                "A / B — частное\n "
                "A ** B — возведение в степень\n "
                "A // B — целочисленное деление\n "
                "A % B — остаток от деления.")
            calculator()


def square():
    while True:
        r_of_round = float(input('Введите радиус круга: '))
        print('Площадь круга:', math.pi * r_of_round * r_of_round)
        user_action()


def volume():
    while True:
        volume_example = input('Обьём квадрата(С), или обьём параллелепипеда(P): ')

        if volume_example == 'P' or volume_example == 'p':
            x = input('Введите высоту:\n')
            y = input('Введите ширину:\n')
            z = input('Введите глубину:\n')
            f = float(x) * float(y) * float(z)
            print('Результат ' + str(f))
            user_action()

        if volume_example == 'c' or volume_example == 'C':
            cube = input('Введите сторону куба: ')
            vcube = float(cube) ** 3
            print('Oбьём вашего куба равен: ' + str(vcube))
            user_action()


main_menu()
