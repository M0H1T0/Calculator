def Calc():
    while True:
        print("Вы можете начать работу с калькулятором(calc) Или посмотреть действия(help)")
        user_say = input("")

        if user_say == "calc":

            calc = input("Введите математическое действие:\n")
            print("Ответ: " + str(eval(calc)))

            ex = input('Хотите продолжить(c), выйти в меню(m), закрыть программу(e)?:\n')

            if ex == 'e' or ex == 'E' or ex == 'е' or ex == 'Е':
                print('Программа закроется через 5 секунд!!!')
                import time
                time.sleep(5)
                break

            if ex == 'c' or ex == 'C' or ex == 'с' or ex == 'С':
                print('Нажмите Enter чтобы продолжить!')
                Calc()

            if ex == 'm' or ex == 'M' or ex == 'м' or ex == 'М':
                MainMenu()

            else:
                print('Ты что за ахинею написал. Программа отказывается это делать!!!')
                print('ПРОГРАММА СЛОМАНА, КРИТИЧЕСКИЙ СБОЙ. ЗАКРЫТИЕ НА ПОЧИНКУ ЧЕРЕЗ 5 СЕКУНД!!!')
                import time
                time.sleep(5)
                break

        if user_say == "help":

            print("print('A + B — сумма\nA - B — разность\nA * B — произведение\nA / B — частное\nA ** B — возведение в степень\nA // B — целочисленное деление\nA % B — остаток от деления.')")

            ex = input('Хотите продолжить(c), выйти в меню(m), закрыть программу(e)?:\n')

            if ex == 'e' or ex == 'E' or ex == 'е' or ex == 'Е':
                print('Программа закроется через 5 секунд!!!')
                import time
                time.sleep(5)
                break

            if ex == 'c' or ex == 'C' or ex == 'с' or ex == 'С':
                print('Нажмите Enter чтобы продолжить!')
                Calc()

            if ex == 'm' or ex == 'M' or ex == 'м' or ex == 'М':
                MainMenu()

            else:
                print('Ты что за ахинею написал. Программа отказывается это делать!!!')
                print('ПРОГРАММА СЛОМАНА, КРИТИЧЕСКИЙ СБОЙ. ЗАКРЫТИЕ НА ПОЧИНКУ ЧЕРЕЗ 5 СЕКУНД!!!')
                import time
                time.sleep(5)
                break



def Square():
    while True:
        import math
        R = float(input('Введите радиус круга:\n'))
        S = math.pi * R * R
        print('Площадь круга:', S)
        ex = input('Хотите продолжить(c), выйти в меню(m), закрыть программу(e)?:\n')

        if ex == 'e' or ex == 'E' or ex == 'е' or ex == 'Е':
            print('Программа закроется через 5 секунд!!!')
            import time
            time.sleep(5)
            break

        if ex == 'c' or ex == 'C' or ex == 'с' or ex == 'С':
            print('Нажмите Enter чтобы продолжить!')
            Square()

        if ex == 'm' or ex == 'M' or ex == 'м' or ex == 'м':
            MainMenu()

        else:
            print('Ты что за ахинею написал. Программа отказывается это делать!!!')
            print('ПРОГРАММА СЛОМАНА, КРИТИЧЕСКИЙ СБОЙ. ЗАКРЫТИЕ НА ПОЧИНКУ ЧЕРЕЗ 5 СЕКУНД!!!')
            import time
            time.sleep(5)
            break

def Volume():
    while True:
        Vex = input('Обьём квадрата(С), или обьём параллелепипеда(P):\n')

        if Vex == 'P' or Vex == 'p':
            x = input('Введите высоту:\n')
            y = input('Введите ширину:\n')
            z = input('Введите глубину:\n')
            f = float(x) * float(y) * float(z)
            print('Результат ' + str(f))
            ex = input('Хотите продолжить(c), выйти в меню(m), закрыть программу(e)?:\n')

            if ex == 'e' or ex == 'E' or ex == 'е' or ex == 'Е':
                print('Программа закроется через 5 секунд!!!')
                import time
                time.sleep(5)
                break

            if ex == 'c' or ex == 'C' or ex == 'с' or ex == 'С':
                print('Нажмите Enter чтобы продолжить!')
                Volume()

            if ex == 'm' or ex == 'M' or ex == 'м' or ex == 'м':
                MainMenu()

            else:
                print('Ты что за ахинею написал. Программа отказывается это делать!!!')
                print('ПРОГРАММА СЛОМАНА, КРИТИЧЕСКИЙ СБОЙ. ЗАКРЫТИЕ НА ПОЧИНКУ ЧЕРЕЗ 5 СЕКУНД!!!')
                import time
                time.sleep(5)
                break

        if Vex == 'c' or Vex == 'C':
            cube = input('Введите сторону куба: ')
            vcube = float(cube) ** 3
            print ('Oбьём вашего куба равен: ' +str(vcube))
            ex = input('Хотите продолжить(c), выйти в меню(m), закрыть программу(e)?:\n')

        if ex == 'e' or ex == 'E' or ex == 'е' or ex == 'Е':
            print('Программа закроется через 5 секунд!!!')
            import time
            time.sleep(5)
            break

        if ex == 'c' or ex == 'C' or ex == 'с' or ex == 'С':
            print('Нажмите Enter чтобы продолжить!')
            Volume()

        if ex == 'm' or ex == 'M' or ex == 'м' or ex == 'М':
            MainMenu()

        else:
            print('Ты что за ахинею написал. Программа отказывается это делать!!!')
            print('ПРОГРАММА СЛОМАНА, КРИТИЧЕСКИЙ СБОЙ. ЗАКРЫТИЕ НА ПОЧИНКУ ЧЕРЕЗ 5 СЕКУНД!!!')
            import time
            time.sleep(5)
            break

def MainMenu():
    print("Функции которые вам доступны:\nКалькулятор(с)\nПлощадь(s)\nОбьём(v)")
    function = input("Введите букву функции которая вам нужна:\n")

    if function == "c" or function == "C":
        Calc()

    if function == "s" or function == "S":
        Square()

    if function == "v" or function == "V":
        Volume()

MainMenu()