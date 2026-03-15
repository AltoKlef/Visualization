import matplotlib.pyplot as plt
import numpy as np

# Данные
U_phase = 220
U_R0 = 1.05
U_h = 218.95

# Углы для фаз (в радианах)
# Фаза A: 90 градусов (вверх)
# Фаза B: -30 градусов (вправо-вниз)
# Фаза C: 210 градусов (влево-вниз)
angles = np.deg2rad([90, -30, 210])

# Координаты концов векторов фаз
# Фаза A (расчетная)
Ax, Ay = U_phase * np.cos(angles[0]), U_phase * np.sin(angles[0])
# Фаза B
Bx, By = U_phase * np.cos(angles[1]), U_phase * np.sin(angles[1])
# Фаза C
Cx, Cy = U_phase * np.cos(angles[2]), U_phase * np.sin(angles[2])

# Координаты для разбиения Фазы А (для наглядности)
# Конец вектора U_R0 (очень короткий, от центра)
R0_end_x = U_R0 * np.cos(angles[0])
R0_end_y = U_R0 * np.sin(angles[0])

plt.figure(figsize=(8, 8))
ax = plt.gca()

# 1. Рисуем Фазу B и C (Синие, стандартные)
ax.quiver(0, 0, Bx, By, angles='xy', scale_units='xy', scale=1, color='blue', alpha=0.5, width=0.012, label='Фазы B и C (220В)')
ax.quiver(0, 0, Cx, Cy, angles='xy', scale_units='xy', scale=1, color='blue', alpha=0.5, width=0.012)

# Подписи B и C
ax.text(Bx, By, '  Ub', fontsize=12, color='blue')
ax.text(Cx, Cy, '  Uc', fontsize=12, color='blue')

# 2. Рисуем Фазу А (Составную)
# Вектор U_R0 (Красный, от центра) - Увеличим толщину, чтобы было видно, т.к. он очень мал (1В)
ax.quiver(0, 0, R0_end_x, R0_end_y, angles='xy', scale_units='xy', scale=1, color='red', width=0.015, label=f'U_R0 = {U_R0} В')

# Вектор U_h (Зеленый, продолжает U_R0)
ax.quiver(R0_end_x, R0_end_y, Ax - R0_end_x, Ay - R0_end_y, angles='xy', scale_units='xy', scale=1, color='green', width=0.012, label=f'U_h = {U_h} В')

# Подпись фазы А
ax.text(Ax, Ay + 10, 'Ua (Фаза А)', fontsize=12, ha='center')

# Настройки графика
plt.xlim(-250, 250)
plt.ylim(-250, 250)
plt.grid(True, linestyle=':')
plt.title('Трехфазная векторная диаграмма\nс выделением падений напряжения на фазе А')
plt.legend(loc='lower left')

# Убираем оси для чистоты
ax.set_aspect('equal')
plt.xlabel('Действительная ось')
plt.ylabel('Мнимая ось (j)')

plt.show()