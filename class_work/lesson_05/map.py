# Пример №1
def square(number):
    return number ** 2


numbers = [1, 2, 3, 4, 5]
print(list(map(square, numbers)))  # Результат: [1, 4, 9, 16, 25]


# Пример №2
str_nums = ["4", "8", "6", "5", "3", "2", "8", "9", "2", "5"]
# Функция int - приводим элемент последовательности к формату int
print(list(map(int, str_nums)))  # Результат: [4, 8, 6, 5, 3, 2, 8, 9, 2, 5]

# Пример №3
words = ['abs', 'len', 'filter', 'map', 'join']
# Функция len - получаем длинну строк исходного списка
print(list(map(len, words)))  # Результат: [3, 3, 6, 3, 4]

# Задача №1
string_upper = 'Mapping'
print(list(map(lambda x: x.upper(), string_upper)))