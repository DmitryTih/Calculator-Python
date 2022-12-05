import math
print('------Welcome------')
alph0 = "а б в г д е ё ж з и й к л м н о п р с т у ф х ц ч ш щ ъ ы ь э ю я"
alph1 = "А Б В Г Д Е Ё Ж З И Й К Л М Н О П Р С Т У Ф Х Ц Ч Ш Щ Ъ Ы Ь Э Ю Я"
alph2 = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z"
alph3 = "a b c d e f j h i j k l m n o p q r s t u v w x y z"

alphEng = alph3.split() + alph2.split()
alphRuss = alph1.split() + alph0.split()
alphAll = alphRuss + alphEng

answer = 0

while True:
    options = input("Введите ваше действие. (P.s. 1-найти квадратичный корень числа, 2-вычеслить математический пример):   ")
    if options == "1":
        print("Вы выбрали поиск квадратичного корня.")
        sqrt_number = input("Желаете найти корень числа? Yes/No :   ")
        if sqrt_number == "Yes":
            sqrt_num = float(input("Ведите число корень которого вы ищите:   "))
            print(math.sqrt(sqrt_num))
        elif sqrt_number == "No":
            print("Тогда введите математическое выражение в следующие строки.")
            number0 = input("Введите 1-е число:  ")
            sign = input("Введите знак математической операции(+, -, *, /, **, %, //):  ")
            number1 = input("Введите 2-е число:  ")
            if (number0 in alphAll) or (number1 in alphAll):
                print("Нужно число.Вы ввели буквую.")
            else:         
                num0f = float(number0)
                num1f = float(number1)
                if sign in ("+", "-", "*", "**", "%", "//", "/",):
                    if sign == "+":
                        print(f"Выведенный ответ: {num0f + num1f}")
                    elif sign == "-":
                        print(f"Ваш ответ: {num0f - num1f}")
                    elif sign == "*":
                        print(f"Вы получили: {num0f * num1f}")
                    elif sign == "**":
                        print(f"Ответ при возведении в степень 1-го числа в 2-е: {num0f ** num1f}")
                    elif sign == "%":
                        if num1f == 0:
                            print("В школе не учился?На 0 делить нельзя.")
                        else:
                            print(f"Ваш вывод {num0f % num1f}")
                    elif sign == "//":
                        if num1f == 0:
                            print("В школе не учился?На 0 делить нельзя.")
                        else:
                            print(f"Ваше целое число при делении 1-го числа на 2-е: {int(num0f // num1f)}")
                    else:
                        if num1f == 0:
                            print("В школе не учился?На 0 делить нельзя.")
                        else:
                            print(f"Вывод по вашему примеру: {num0f / num1f}")
                else:
                    print("Данный знак недоступен, пожалуйста введите знак приведенный в скобках.")
        else:
            print("Неверная команда.")
    elif options == "2":
        print("Вы выбрали решение математического примера.")
        math_exp = input("Желаете продлжить? Yes/No :   ")
        if math_exp == "Yes":
                number0 = input("Введите 1-е число:  ")
                sign = input("Введите знак математической операции(+, -, *, /, **, %, //):  ")
                number1 = input("Введите 2-е число:  ")
                if (number0 in alphAll) or (number1 in alphAll):
                    print("Нужно число.Вы ввели буквую.")
                else:         
                    num0f = float(number0)
                    num1f = float(number1)
                    if sign in ("+", "-", "*", "**", "%", "//", "/",):
                        if sign == "+":
                            print(f"Выведенный ответ: {num0f + num1f}")
                        elif sign == "-":
                            print(f"Ваш ответ: {num0f - num1f}")
                        elif sign == "*":
                            print(f"Вы получили: {num0f * num1f}")
                        elif sign == "**":
                            print(f"Ответ при возведении в степень 1-го числа в 2-е: {num0f ** num1f}")
                        elif sign == "%":
                            if num1f == 0:
                                print("В школе не учился?На 0 делить нельзя.")
                            else:
                                print(f"Ваш вывод: {num0f % num1f}")
                        elif sign == "//":
                            if num1f == 0:
                                print("В школе не учился?На 0 делить нельзя.")
                            else:
                                print(f"Ваше целое число при делении 1-го числа на 2-е: {int(num0f // num1f)}")
                        else:
                            if num1f == 0:
                                print("В школе не учился?На 0 делить нельзя.")
                            else:
                                print(f"Вывод по вашему примеру: {num0f / num1f}")
                    else:
                        print("Данный знак недоступен, пожалуйста введите знак приведенный в скобках.")
        elif math_exp == "No":
            print("Тогда введите число (квадратичный корень которого вы хотите найти).")
            sqrt_num = float(input("Ведите число корень которого вы ищите:   "))
            print(math.sqrt(sqrt_num))
        else:
            print("Неверная команда.")
    else:
        print("Неверный номер опции.")
    exit = input('Вы находитесь в цикле.Для выхода из него введите "Stop"(Для продолжения "Continue"):  ')
    if exit == "Stop":
        break
    elif exit == "Continue":
        continue
    else:
        print("Неверная команда. (Автоматически цикл продолжит осуществлятся.)")