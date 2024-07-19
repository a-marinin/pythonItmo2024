""" Домашнее задание № 4 """

# Задача № 1
my_list = [1, 2, 3, 4, 5, 7.0, 8.0, 3.1415, True, False, "test", [1, 2], 99, 0, 'ноль', {'test': 'два'}]
print(list(filter(lambda x: type(x) is int, my_list)))  # Результат: [1, 2, 3, 4, 5, 99, 0]

# Задача № 2


def filter_out_some_words(my_str: str, my_list: list) -> list:
    for i in my_list:
        my_str = my_str.replace(i, '')
    return my_str


str = 'В мире насчитывают примерно 9 000 языков программирования. Среди них: C, Rust, php, Ruby, Python, Java, go, C#'
lst = ["Python", "php", "go", "C"]

print(filter_out_some_words(my_str=str, my_list=lst))
# В мире насчитывают примерно 9 000 языков программирования. Среди них: , Rust, , Ruby, , Java, , #


# Задача № 3
def task_3(*args):
    temp_list = []
    for item in args:
        if isinstance(item, type(str)):
            temp_list.append(item)

    return temp_list


test = task_3(1, 2, 3, 4, 5, 7.0, 8.0, 3.1415, True, False, "test", [1, 2], 99, 0, 'ноль', {'test': 'два'}, 'String')
print(test)  # Результат: ['test', 'ноль', 'String']


# Задача № 4
def lesenka(cubes_qty, max_layer_width):
    '''
    cubes_qty - это общее количество кубиков
    max_layer_width - это максимально допустимая ширина слоя кубиков (в текущем ряду)
    count - это количество комбинаций лесенки из кубиков
    i (в цикле for) - это количество кубиков в текущем слое
    '''
    if cubes_qty == 0:  # Если все кубики закончились
        return 1
    count = 0  # Сбрасываем значение переменной count до 0 (при каждой итерации)
    '''
    В цикле подставляем текущее количества кубиков в слое в диапозоне:
    Минимальное значение общего количества кубиков или максимальную допустимую ширину слоя (что быстрее закончится)
    Уменьшаем до 0 с шагом в -1
    '''
    for i in range(min(cubes_qty, max_layer_width), 0, -1):
        '''
        Увеличиваем количество комбинаций, повторно вызывая функцию lesenka.
        В качестве аргументов передаём ей:
        1. Количество оставшихся не использованных кубиков (общее количество кубиков минус количество кубиков в текущем слое)
        2. Максимально допустамую ширину слоя минус 1.
        '''
        count += lesenka(cubes_qty - i, i - 1)

    return count  # Возвращаем количество комбинаций


cubes_qty = 7  # Указываем количество кубиков
print(lesenka(cubes_qty, cubes_qty))  # Результат: 5
