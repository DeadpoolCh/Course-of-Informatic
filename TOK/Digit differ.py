import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Определяем функцию и ее четыре производные
def f(x): return np.sin(1-0.4*x)**2
def f1(x): return -0.4*np.sin(2-0.8*x)
def f2(x): return 0.32*np.cos(2-0.8*x)
def f3(x): return 0.256*np.sin(2-0.8*x)
def f4(x): return -0.2048*np.cos(2-0.8*x)
# Определяем функции для расчета разностей
def l_r_diff(y0,y1,h): return (y1-y0)/h
def mean_diff(y0,y2,h): return (y2-y0)/(2*h)
# Определяем функции для трехточечного дифференцирования
def tri_point_0(y0,y1,y2,h): return (-3*y0+4*y1-y2)/(2*h)
def tri_point_1(y0,y2,h): return (-y0+y2)/(2*h)
def tri_point_2(y0,y1,y2,h): return (y0-4*y1+3*y2)/(2*h)
def tri_point_sec(y0,y1,y2,h): return (y0-2*y1+y2)/h**2
# Определяем функции для четырехточечного дифференцирования
def four_point_diff_0(y0,y1,y2,y3,h): return (-11*y0+18*y1-9*y2+2*y3)/(6*h)
def four_point_diff_1(y0,y1,y2,y3,h): return (-2*y0-3*y1+6*y2-y3)/(6*h)
def four_point_diff_2(y0,y1,y2,y3,h): return (y0-6*y1+3*y2+2*y3)/(6*h)
def four_point_diff_3(y0,y1,y2,y3,h): return (-2*y0+9*y1-18*y2+11*y3)/(6*h)
def four_point_diff_0_sec(y0,y1,y2,y3,h): return (2*y0-5*y1+4*y2-y3)/(h**2)
def four_point_diff_1_sec(y0,y1,y2,h): return (y0-2*y1+y2)/(h**2)
def four_point_diff_2_sec(y1,y2,y3,h): return (y1-2*y2+y3)/(h**2)
def four_point_diff_3_sec(y0,y1,y2,y3,h): return (-y0+4*y1-5*y2+2*y3)/(h**2)

# Начальные условия
h = 0.07
a, b = 1.5, 2.9
x=np.arange(a,b+h,h)

# Создаем датафрейм
df = pd.DataFrame({"x":x})
df["f"] = df["x"].apply(f)
df["f'"] = df["x"].apply(f1)
df["f''"] = df["x"].apply(f2)
df["f'''"] = df["x"].apply(f3)
df["f''''"] = df["x"].apply(f4)

# Создаем строки в результате расчетов различными методами
l=len(df['f'])
for i in range(l-1):
    df.loc[i,'left diff']=l_r_diff(df.loc[i,'f'],df.loc[i+1,'f'],h)
    df.loc[i+1,'right diff']=l_r_diff(df.loc[i,'f'],df.loc[i+1,'f'],h)
for i in range(l-2):
    df.loc[i+1,'mean diff']=mean_diff(df.loc[i,'f'],df.loc[i+2,'f'],h)
    df.loc[i,'tri point 0']=tri_point_0(df.loc[i,'f'],df.loc[i+1,'f'],df.loc[i+2,'f'],h)
    df.loc[i+1,'tri point 1']=tri_point_1(df.loc[i,'f'],df.loc[i+2,'f'],h)
    df.loc[i+2,'tri point 2']=tri_point_2(df.loc[i,'f'],df.loc[i+1,'f'],df.loc[i+2,'f'],h)
    df.loc[i, 'tri point sec'] = tri_point_sec(df.loc[i,'f'], df.loc[i+1,'f'], df.loc[i+2,'f'], h)
for i in range(l-3):
    y0,y1,y2,y3=df.loc[i:i+3,'f']
    df.loc[i,'four point 0']=four_point_diff_0(y0,y1,y2,y3,h)
    df.loc[i+1,'four point 1']=four_point_diff_1(y0,y1,y2,y3,h)
    df.loc[i+2,'four point 2']=four_point_diff_2(y0,y1,y2,y3,h)
    df.loc[i+3,'four point 3']=four_point_diff_3(y0,y1,y2,y3,h)
    df.loc[i, 'four point 0 sec'] = four_point_diff_0_sec(y0, y1, y2, y3, h)
    df.loc[i + 1, 'four point 1 sec'] = four_point_diff_1_sec(y0, y1, y2, h)
    df.loc[i + 2, 'four point 2 sec'] = four_point_diff_2_sec(y1, y2, y3, h)
    df.loc[i + 3, 'four point 3 sec'] = four_point_diff_3_sec(y0, y1, y2, y3, h)

