class DataBase:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    def __init__(self, user, password, port):
        self.user = user
        self.password = password
        self.port = port

    def connect(self):
        print(f"Соединение в БД: {self.user}, {self.password}, {self.port}")

    @staticmethod
    def close():
        print("Закрытие соединения в БД")


db1 = DataBase(user='root', password='1234', port=88)
db2 = DataBase(user='root2', password='5678', port=40)
print(id(db1), id(db2))

db1.connect()
db2.connect()

# Результат:
'''
4333961824 4333961824
Соединение в БД: root2, 5678, 40
Соединение в БД: root2, 5678, 40
'''
