""" Домашнее задание № 7 """


# Задача № 1
class Teacher:  # Класс учителя
    def __init__(self, students_qty):
        self.students_qty = students_qty  # Количество обученных учеников

    # TODO
    def teach(self, material, *kwargs):
        for student in kwargs:
            student.take(material)
            self.students_qty += 1  # Количество учеников увеличилось


class Student:  # Класс ученика
    def __init__(self, knowledge_list=None):
        if knowledge_list is None:
            knowledge_list = []
        self.knowledge_list = knowledge_list  # Список знаний ученика

    def take(self, knowledge):  # Метод "take" принимает строку знаний и добавляет ее в список знаний ученика
        self.knowledge_list.append(knowledge)  # Добавляем знание в список знаний ученика


class LearningMaterials:  # Класс учебных материалов

    def __new__(cls, *args, **kwargs):
        materials_list = [*args]  # при инициализации сохранять в один атрибут в виде списка.
        # print(materials_list)  # Проверяем, правильно ли мы создали лист с материалами

    def __init__(self):  # Принимает любое количество не именованных атрибутов
        self.materials_list = self.materials_list
        print(self.materials_list)

    def __getitem__(self, i):  # Получение значения по ключу
        return self.materials_list[i]


lessons = LearningMaterials('Python', 'Version Control Systems', 'Relational Databases', 'NoSQL databases', 'Message Brokers')  # Создаём объект учебных матириалов
theTeacher = Teacher(students_qty=0)  # Создаём объект учителя
student1 = Student()  # Ученик №1
student2 = Student()  # Ученик №2
student3 = Student()  # Ученик №3
student4 = Student()  # Ученик №4

# temp
print(lessons.materials_list[0])

# Проводим обучение
theTeacher.teach(lessons, student1)
theTeacher.teach(lessons, student1)
print(student1.knowledge_list)


