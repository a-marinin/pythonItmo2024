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
