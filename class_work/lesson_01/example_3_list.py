my_list = [1, 2, 3, 4, 5]

my_list_2 = [[1, 2, 3], 'text', 5.5]

print('Длина списка my_list: ', len(my_list))  # Длина списка my_list:  5
print('Обращение к элементу', my_list_2[2])  # Обращение к элементу 5.5

# Изменение элемента
print(my_list)  # [1, 2, 3, 4, 5]
my_list[0] = 6
print(my_list)  # [6, 2, 3, 4, 5]

# Добавление элемента
my_list.append(7)
print(my_list)  # [6, 2, 3, 4, 5, 7]

# Удаление по элементу
my_list.remove(7)
print(my_list)  # [6, 2, 3, 4, 5]

# Удаление по индексу
my_list.pop(0)
print(my_list)  # [2, 3, 4, 5]
