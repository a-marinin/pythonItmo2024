from random import randrange
""" Домашнее задание № 7 """


# Задачи № 1 и № 2

class Human:  # Класс человек
    def __init__(self, full_name, age, gender):
        self.full_name = full_name
        self.age = age
        self.gender = gender


class Teacher(Human):  # Класс учителя
    def __init__(self, full_name, age, gender):
        super().__init__(full_name, age, gender)
        self.students_qty = 0  # Количество обученных учеников

    def teach(self, material, students):
        if not isinstance(students, list):  # Если передан только 1 ученик (а не список учеников)
            students = [students]  # Создаём список с 1 учеником (str -> list)
        for student in students:  # Для каждого студента из списка студентов
            student.take(material)  # Вызываем метод “take” из класса ученика с параметром “название материала”.
            self.students_qty += 1  # Количество учеников увеличилось


class Student(Human):  # Класс ученика
    def __init__(self, full_name, age, gender):
        super().__init__(full_name, age, gender)
        self.knowledge_list = []  # Список знаний ученика

    def __len__(self):
        return len(self.knowledge_list)

    def take(self, knowledge):  # Метод "take" принимает строку знаний и добавляет ее в список знаний ученика
        self.knowledge_list.append(knowledge)  # Добавляем знание в список знаний ученика

    def forgot(self, knowledge):  #  метод, позволяющий ученику случайно "забывать" какую-нибудь часть своих знаний
        self.knowledge_list.pop(randrange(len(self.knowledge_list)))  # Забываем случайное знание из списка знаний

class LearningMaterials:  # Класс учебных материалов

    def __init__(self, *args):  # Принимает любое количество не именованных атрибутов
        self.materials_list = [*args]  # При инициализации сохранять в один атрибут в виде списка.
        # print(self.materials_list)  # Просто проверяем, правильно ли мы создали лист с материалами

    def __len__(self):
        return len(self.materials_list)


lessons = LearningMaterials('Python', 'Version Control Systems', 'Relational Databases', 'NoSQL databases', 'Message Brokers')  # Создаём объект учебных матириалов
theTeacher = Teacher(full_name='Иванов Иван Иванович', age=55, gender='male')  # Создаём объект учителя
student1 = Student(full_name='Петров Пётр Петрович', age=18, gender='male')  # Ученик №1
student2 = Student(full_name='Сидоров Сидор Сидорович', age=19, gender='male')  # Ученик №2
student3 = Student(full_name='Иванова Оксана Григорьевна', age=20, gender='female')  # Ученик №3
student4 = Student(full_name='Новиков Вяеслав Иванович', age=21, gender='male')  # Ученик №4


# Проводим обучение учеников.
# Проводим занятия по каждому материалу (с произвольным набором учеников).
theTeacher.teach(lessons.materials_list[0], [student1, student2, student3, student4])  # Обучаем 1му материалу всех уч-в
theTeacher.teach(lessons.materials_list[1], [student1, student2, student3])  # Обучаем 2му материалу 3-х учеников
theTeacher.teach(lessons.materials_list[2], [student1, student2])  # Обучаем 3му материалу 2-х учеников
theTeacher.teach(lessons.materials_list[3], student1)  # Обучаем 4му материалу одного ученика
theTeacher.teach(lessons.materials_list[4], [])  # Никого не обучаем 5му материалу

# Выводим на печать знания каждого ученика.
print(f'1-й ученик знает следующие материалы: {student1.knowledge_list}')
print(f'2-й ученик знает следующие материалы: {student2.knowledge_list}')
print(f'3-й ученик знает следующие материалы: {student3.knowledge_list}')
print(f'4-й ученик знает следующие материалы: {student4.knowledge_list}')

# Результат:
'''
1-й ученик знает следующие материалы: ['Python', 'Version Control Systems', 'Relational Databases', 'NoSQL databases']
2-й ученик знает следующие материалы: ['Python', 'Version Control Systems', 'Relational Databases']
3-й ученик знает следующие материалы: ['Python', 'Version Control Systems']
4-й ученик знает следующие материалы: ['Python']
'''

print('Количество материалов:', len(lessons))
print(f'Количество знаний у ученика №1 ({student1.full_name}, {student1.age} лет, {student1.gender}): {len(student1)} '
      f'знаний: \n {student1.knowledge_list}')
student1.forgot(len(student1))  # Ученик забывает случайное знание
print(f'Количество знаний у ученика №1 ({student1.full_name}, {student1.age} лет, {student1.gender}): {len(student1)} '
      f'знаний: \n {student1.knowledge_list}')

# Результат:
'''
Количество материалов: 5
Количество знаний у ученика №1 (Петров Пётр Петрович, 18 лет, male): 4 знаний: 
 ['Python', 'Version Control Systems', 'Relational Databases', 'NoSQL databases']
Количество знаний у ученика №1 (Петров Пётр Петрович, 18 лет, male): 3 знаний: 
 ['Version Control Systems', 'Relational Databases', 'NoSQL databases']
'''
