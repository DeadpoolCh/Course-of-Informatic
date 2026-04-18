import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Параметры модели
a = 0.13
b = 0.13
k = 8
e = [0.0001, 0.001, 0.01, 0.05]
μ1 = 0.07
μ2 = 0.3

# Время интегрирования (мс)
t = np.linspace(0, 400, 10000)

# Система дифференциальных уравнений
def aliev_panfilov(y, t, ε, I_stim):
    u, v = y
    du = k*u*(u - a)*(1 - u) - u*v + I_stim(t)
    dv = (ε + (μ1*v)/(μ2 + u)) * (-v - k*u*(u - b - 1))
    return [du, dv]

# Функция стимула (одиночный толчок тока)
# def stimulus(t):
#     return 0.5 if 10 <= t <= 12 else 0.0
def stimulus(t):
    return 0.5 if 10 <= t <= 12 or 62 <= t <= 64  else 0.0

# Функция длительности ПД
def dt(u):
    zero_index = np.where(np.isclose(u, 0, atol=1e-1))[0]
    t_zero = t[zero_index]
    dt = np.diff(t_zero)
    return round(max(dt))

# Функция для графиков
def plot(t, solution,e):
    u, v = solution[:, 0], solution[:, 1]
    plt.plot(t, u, 'b-', linewidth=2, label='Потенциал u (нормированный)')
    plt.plot(t, v, 'r--', linewidth=2, label='Переменная восстановления v')
    plt.xlabel('Время (мс)')
    plt.ylabel('Значение')
    plt.title(f'Потенциал действия в модели Алиева–Панфилова.\nЗначение ε = {e}, длительность ПД = {dt(u)} мс')
    plt.legend()
    plt.grid(True)
    plt.show()

# Начальные условия: потенциал покоя, v0 = 0
u0 = 0.0
v0 = 0.0
y0 = [u0, v0]

# Построение графика
# for e in ε:
#     plt.figure(figsize=(8, 5))
#     solution = odeint(aliev_panfilov, y0, t, args=(e,stimulus,))
#     plot(t, solution,e)

plt.figure(figsize=(8, 5))
solution = odeint(aliev_panfilov, y0, t, args=(e[0],stimulus,))
plot(t, solution,e[0])
