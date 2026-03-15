import random
import numpy as np
import matplotlib.pyplot as plt


# --- Исходные данные ---
x_values = [-96.9, -87.4, -55.7, -54.5, 59.7, 83.5, 99.3]
p_values = [0.114, 0.090, 0.270, 0.192, 0.086, 0.242, 0.006]

# --- Сортировка по x ---
data = sorted(zip(x_values, p_values), key=lambda t: t[0])
x_values, p_values = map(list, zip(*data))

K = len(x_values)
p_segments = np.cumsum(p_values)  # правая граница интервала

# --- Генератор методом инверсии ---
def next_x():
    z = random.random()
    for k in range(K - 1):
        if z < p_segments[k]:
            return x_values[k]
    return x_values[-1]

# --- Генерация выборки ---
n = 1500
sample = [next_x() for _ in range(n)]

# --- Эмпирические и теоретические оценки ---
M_empirical = np.mean(sample)
D_empirical = np.var(sample)

M_theoretical = sum(x * p for x, p in zip(x_values, p_values))
D_theoretical = sum((x - M_theoretical)**2 * p for x, p in zip(x_values, p_values))

# --- Эмпирические вероятности ---
unique, counts = np.unique(sample, return_counts=True)
p_empirical = counts / n
empirical_dict = dict(zip(unique, p_empirical))
p_emp_full = [empirical_dict.get(x, 0) for x in x_values]



# --- Вывод ---
print("=" * 90)

print("=" * 90)
print("Первые 30 сгенерированных значений x_i:\n")
print(", ".join([f"{val:6.1f}" for val in sample[:30]]))
print("=" * 90)
print(f"Теоретическое M = {M_theoretical:.4f}")
print(f"Эмпирическое M  = {M_empirical:.4f}")
print()
print(f"Теоретическая D = {D_theoretical:.4f}")
print(f"Эмпирическая D  = {D_empirical:.4f}")
print("=" * 90)

# --- Гистограммы ---
fig, ax = plt.subplots(figsize=(9, 5))
width = 3

ax.bar(np.array(x_values) - width/2, p_values, width=width, label='Теоретические вероятности', alpha=0.6)
ax.bar(np.array(x_values) + width/2, p_emp_full, width=width, label='Эмпирические вероятности', alpha=0.6)

ax.set_xlabel("Значения x")
ax.set_ylabel("Вероятности")
ax.set_title("Сравнение эмпирических и теоретических вероятностей (отсортировано по x)")
ax.legend()
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()
