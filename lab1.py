import random
import matplotlib.pyplot as plt
import numpy as np

# параметры генератора
m = 16  # чётное число (2^m - модуль)
k = 17  # целое число >= 16
n = 1000 # количество значений

# создаём начальные состояния X_0 ... X_{k-1}
X = [random.randint(0, 2 ** m - 1) for _ in range(k)]

# генерируем последовательность
for i in range(n - k):
    X_next = (X[-1] + X[-k]) % (2 ** m)
    X.append(X_next)

# нормируем
Z = [x / (2 ** m) for x in X]

# выводим первые 10 значений
print("Первые 10 zi:", Z[:10])

# гистограмма относительных частот
plt.hist(Z, bins=20, density=True, edgecolor='black')
plt.title("Гистограмма относительных частот (датчик Фибоначчи)")
plt.xlabel("zi")
plt.ylabel("Относительная частота")
plt.show()

# вычисляем математическое ожидание и дисперсию
mean = np.mean(Z)
variance = np.var(Z)
print(f"Математическое ожидание: {mean:.4f}")
print(f"Дисперсия: {variance:.4f}")

# теоретические значения для равномерного [0,1)
theor_mean = 0.5
theor_var = 1 / 12
print(f"Теоретическое мат. ожидание: {theor_mean:.4f}")
print(f"Теоретическая дисперсия: {theor_var:.4f}")

# проверка корреляции для s = 2, 5, 10
s_values = [2, 5, 10]
n_values = range(50, len(Z), 10)

plt.figure(figsize=(8, 5))

for s in s_values:
    R = [np.corrcoef(Z[:nn - s], Z[s:nn])[0, 1] for nn in n_values]
    plt.plot(n_values, R, marker='o', label=f"s={s}")  # <-- линии вместо точек

plt.title("Зависимость коэффициента корреляции R от n (датчик Фибоначчи)")
plt.xlabel("Размер выборки n")
plt.ylabel("Коэффициент корреляции R")
plt.grid(True, alpha=0.3)
plt.legend()
plt.show()

