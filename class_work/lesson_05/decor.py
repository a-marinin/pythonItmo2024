"""
# Декоратор (только скелет декоратора)
def currency(fn):
    def wrapper(*args, **kwargs):
        fn(*args, **kwargs)

    return wrapper
"""


# Доработанный декоратор (чтобы он выполнял условия задачи)
def currency(fn):
    def wrapper(*args, **kwargs):
        result = fn(*args, **kwargs)
        # print("Была запущена функция: ", fn.__name__)  # Просто логгирование
        return f'{result} руб.'
        # return fn(*args, **kwargs)  # Возвращаем просто вызов функции fn (если не производили никаких вычислений)
    return wrapper


# Оригинальная функция
@currency
def price_calculation(price, tax):
    return price * (1 + tax)


# Декорируем нашу функцию
# price_calculation = currency(price_calculation)  # Переопределили price_calculation, задекорировав её currency.
print(price_calculation(100, 0.05))  # Результат: 105.0 руб.
