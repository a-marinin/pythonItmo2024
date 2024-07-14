# Это наше предыдущее решение задачи № 2 (достаточно громоздкое)
task_list = []
for i in range(10):
    task_list.append(i ** 2)
print(task_list)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Это решение задачи № 2 (через list comprehensions)
my_list = [x ** 2 for x in range(10)]
print(my_list)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]


# Example 2
fruit_list = ['apple', 'banana', 'cherry', 'kiwi', 'mango']
# Создать список из слов, где присутствует буква 'а'
print([x for x in fruit_list if 'a' in x])  # ['apple', 'banana', 'mango']

# Task 3
# Требуется получить абревиатуры слов из следующего списка:
str_list = ['continuous', 2, 'integration', 34, 'continuous', [123, 1234], 'delivery']

print(''.join([x[0].upper() for x in str_list if isinstance(x, str)]))  # CICD
