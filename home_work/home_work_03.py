import random

# Задача № 1.1 (решение с использованием цикла)
my_list = [random.randint(-999, 999) for x in range(5)]  # Генерируем список из пяти случайных целых чисел


def find_positive_numbers_v1(my_list: list) -> None:
    print(f'Был сгенерирован следующий список случайных чисел: {my_list}')
    list_positive_num = []  # Пустой список, чтобы добавлять в него положительные цифры
    for i in range(len(my_list)):
        if my_list[i] > 0:
            list_positive_num.append(my_list[i])  # Добавляем положительное число в список
    print(f'В списке {my_list} колличество положительных чисел = {len(list_positive_num)} ({list_positive_num}) ')


# Задача № 1.2 (решение с использованием List comprehensions)
def find_positive_numbers_v2(my_list: list) -> None:
    print(f'Был сгенерирован следующий список случайных чисел: {my_list}')
    list_positive_num = [x for x in my_list if x > 0]
    print(f'В списке {my_list} колличество положительных чисел = {len(list_positive_num)} ({list_positive_num}) ')


find_positive_numbers_v1(my_list)
find_positive_numbers_v2(my_list)
