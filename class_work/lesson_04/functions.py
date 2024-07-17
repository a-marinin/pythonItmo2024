""" Определяем функцию """

def function():
    a = -2
    b = 3
    c = abs(a) ** b
    print(c)


def main(a, b):
    return a + b  # return - это иснструкция возвращает значение из функции


# Вызываем функцию
function()

main(1, 2)

print(main(23, 89))

result_main = main(23, 89)


""" Аргументы функции """

def arg(a, b, c=2, d=3):
    return a + b + c + d


print(arg(1, 1, 1, 1))

print(arg(1, 1))

# print(arg(1, 1, '1', 1))  # Ошибка (из-за строгой типизации)

# def arg(c=2, d=3, a, b):  # Ошибка (из-за порядка аргументов)
#     return a + b + c + d


def range_arg(a, b, c, d):
    return a + ' ' + b + ' ' + c + ' ' + d


print(range_arg('1', '2', '3', '4'))

print(range_arg('1', '2', d='3', c='4'))