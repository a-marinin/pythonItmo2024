# Декоратор
def currency(currency_name):  # Функция currency примет аргумент с названием валюты
    def decor(fn):  # Создаётся декоратор, который возвращаем результат с типом валюты, примет функцию
        def wrapper(*args, **kwargs):
            result = fn(*args, **kwargs)
            return f'{result} {currency_name}'
        return wrapper
    return decor  # Возвращаем без вызова, просто название функции. () - Не нужно!


# Оригинальная функция
@currency('$')
def price_calculation(price, tax):
    return price * (1 + tax)


# Декорируем нашу функцию
print(price_calculation(100, 0.05))  # Результат: 105.0 руб./$ и т.п.
