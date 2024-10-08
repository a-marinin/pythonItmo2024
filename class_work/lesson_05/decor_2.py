def print_result(f):  # Это декоратор
    def result(x):  # Такая запись возможно, если мы точно уведерены, что все функции будут принимать только 1 аргумент
        r = f(x)  # Вызывает функцию, которую мы принями в качестве аргумента, передаём в неё x
        print(f'Результат вычислений: {r}')
        return r
    return result


@print_result
def square(x):  # Это Функция 1 - возвращает квадрат числа
    return x ** 2


@print_result  # Это Функция 2 - возвращает произведения числа и 2-х
def multiply(x):
    return x * 2


square(3)  # Результат вычислений: 9
multiply(3)  # Результат вычислений: 6
