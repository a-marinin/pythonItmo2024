import re

# Пример №1
if re.fullmatch(r'python', 'python'):
    print(True)
else:
    print(False)
# Результат: True

# Пример №2
if re.fullmatch(r'\*python\.', '*python.'):
    print(True)
else:
    print(False)
# Результат: True
