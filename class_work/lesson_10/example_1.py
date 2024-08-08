# Задание 1
with open('data.txt', 'w+') as f:

    f.write('test file\n')

    data = ['test\n', 'line\n', 'write\n']
    f.writelines(data)


# Задание 2
with open('data.txt', 'w+') as f:
    data = f.read()
print(data)