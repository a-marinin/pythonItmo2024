class Student:
    profession = 'Developer'

    def __new__(cls, *args, **kwargs):
        print('new')
        return super().__new__(cls)

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def check_profession(self):
        print(self.profession)


new_student = Student(first_name='Иван', last_name='Иванов', age=22)

new_student.check_profession()

print(new_student.age)
print(new_student.first_name)
print(new_student.last_name)

# Результат:
'''
Developer
22
Иван
Иванов
'''
