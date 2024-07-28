from abc import ABC, abstractmethod
""" Домашнее задание № 8 """


# Задача № 1
class Ingredient:
    @abstractmethod
    def get_name(self):
        pass

    @abstractmethod
    def get_quantity(self):
        pass


class Vegetable(Ingredient):
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity
        self.type = 'Овощь'

    def get_name(self):
        return self.name

    def get_quantity(self):
        return self.quantity


class Fruit(Ingredient):
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity
        self.type = 'Фрукт'

    def get_name(self):
        return self.name

    def get_quantity(self):
        return self.quantity


cucumber = Vegetable(name='Огурец', quantity=5)
pear = Fruit(name='Груша', quantity=1)

print(f'{cucumber.type} {cucumber.get_name()} в количестве {cucumber.get_quantity()} шт.')
print(f'{pear.type} {pear.get_name()} в количестве {pear.get_quantity()} шт.')

# Результат:
# Овощь Огурец в количестве 5 шт.
# Фрукт Груша в количестве 1 шт.

for i in (cucumber, pear):
    print(f'{i.get_name()}, {i.get_quantity()} шт.')

# Результат:
# Огурец, 5 шт.
# Груша, 1 шт.
