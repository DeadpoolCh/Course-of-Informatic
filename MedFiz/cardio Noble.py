import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Константы
Cm = 12.0   # мкФ/см²
gNa = 400.0
gCa = 8.0
gK  = 8.0
ENa = 40.0
ECa = 100.0
EK  = -100.0

# Время (мс)
t = np.linspace(0, 500, 10000)

def alpha_m(V):
    return 0.1 * (V + 48) / (1 - np.exp(-(V + 48)/15)) if abs(V+48) > 1e-8 else 0.1*15

def beta_m(V):
    return 0.12 * (V + 8) / (np.exp((V+8)/5) - 1) if abs(V+8) > 1e-8 else 0.12*5

def alpha_h(V):
    return 0.17 * np.exp(-(V+90)/20)

def beta_h(V):
    return 1.0 / (1 + np.exp(-(V+42)/10))

def alpha_d(V):
    return 0.002 * (V + 50) / (1 - np.exp(-(V+50)/10)) if abs(V+50) > 1e-8 else 0.002*10

def beta_d(V):
    return 0.02 * (V + 20) / (np.exp((V+20)/10) - 1) if abs(V+20) > 1e-8 else 0.02*10

def alpha_f(V):
    return 0.001 * np.exp(-(V+50)/20)

def beta_f(V):
    return 0.002 / (1 + np.exp(-(V+20)/10))

def alpha_n(V):
    return 0.01 * (V + 50) / (1 - np.exp(-(V+50)/10)) if abs(V+50) > 1e-8 else 0.01*10

def beta_n(V):
    return 0.02 * np.exp(-(V+50)/80)

# Система уравнений
def noble(y, t, I_stim):
    V, m, h, d, f, n = y
    # Токи
    I_Na = gNa * m**3 * h * (V - ENa)
    I_Ca = gCa * d * f * (V - ECa)
    I_K  = gK  * n**4 * (V - EK)
    I_total = I_Na + I_Ca + I_K - I_stim(t)

    dVdt = -I_total / Cm

    dmdt = alpha_m(V) * (1 - m) - beta_m(V) * m
    dhdt = alpha_h(V) * (1 - h) - beta_h(V) * h
    dddt = alpha_d(V) * (1 - d) - beta_d(V) * d
    dfdt = alpha_f(V) * (1 - f) - beta_f(V) * f
    dndt = alpha_n(V) * (1 - n) - beta_n(V) * n

    return [dVdt, dmdt, dhdt, dddt, dfdt, dndt]

# Стимул: короткий импульс тока 10 мкА/см² на 10-12 мс
def stimulus(t):
    return 10.0 if 10 <= t <= 12 or 112 <= t <= 114 else 0.0

def apd90(V,t):
    peak_idx = np.where(V > 32)[0]
    splits = np.where(np.diff(peak_idx) > 1)[0] + 1
    groups = np.split(peak_idx, splits)
    true_peak = np.array([g[np.argmax(V[g])] for g in groups])
    V_90, thresholds, start_idx = [], [], []
    for n, i in enumerate(true_peak):
        V_90.append(V0 + 0.1 * (V[i] - V0))
        threshold = V0 + 0.2 * (V[i] - V0)
        thresholds.append(threshold)
        after_peak = V[i:]
    cross = np.where((after_peak[:-1] > V_90[0]) & (after_peak[1:] <= V_90[0]))[0]
    start_idx = np.where((V[:-1] < threshold) & (V[1:] >= threshold))[0]
    end_idx = true_peak + cross
    apd90 = [t[end_idx[i]] - t[start_idx[i]] for i in range(len(end_idx))]
    return round(np.mean(apd90),2)

# Начальные условия (потенциал покоя ~ -85 мВ, ворота в равновесии)
V0 = -85.0
m0 = alpha_m(V0) / (alpha_m(V0) + beta_m(V0))
h0 = alpha_h(V0) / (alpha_h(V0) + beta_h(V0))
d0 = alpha_d(V0) / (alpha_d(V0) + beta_d(V0))
f0 = alpha_f(V0) / (alpha_f(V0) + beta_f(V0))
n0 = alpha_n(V0) / (alpha_n(V0) + beta_n(V0))

y0 = [V0, m0, h0, d0, f0, n0]

# Решение
solution = odeint(noble, y0, t, args=(stimulus,))
V, m, h, d, f, n = solution[:, 0], solution[:, 1], solution[:, 2], solution[:, 3], solution[:, 4], solution[:, 5]

# Построение
plt.figure(figsize=(12, 5))
plt.plot(t, V, 'b-', linewidth=2)
plt.xlabel('Время (мс)')
plt.ylabel('Потенциал V (мВ)')
# plt.title(f'Потенциал действия в модели Нобла (клетка Пуркинье)\nСредняя длительность ПД (по 90% реполяризации) = {apd90(V, t)} мс')
plt.title(f'Потенциал действия в модели Нобла (клетка Пуркинье). gK = {gK}')
plt.grid(True)
plt.show()