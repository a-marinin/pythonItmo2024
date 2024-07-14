""" Домашнее задание № 2 """

# Задача № 1
my_str = "List Type Data Date Step"
print(my_str[0:len(my_str):5])  # Выводим в консоль первые буквы каждого слова
print(my_str[0:4])  # Выводим в консоль первое слово
print(my_str[-4:])  # Выводим в консоль последнее слово
print()

# Задача № 2
my_list = ["List", "Type", "Data", "Date", "Step"]
# my_str1 = str(my_list)
# print(str(my_list), type(my_list))
x = ', '.join(my_list)
print('x = ', x)
print('type(x): ', type(x))
print()

# Задачи № 3 и 4
month_num = 8
month_list = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь',
              'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']
if month_num in range(1, 13):  # Если число входит в диапозон от 1 до 12
    # Выводим в консоль номер месяца и его название
    print(f"{month_num}-й месяц года - это {month_list[month_num-1]}")
elif month_num not in range(1, 13) and isinstance(month_num, int):  # Если чисто не входит в диапозон от 1 до 12
    print(f"{month_num} - это не похоже на номер месяца")
elif not isinstance(month_num, int):  # Если чисто не является целым числом (int)
    print(f"{month_num} - это не целое число")