# Расчет абсолютных и относительных погрешностей
methods1 = ['left diff','right diff','mean diff','tri point 0','tri point 1','tri point 2','four point 0','four point 1','four point 2','four point 3']
methods2 = ['tri point sec','four point 0 sec','four point 1 sec','four point 2 sec','four point 3 sec']
for m in methods1:
    df[f'abs_err_{m}'] = abs(df["f'"] - df[m])
    df[f'rel_err_{m}'] = df[f'abs_err_{m}']/abs(df["f'"])*100
for m in methods2:
    df[f'abs_err_{m}'] = abs(df["f''"] - df[m])
    df[f'rel_err_{m}'] = df[f'abs_err_{m}']/abs(df["f''"])*100

# Рассчитываем максимальную теоретическую погрешность
M3 = df["f'''"].abs().max()
M4 = df["f''''"].abs().max()
k_3pt_central = 1/6
k_3pt_edge = 1/3
k_3pt_central_sec = 1/12
k_3pt_edge_sec = 1
k_4pt = [1/4, 1/12, 1/12, 1/4]
k_4pt_sec = [11/12, 1/12, 1/12, 11/12]
df['R_3pt_central'] = k_3pt_central * h**2 * M3
df['R_3pt_edge'] = k_3pt_edge * h**2 * M3
df['R_3pt_central_sec'] = k_3pt_central_sec * h**2 * M4
df['R_3pt_edge_sec'] = k_3pt_edge_sec * h * M3
for i,col in enumerate(['four point 0','four point 1','four point 2','four point 3','four point 0 sec','four point 1 sec','four point 2 sec','four point 3 sec']):
    if "sec" in col:
        df['R_' + col] = k_4pt_sec[i-4] * h ** 2 * M4
    else:
        df['R_' + col] = k_4pt[i] * h**2 * M3

# Функция для построения графиков
def plot(col,title,ref="",log=False,ylabel="value"):
    markers = ['o', 's', '^', 'x', 'd']
    plt.figure(figsize=(10, 6))
    if isinstance(col,str):
        col = [col]
    if ref:
        plt.plot(df['x'],df[ref],marker='*',label=ref)
    for i,c in enumerate(col):
        plt.plot(df["x"], df[c], marker=markers[i%len(markers)], label=c)
    if log==True:
        plt.yscale('log')
    plt.title(title)
    plt.xlabel('x')
    plt.ylabel(ylabel)
    plt.legend()
    plt.grid(True)
    plt.show()

# Различные графики
cols = ["f", "f'", "f''"]
plot(cols,"График функции, первой и второй производной")

cols = ["left diff", "right diff", "mean diff"]
plot(cols,"Правая, левая и центральная разности","f'")

cols = ["tri point 0", "tri point 1", "tri point 2"]
plot(cols,"Трёхточечное дифференцирование f'","f'")

cols = ["four point 0", "four point 1", "four point 2", "four point 3"]
plot(cols,"Четырёхточечное дифференцирование f'","f'")

plot([f'abs_err_{m}' for m in methods1],"Абсолютные ошибки f'",ylabel="absolute error")
plot([f'rel_err_{m}' for m in methods1],"Относительные ошибки f'",ylabel="relative error, %")

cols = ["R_3pt_central", "R_3pt_edge"]
plot(cols,"Максимальная теоретическая ошибка трехточечного дифференцирования f'",ylabel="R value")

cols = ["four point 0", "four point 1", "four point 2", "four point 3"]
plot([f'R_{c}' for c in cols],"Максимальная теоретическая ошибка четырёхточечного дифференцирования f'",ylabel="R value")

plot('tri point sec',"Трёхточечное дифференцирование f''","f''")

cols = ["four point 0 sec", "four point 1 sec", "four point 2 sec", "four point 3 sec"]
plot(cols,"Четырёхточечное дифференцирование f''","f''")

plot([f'abs_err_{m}' for m in methods2],"Абсолютные ошибки f''",ylabel="absolute error")
plot([f'rel_err_{m}' for m in methods2],"Относительные ошибки f''",ylabel="relative error, %")

cols = ["R_3pt_central_sec", "R_3pt_edge_sec"]
plot(cols,"Максимальная теоретическая ошибка трехточечного дифференцирования f''",ylabel="R value")

cols = ["four point 0 sec", "four point 1 sec", "four point 2 sec", "four point 3 sec"]
plot([f'R_{c}' for c in cols],"Максимальная теоретическая ошибка четырёхточечного дифференцирования f''",ylabel="R value")

# print(df.to_string())
# df.to_excel('digit differ.xlsx')