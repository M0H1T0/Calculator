def calculator():
    global example_for_calc
    while True:
        print("Вы можете начать работу с калькулятором(calc) Или посмотреть действия(help)")
        user_say = input("")

        if user_say == "calc":

            calc = input("Введите математическое действие:\n")
            print("Ответ: " + str(eval(calc)))

            example_for_calc = input('Хотите продолжить(c), выйти в меню(m), закрыть программу(e)?:\n')

            if example_for_calc == 'e' or example_for_calc == 'E' or example_for_calc == 'е' or example_for_calc == 'Е':
                print('Программа закроется через 5 секунд!!!')
                import time
                time.sleep(5)
                break

            if example_for_calc == 'c' or example_for_calc == 'C' or example_for_calc == 'с' or example_for_calc == 'С':
                print('Нажмите Enter чтобы продолжить!')
                calculator()

            if example_for_calc == 'm' or example_for_calc == 'M' or example_for_calc == 'м' or example_for_calc == 'М':
                main_menu()

            else:
                print('Ты что за ахинею написал. Программа отказывается это делать!!!')
                print('ПРОГРАММА СЛОМАНА, КРИТИЧЕСКИЙ СБОЙ. ЗАКРЫТИЕ НА ПОЧИНКУ ЧЕРЕЗ 5 СЕКУНД!!!')
                import time
                time.sleep(5)
                break

        if user_say == "help":

            print(
                "print('A + B — сумма"
                "A - B — разность"
                "A * B — произведение"
                "A / B — частное"
                "A ** B — возведение в степень"
                "A // B — целочисленное деление"
                "A % B — остаток от деления.')")

            user_action = input('Хотите продолжить(c), выйти в меню(m), закрыть программу(e)?:\n')

            if user_action == 'e' or user_action == 'E' or user_action == 'е' or user_action == 'Е':
                print('Программа закроется через 5 секунд!!!')
                import time
                time.sleep(5)
                break

            if example_for_calc == 'c' or example_for_calc == 'C' or example_for_calc == 'с' or example_for_calc == 'С':
                print('Нажмите Enter чтобы продолжить!')
                calculator()

            if example_for_calc == 'm' or example_for_calc == 'M' or example_for_calc == 'м' or example_for_calc == 'М':
                main_menu()

            else:
                print('Ты что за ахинею написал. Программа отказывается это делать!!!')
                print('ПРОГРАММА СЛОМАНА, КРИТИЧЕСКИЙ СБОЙ. ЗАКРЫТИЕ НА ПОЧИНКУ ЧЕРЕЗ 5 СЕКУНД!!!')
                import time
                time.sleep(5)
                break


def function_square():
    while True:
        import math
        r_of_round = float(input('Введите радиус круга:\n'))
        square = math.pi * r_of_round * r_of_round
        print('Площадь круга:', square)
        example = input('Хотите продолжить(c), выйти в меню(m), закрыть программу(e)?:\n')

        if example == 'e' or example == 'E' or example == 'е' or example == 'Е':
            print('Программа закроется через 5 секунд!!!')
            import time
            time.sleep(5)
            break

        if example == 'c' or example == 'C' or example == 'с' or example == 'С':
            print('Нажмите Enter чтобы продолжить!')
            function_square()

        if example == 'm' or example == 'M' or example == 'м' or example == 'м':
            main_menu()

        else:
            print('Ты что за ахинею написал. Программа отказывается это делать!!!')
            print('ПРОГРАММА СЛОМАНА, КРИТИЧЕСКИЙ СБОЙ. ЗАКРЫТИЕ НА ПОЧИНКУ ЧЕРЕЗ 5 СЕКУНД!!!')
            import time
            time.sleep(5)
            break


def volume():
    global user_action
    while True:
        volume_example = input('Обьём квадрата(С), или обьём параллелепипеда(P):\n')

        if volume_example == 'P' or volume_example == 'p':
            x = input('Введите высоту:\n')
            y = input('Введите ширину:\n')
            z = input('Введите глубину:\n')
            f = float(x) * float(y) * float(z)
            print('Результат ' + str(f))
            user_action = input('Хотите продолжить(c), выйти в меню(m), закрыть программу(e)?:\n')

            if user_action == 'e' or user_action == 'E' or user_action == 'е' or user_action == 'Е':
                print('Программа закроется через 5 секунд!!!')
                import time
                time.sleep(5)
                break

            if user_action == 'c' or user_action == 'C' or user_action == 'с' or user_action == 'С':
                print('Нажмите Enter чтобы продолжить!')
                volume()

            if user_action == 'm' or user_action == 'M' or user_action == 'м' or user_action == 'м':
                main_menu()

            else:
                print('Ты что за ахинею написал. Программа отказывается это делать!!!')
                print('ПРОГРАММА СЛОМАНА, КРИТИЧЕСКИЙ СБОЙ. ЗАКРЫТИЕ НА ПОЧИНКУ ЧЕРЕЗ 5 СЕКУНД!!!')
                import time
                time.sleep(5)
                break

        if volume_example == 'c' or volume_example == 'C':
            cube = input('Введите сторону куба: ')
            vcube = float(cube) ** 3
            print('Oбьём вашего куба равен: ' + str(vcube))
            user_action = input('Хотите продолжить(c), выйти в меню(m), закрыть программу(e)?:\n')

        if 'e' == user_action or user_action == 'E' or user_action == 'е' or user_action == 'Е':
            print('Программа закроется через 5 секунд!!!')
            import time
            time.sleep(5)
            break

        if user_action == 'c' or user_action == 'C' or user_action == 'с' or user_action == 'С':
            print('Нажмите Enter чтобы продолжить!')
            volume()

        if user_action == 'm' or user_action == 'M' or user_action == 'м' or user_action == 'М':
            main_menu()

        else:
            print('Ты что за ахинею написал. Программа отказывается это делать!!!')
            print('ПРОГРАММА СЛОМАНА, КРИТИЧЕСКИЙ СБОЙ. ЗАКРЫТИЕ НА ПОЧИНКУ ЧЕРЕЗ 5 СЕКУНД!!!')
            import time
            time.sleep(5)
            break


def main_menu():
    print("Функции которые вам доступны:\nКалькулятор(с)\nПлощадь(s)\nОбьём(v)")
    function = input("Введите букву функции которая вам нужна:\n")

    if function == "c" or function == "C":
        calculator()

    if function == "s" or function == "S":
        function_square()

    if function == "v" or function == "V":
        volume()


main_menu()
