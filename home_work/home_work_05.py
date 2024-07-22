from datetime import datetime
import time

""" Домашнее задание № 5 """


# Задача № 1
def decor_func(f):  # Это декоратор
    def result(x):  # Такая запись возможно, если мы точно уведерены, что все функции будут принимать только 1 аргумент
        r = f(x)  # Вызывает функцию, которую мы принями в качестве аргумента, передаём в неё x
        if isinstance(r, int):  # Если декорируемая функция возвращает тип данных int
            print(f'{r} - Тип данных int. Всё в порядке.')
        else:  # Если декорируемая функция возвращает тип данных отличный от int
            print(f'{r} - Тип данных не int! Выводим ошибку!')
            raise Exception('Декорируемая функция возвращает тип данных не int')  # Выводим кастомное исключение
        return r
    return result


@decor_func
def square(x):  # Это Функция 1 - возвращает квадрат числа
    return x ** 2


@decor_func  # Это Функция 2 - возвращает произведения числа и 2-х
def multiply(x):
    return x * 2


square(3)  # 9 - Тип данных int. Всё в порядке.
multiply(3)  # 6 - Тип данных int. Всё в порядке.

# square(3.1)  # Exception: Декорируемая функция возвращает тип данных не int
# multiply(3.1)  # Exception: Декорируемая функция возвращает тип данных не int


# Задача № 2
elements = [(2, 12, "Mg"), (1, 11, "Na"), (1, 3, "Li"), (2, 4, "Be")]
sorted_elem = sorted(elements, key=lambda x: (x[1], x[2]))  # Сортируем кортежи по 2-м элементам (2-му и 3-му)
print(sorted_elem)  # [(1, 3, 'Li'), (2, 4, 'Be'), (1, 11, 'Na'), (2, 12, 'Mg')]


# Задача № 3
def decor_time_count(f):  # Это декоратор (измеряет время выполнения функции)
    def result(x):
        time_start = datetime.now()  # Время до вызова функции
        print(f"Время начала работы функции: {time_start.strftime('%Y-%m-%d %H:%M:%S')}")
        r = f(x)  # Непосредственный вызов функции, которую мы принями в качестве аргумента
        time_finish = datetime.now()  # Время после вызова функции
        print(f"Время окончания работы функции {time_finish.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Выполнение функции заняло {(time_finish - time_start).total_seconds()} секунд.")
        return r
    return result


@decor_time_count
def func_wait_some_seconds(x):  # Функция 1
    time.sleep(x)
    return x


@decor_time_count  # Функция 2
def test(x):
    return x ** x


func_wait_some_seconds(1)  # Выполнение функции заняло 1.004618 секунд.
func_wait_some_seconds(5)  # Выполнение функции заняло 5.003221 секунд.
func_wait_some_seconds(10)  # Выполнение функции заняло 10.005206 секунд.

test(999999)  # Выполнение функции заняло 3.781514 секунд.
