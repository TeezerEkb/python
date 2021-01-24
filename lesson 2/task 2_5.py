# Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор
# натуральных чисел. У пользователя необходимо запрашивать новый элемент
# рейтинга. Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.
# Набор натуральных чисел можно задать непосредственно в коде

my_list = [7, 5, 3, 3, 2]
print(f"Текущий рейтинг - {my_list}")
digit = int(input("Введите число (1234 - выход из программы) "))
while digit != 1234:
    for el in range(len(my_list)):
        if my_list[el] == digit:
            my_list.insert(el + 1, digit)
            break
        elif my_list[0] < digit:
            my_list.insert(0, digit)
        elif my_list[-1] > digit:
            my_list.append(digit)
        elif my_list[el] > digit and my_list[el + 1] < digit:
            my_list.insert(el + 1, digit)
    print(f"новый рейтинг - {my_list}")
    digit = int(input("Введите число "))
