
# пазиционные аргументы

def add(*args):
    value = 0
    for item in args:
        if isinstance(item, (int, float)):
            value += item

    return value


total = add(1, "function", 2, 3, "python", 5.1, "kwargs")
print("Total: ", total)


def print_kwargs(**kwargs):
    print(kwargs)


print_kwargs(kone="one", ktwo=3, kthree=3.0)  # Получаем {'kone': 'one', 'ktwo': 3, 'kthree': 3.0}


# Ещё один частый случай записи:
def main(*args, **kwargs):
    # На тот случай, когда мы абсолютно не знаем какие аргументы может получать функция (и именнованные и не именнованные).
    pass