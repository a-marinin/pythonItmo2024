
func = lambda x: x*2


def func_2(x):
    return x * 2


print(func(5))  # Результат: 10

# ---
list_values = (1, 3, 4, 2, 6, 7, 5, 8, 9)
print(list(filter(lambda x: x % 2 == 0, list_values)))  # Результат: [4, 2, 6, 8]


# ---
numbers = [1, 2, 4, 5, 7, 8, 10, 11]


def filter_num(in_num):
    return in_num % 2 == 0


print(list(filter(filter_num, numbers)))  # Результат: [2, 4, 8, 10]
