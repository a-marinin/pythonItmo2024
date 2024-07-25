class Salary:
    def __init__(self, pay):
        self.pay = pay

    def get_total(self):
        return self.pay * 12


class Employee:
    def __init__(self, pay, bonus):
        self.pay = pay
        self.bonus = bonus
        self.salary = Salary(self.pay)  # Обращается к классу Salary

    def annual_salary(self):
        return 'Total: ' + str(self.salary.get_total() + self.bonus)


empoyee = Employee(pay=100, bonus=10)
print(empoyee.annual_salary())  # Результат: Total: 1210
