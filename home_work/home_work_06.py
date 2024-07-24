""" Домашнее задание № 6 """


# Задача № 1
class Rectangle:
    def __init__(self, side_1, side_2):
        self.side_1 = side_1  # 1-я сторона прямоугольника
        self.side_2 = side_2  # 2-я сторона прямоугольника

    def calculate_perimeter(self):
        perimeter = (self.side_1 + self.side_2) * 2
        print(f'Периметр прямоугольника (со сторонами {self.side_1} и {self.side_2}) равен: {perimeter}.')
        return perimeter

    def calculate_area(self):
        area = self.side_1 * self.side_2
        print(f'Площадь прямоугольника (со сторонами {self.side_1} и {self.side_2}) равна: {area}.')
        return area


triangle1 = Rectangle(side_1=1, side_2=2)
triangle2 = Rectangle(side_1=7, side_2=8)

triangle1.calculate_perimeter()  # Периметр прямоугольника (со сторонами 1 и 2) равен: 6.
triangle2.calculate_perimeter()  # Периметр прямоугольника (со сторонами 7 и 8) равен: 30.

triangle1.calculate_area()  # Площадь прямоугольника (со сторонами 1 и 2) равна: 2.
triangle2.calculate_area()  # Площадь прямоугольника (со сторонами 7 и 8) равна: 56.


# Задача № 2
class Book:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, title, author, checked_out=False):
        self.title = title
        self.author = author
        self.checked_out = checked_out

    def check_out(self):
        if not self.checked_out:
            print(f'{self.author} {self.title} - Выдаем книгу абоненту.')
            self.checked_out = True
        else:
            print(f'{self.author} {self.title} - Книга находится у абонента.')

    def check_in(self):
        if not self.checked_out:
            print(f'{self.author} {self.title} - Книга в наличии.')
        else:
            print(f'{self.author} {self.title} - Принимаем книгу в библиотеку.')
            self.checked_out = False


book1 = Book(title='Евгений Онегин', author='А. С. Пушкин')
book2 = Book(title='Братья Карамазовы', author='Ф. М. Достоевский')

print(id(book1), id(book2))  # 4405531216 4405531216
book1.check_out()  # Ф. М. Достоевский Братья Карамазовы - Выдаем книгу абоненту.
book1.check_out()  # Ф. М. Достоевский Братья Карамазовы - Книга находится у абонента.
book1.check_in()  # Ф. М. Достоевский Братья Карамазовы - Принимаем книгу в библиотеку.
book1.check_in()  # Ф. М. Достоевский Братья Карамазовы - Книга в наличии.


# Задача № 3
class Data:

    def __new__(cls, *args, **kwargs):
        print('state fetching.')  # Эта строчка выводится в консоль 1-й
        return super().__new__(cls)

    def __init__(self, my_list):
        self.my_list = my_list
        print(f'Data processing: {my_list}')  # Эта строчка выводится в консоль 2-й

    @staticmethod
    def random_method():
        print('Это строчка выводится 3-й')  # Эта строчка выводится в консоль 3-й (если вызовим этот метод)


random_data_1 = Data(my_list=[1, 2, 3, 4, 5, True, False])
random_data_1.random_method()
random_data_2 = Data(my_list=['Test', 'Testing', 'QA'])

# Результат:
'''
state fetching.
Data processing: [1, 2, 3, 4, 5, True, False]
Это строчка выводится 3-й
state fetching.
Data processing: ['Test', 'Testing', 'QA']
'''
