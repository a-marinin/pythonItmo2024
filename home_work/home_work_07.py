""" Домашнее задание № 7 """


# Задача № 1
class Teacher:  # Класс учителя
    def __init__(self):
        self.students_qty = 0  # Количество обученных учеников

    # TODO
    def teach(self, material, students):
        if not isinstance(students, list):  # Если передан только 1 ученик (а не список учеников)
            students = [students]  # Создаём список с 1 учеником (str -> list)
        for student in students:  # Для каждого студента из списка студентов
            student.take(material)  # Вызываем метод “take” из класса ученика с параметром “название материала”.
            self.students_qty += 1  # Количество учеников увеличилось


class Student:  # Класс ученика
    def __init__(self):
        self.knowledge_list = []  # Список знаний ученика

    def take(self, knowledge):  # Метод "take" принимает строку знаний и добавляет ее в список знаний ученика
        self.knowledge_list.append(knowledge)  # Добавляем знание в список знаний ученика


class LearningMaterials:  # Класс учебных материалов

    # def __new__(cls, *args, **kwargs):
    #     materials_list = [*args]  # при инициализации сохранять в один атрибут в виде списка.
    #     # print(materials_list)  # Проверяем, правильно ли мы создали лист с материалами

    def __init__(self, *args):  # Принимает любое количество не именованных атрибутов
        self.materials_list = [*args]  # При инициализации сохранять в один атрибут в виде списка.
        # print(self.materials_list)  # Просто проверяем, правильно ли мы создали лист с материалами


lessons = LearningMaterials('Python', 'Version Control Systems', 'Relational Databases', 'NoSQL databases', 'Message Brokers')  # Создаём объект учебных матириалов
theTeacher = Teacher()  # Создаём объект учителя
student1 = Student()  # Ученик №1
student2 = Student()  # Ученик №2
student3 = Student()  # Ученик №3
student4 = Student()  # Ученик №4


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

