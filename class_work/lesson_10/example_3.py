import matplotlib.pyplot as plt

with open('data.txt', 'r') as f:
    def my_int(x):
        try:
            return int(x)
        except:
            return x

    data = list(filter(lambda x: type(x) == int, map(my_int, list(f.read()))))


print(data)  # Результат: [2, 5, 6, 9, 1, 6, 5, 7, 9, 1, 7, 4, 6, 5, 8, 4, 8, 7, 4, 1]

plt.plot(data)
plt.show()
