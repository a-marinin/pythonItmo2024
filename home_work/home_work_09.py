import re
""" Домашнее задание № 9 """


# Задача № 1
"""
Легковой автомобиль:
    1) 1 буква (одна из 12-ти букв: А, В, Е, К, М, Н, О, Р, С, Т, У и Х)
    2) 3 цифры
    3) 2 буквы (одна из 12-ти букв: А, В, Е, К, М, Н, О, Р, С, Т, У и Х)
    4) 2 или 3 цифры (с кодом региона)

Такси:
    1) 2 буквы (одна из 12-ти букв: А, В, Е, К, М, Н, О, Р, С, Т, У и Х)
    2) 3 цифры
    3) 2 или 3 цифры (с кодом региона)
"""


def check_car_registration_plates(reg_plate: str):
    if bool(re.fullmatch(r'[АВЕКМНОРСТУХ]\d{3}[АВЕКМНОРСТУХ]{2}\d{2,3}', reg_plate)):
        print(f'Регистрационный знак {reg_plate} валидный! Это легковой автомобиль')
        return 'Обычный легковой автомобиль'

    elif bool(re.fullmatch(r'[АВЕКМНОРСТУХ]{2}\d{3}\d{2,3}', reg_plate)):
        print(f'Регистрационный знак {reg_plate} валидный! Это такси')
        return 'Такси'

    else:
        print(f'Регистрационный знак {reg_plate} не валиден.')
        return None


print(check_car_registration_plates(reg_plate='КУ22777'))  # Валидный регистрационный знак такси
print(check_car_registration_plates(reg_plate='М123УУ777'))  # Валидный регистрационный знак легкового автомобиля
print(check_car_registration_plates(reg_plate='ЮЯ22777'))  # Не валидный регистрационный знак (используем запрещённые буквы)
print(check_car_registration_plates(reg_plate='123УУ777'))  # Не валидный регистрационный знак (неверная последовательность цифр и букв)

# Результат:
"""
Регистрационный знак КУ22777 валидный! Это такси
Такси
Регистрационный знак М123УУ777 валидный! Это легковой автомобиль
Обычный легковой автомобиль
Регистрационный знак ЮЯ22777 не валиден.
None
Регистрационный знак 123УУ777 не валиден.
None
"""
