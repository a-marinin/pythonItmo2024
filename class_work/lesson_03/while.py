# Example 1
number = 0

while number < 10:
    print(f'number {number}')
    number += 1

print('app close')


# Example 2
string = '123'
while len(string) > 0:
    print('Строка существует' + string)
    string = string[0:-1]
else:
    print('Пустая строка')


# Example 3
numb_break = 0
while numb_break < 5:
    numb_break += 5
    if numb_break == 3:   # Если numb_break == 3 -> Выходим из цикла
        break
    print(f'numb_break = {numb_break}')

# Example 4
numb_continue = 0
while numb_continue < 5:
    numb_continue += 1
    if numb_continue == 3:  # Если numb_continue == 3 -> Переходим на следующую итерацию цикла
        continue
    print(f'numb_continue = {numb_continue}')


# Task 2
def task_2():
    task_list = []

    for i in range(10):  # range(10) - это кортеж от 0 до 10
        task_list.append(i**2)

    print(task_list)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]


task_2()
