
my_list = [1, 2, 3, 4, 5, 6, 7]

for i in my_list:  # Цикл for пробегается по list
    print(i ** 2)  # Возводим в квадрат каждое число из my_list

my_str = 'строкa'

for i in my_str:  # Цикл for пробегается по str
    print(i)  # Выводис каждый элемент из str на новой строчке

# Task 1
# 1-й вариант решения задачи № 1 (через цикл for)
def task_1(task_list):
    result = 0
    for x in task_list:
        result = result + x
    return result


# 2-й вариант решения задачи № 1 (через функцию sum)
def task_1_v2(task_list):
    return sum(task_list)


task_1_list = [1, 5.3, 6, 3, .7, 4]
task_1(task_1_list)

