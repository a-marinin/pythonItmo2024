from abc import ABC, abstractmethod


class User(ABC):  # INFO: Это пример абстракции
    def __init__(self, name, password):
        self.name = name
        self.password = password

    @abstractmethod  # INFO: Это пример абстракции
    def login(self):
        pass


class Admin(User):
    def login(self):
        print(f'{self.name} - login')


class Teacher(User):
    def login(self):
        print(f'{self.name} - login')


class Student(User):  # Тут будет ошибка, т.к. метод Student не имеет метод 'login'
    pass


class Magistr(Student):
    def login(self):
        print(f'{self.name} - login')


admin_1 = Admin('Фёдор', '!@#GRTY%^%^')  # Результат: Фёдор - login
teacher_1 = Teacher('Мария', 'fasdfoi@#$DG_!±@')  # Результат: Мария - login
# student_1 = Student('Илья', 'asdfWER#$Y%$)IGASD')  # Ошибка: TypeError: Can't instantiate abstract class Student without an implementation for abstract method 'login'
student_m = Magistr('Илья', 'asdfWER#$Y%$)IGASD')  # Результат: Илья - login

for user in (admin_1, teacher_1, student_m):  # INFO: Тут используем полиморфизм
    user.login()
