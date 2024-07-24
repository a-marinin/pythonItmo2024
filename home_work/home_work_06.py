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
# Задача № 3
