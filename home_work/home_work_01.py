""" Домашнее задание № 1 """

# Задача № 1
var_int = 1
var_float = 1.0
var_str = "This is a string variable"
var_list = [1, 1.0, "test", [1, 2, 3], True]
var_bool = False
print(var_int, '\n', var_float, '\n', var_str, '\n', var_list, '\n', var_bool)
print()

# Задача № 2
print(isinstance(var_int, int))
print(isinstance(var_float, float))
print(isinstance(var_str, str))
print(isinstance(var_list, list))
print(isinstance(var_bool, bool))
print()

# Задача № 3
x = 10
print(x)
x += 5
print(x)
print(x == 15)

# Задача № 4
str1 = "Это переменная для 4-й задачи, 1-го домашнего задания"
str2 = "ITMO 2024 - Курс Python для начинающих"
print("Длина 1-й переменной: ", len(str1))
print("Длина 2-й переменной: ", len(str2))
print(str1 + " " + str2)