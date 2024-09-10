import math
num_input = -1
while num_input != 0:
    greatings = """Выберите желаемую функцию:
    1. Сложение 
    2. Вычитание
    3. Умножение
    4. Деление
    5. Возведение в степень
    6. Округление числа в большую сторону до целого
    7. Округление числа в меньшую сторону до целого
    
    Введите "0" чтобы завершить выполнение программы"""

    print(greatings)
        
    num_input = int(input())

    if num_input == 1:
        print("Введите первый элемент:")
        sum1_input = int(input())
        print("Введите второй элемент:")
        sum2_input = int(input())

        summa = sum1_input + sum2_input
        print("Ответ: ", summa)


    if num_input == 2:
        print("Введите первый элемент:")
        sub1_input = int(input())
        print("Введите второй элемент:")
        sub2_input = int(input())

        subtract = sub1_input - sub2_input
        print("Ответ: ", subtract)

    if num_input == 3:
        print("Введите первый элемент:")
        prod1_input = int(input())
        print("Введите второй элемент:")
        prod2_input = int(input())

        product = prod1_input * prod2_input
        print("Ответ: ", product)

    if num_input == 4:
        try:
            print("Введите первый элемент:")
            div1_input = float(input())
            print("Введите второй элемент:")
            div2_input = float(input())

            division = div1_input / div2_input
            print("Ответ: ", division)
        except ZeroDivisionError:
            print("На 0 делить нельзя!")
            
    if num_input == 5:
        print("Введите первый элемент:")
        exp1_input = int(input())
        print("Введите второй элемент:")
        exp2_input = int(input())

        exponation = exp1_input ** exp2_input
        print("Ответ: ", exponation)

    if num_input == 6:
        print("Введите элемент:")
        round1_input = float(input())

        rounding_big = math.ceil(round1_input)
        print("Ответ: ", rounding_big)

    if num_input == 7:
        print("Введите элемент:")
        round2_input = float(input())
        
        rounding_small = int(round2_input)
        print("Ответ: ", rounding_small)

    
