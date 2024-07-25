class Encapsulation:

    def __init__(self):
        self.open_param = {'db_name': 'student', 'db_port': '3007'}  # Открытый атрибут
        self.__config = {'db_name': 'root', 'db_pass': 'nksadf#$1_sdfU'}  # Закрытый атрибут


obj = Encapsulation()

print(obj.open_param)  # Этот параметр мы можем получить извне
print(obj.__config)  # Не можем доступчаться до параметра (AttributeError)

print(obj._Encapsulation__config)  # Всё равно можем достучаться до параметра (обходной путь)
