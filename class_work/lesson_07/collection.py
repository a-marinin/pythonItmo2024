class Collection:
    def __init__(self, my_list):
        self.my_list = my_list

    def __len__(self):
        return len(self.my_list)

    def __del__(self):
        print('Удаляется объект класса Collection')


obj1 = Collection([1, 2, 3, 4])

print(len(obj1))  # Результат: 4
del obj1  # Результат: Удаляется объект класса Collection
# print(obj1)  # Ошибка NameError: name 'obj1' is not defined
