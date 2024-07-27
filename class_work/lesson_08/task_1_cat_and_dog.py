class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f'{Cat.__name__}: name - {self.name}, year - {self.age}')


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f'{Dog.__name__}: name - {self.name}, year - {self.age}')


cat1 = Cat('C1', 1)
dog1 = Dog('D1', 0.4)

for animal in (cat1, dog1):
    animal.info()
