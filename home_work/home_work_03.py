import random


# Задача № 1.1 (решение с использованием цикла)
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


my_list = [random.randint(-999, 999) for x in range(5)]  # Генерируем список из пяти случайных целых чисел
find_positive_numbers_v1(my_list)
find_positive_numbers_v2(my_list)
print()


# Задача № 2
def find_same_values_in_lists() -> None:
    l1 = [1, 2, 3, 'test', True, False, 5.5]
    l2 = [4, 5, 6, 'temp', 0, 0.1, -5, 5.5]
    print([element for element in l1 if element in l2])  # [False, 5.5]


find_same_values_in_lists()
print()


# Задача № 3
def task_3(my_list: list, my_num: int) -> list:
    print(f'Был сгенерирован следующий список случайных чисел: {my_list}')  # [9, 1, 4, 4, 9, 3, 8, 7, 8, 6]
    lst = [num for num in my_list if num % my_num == 0]
    print(f'Следующие числа кратны числу {my_num}: {lst}')  # Следующие числа кратны числу 2: [4, 4, 8, 8, 6]
    return lst


task_3(my_list=[random.randint(1, 10) for x in range(10)], my_num=2)
print()


# Задача № 4
def find_the_factorial_of_a_number(my_num: int) -> None:
    n = my_num
    factorial = 1
    while n > 1:
        factorial *= n
        n -= 1
    print(f'Факториал числа {my_num} равен {factorial}')


find_the_factorial_of_a_number(my_num=6)  # Факториал числа 6 равен 720
print()

# Задача № 5
lst = [2, 4, 5, 8, 9, 13]

for number in range(len(lst)):
    lst[number] *= number
print(lst)  # Результат [0, 4, 10, 24, 36, 65]

lst2 = [2, 4, 5, 8, 9, 13]
n = 0
while n < len(lst2):
    lst2[n] *= n
    n += 1
print(lst2)  # Результат [0, 4, 10, 24, 36, 65]
