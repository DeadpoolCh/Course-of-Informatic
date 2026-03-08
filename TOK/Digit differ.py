import math as m
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def y(x):
    return m.sin(1-0.4*x)**2
def y_proiz(x):
    return -0.4*m.sin(2-0.8*x)
def y_proiz2(x):
    return 0.32*m.cos(2-0.8*x)
def y_proiz3(x):
    return 0.256*m.sin(2-0.8*x)
def y_proiz4(x):
    return -0.2048*m.cos(2-0.8*x)
def left_diff(y0,y1,step):
    return (y1-y0)/step
def right_diff(y0,y1,step):
    return (y1-y0)/step
def mean_diff(y0,y2,step):
    return (y2-y0)/(2*step)
def tri_point_0(y0,y1,y2,step):
    return (-3*y0+4*y1-y2)/(0.5*step)
def tri_point_1(y0,y2,step):
    return (-y0+y2)/(0.5*step)
def tri_point_2(y0,y1,y2,step):
    return (y0-4*y1+3*y2)/(0.5*step)
def tri_point_sec(y0,y1,y2,step):
    return (y0-2*y1+y2)/step**2
def four_point_diff_0(y0,y1,y2,y3,step):
    return (-11*y0+18*y1-9*y2+2*y3)/(6*step)
def four_point_diff_1(y0,y1,y2,y3,step):
    return (-2*y0-3*y1+6*y2-y3)/(6*step)
def four_point_diff_2(y0,y1,y2,y3,step):
    return (y0-6*y1+3*y2+2*y3)/(6*step)
def four_point_diff_3(y0,y1,y2,y3,step):
    return (-2*y0+9*y1-18*y2+11*y3)/(6*step)
def four_point_diff_0_sec(y0,y1,y2,y3,step):
    return (2*y0-5*y1+4*y2-y3)/(step**2)
def four_point_diff_1_sec(y0,y1,y2,step):
    return (y0-2*y1+y2)/(step**2)
def four_point_diff_2_sec(y1,y2,y3,step):
    return (y1-2*y2+y3)/(step**2)
def four_point_diff_3_sec(y0,y1,y2,y3,step):
    return (-y0+4*y1-5*y2+2*y3)/(step**2)


step = 0.07
a, b = 1.5, 2.9
x=[i for i in np.arange(a,b+step,step)]
function,proiz,proiz2,proiz3,proiz4=[],[],[],[],[]
for i in np.arange(a,b+step,step):
    function.append(y(i))
    proiz.append(y_proiz(i))
    proiz2.append(y_proiz2(i))
    proiz3.append(y_proiz3(i))
    proiz4.append(y_proiz4(i))

data={"x":x,"f":function,"f'":proiz, "f''":proiz2,"f'''":proiz3,"f''''":proiz4}
df = pd.DataFrame(data)

for i in range(len(df['f'])-1):
    df.loc[i,'left diff']=left_diff(df['f'][i],df['f'][i+1],step)
    df.loc[i+1,'right diff']=right_diff(df['f'][i],df['f'][i+1],step)
for i in range(len(df['f'])-2):
    df.loc[i+1,'mean diff']=mean_diff(df['f'][i],df['f'][i+2],step)
for i in range(len(df['f']) - 2):
    df.loc[i,'tri point 0']=tri_point_0(df['f'][i],df['f'][i+1],df['f'][i+2],step)
    df.loc[i+1,'tri point 1']=tri_point_1(df['f'][i],df['f'][i+2],step)
    df.loc[i+2,'tri point 2']=tri_point_2(df['f'][i],df['f'][i+1],df['f'][i+2],step)
    df.loc[i, 'tri point sec'] = tri_point_sec(df['f'][i], df['f'][i + 1], df['f'][i + 2], step)
for i in range(len(df['f'])-3):
    df.loc[i,'four point 0']=four_point_diff_0(df['f'][i],df['f'][i+1],df['f'][i+2],df['f'][i+3],step)
    df.loc[i+1,'four point 1']=four_point_diff_1(df['f'][i],df['f'][i+1],df['f'][i+2],df['f'][i+3],step)
    df.loc[i+2,'four point 2']=four_point_diff_2(df['f'][i],df['f'][i+1],df['f'][i+2],df['f'][i+3],step)
    df.loc[i+3,'four point 3']=four_point_diff_3(df['f'][i],df['f'][i+1],df['f'][i+2],df['f'][i+3],step)
    df.loc[i, 'four point 0 sec'] = four_point_diff_0_sec(df['f'][i], df['f'][i + 1], df['f'][i + 2], df['f'][i + 3], step)
    df.loc[i + 1, 'four point 1 sec'] = four_point_diff_1_sec(df['f'][i], df['f'][i + 1], df['f'][i + 2], step)
    df.loc[i + 2, 'four point 2 sec'] = four_point_diff_2_sec(df['f'][i + 1], df['f'][i + 2], df['f'][i + 3], step)
    df.loc[i + 3, 'four point 3 sec'] = four_point_diff_3_sec(df['f'][i], df['f'][i + 1], df['f'][i + 2], df['f'][i + 3], step)

M3 = max(abs(df["f'''"]))
M4 = max(abs(df["f''''"]))
k_3pt_central = 1/6
k_3pt_edge = 1/3
k_3pt_central_sec = 1/12
k_3pt_edge_sec = 1
k_4pt = [1/4, 1/12, 1/12, 1/4]
k_4pt_sec = [11/12, 1/12, 1/12, 11/12]

df['R_3pt_central'] = k_3pt_central * step**2 * M3
df['R_3pt_edge'] = k_3pt_edge * step**2 * M3
df['R_3pt_central_sec'] = k_3pt_central_sec * step**2 * M4
df['R_3pt_edge_sec'] = k_3pt_edge_sec * step * M3
for i,col in enumerate(['four point 0','four point 1','four point 2','four point 3','four point 0 sec','four point 1 sec','four point 2 sec','four point 3 sec']):
    if "sec" in col:
        df['R_' + col] = k_4pt_sec[i-4] * step ** 2 * M4
    else:
        df['R_' + col] = k_4pt[i] * step**2 * M3


plt.figure(figsize=(10,6))
cols = ["f", "f'", "f''"]
for col in cols:
    if col in df.columns:
        plt.plot(df["x"], df[col], marker='.', label=col)
plt.title("График функции, первой и второй производной")
plt.xlabel('x')
plt.ylabel('value')
plt.legend()
plt.grid(True)
plt.show()

# Графики правой, левой и центральной разности
plt.figure(figsize=(10,6))
cols = ["left diff", "right diff", "mean diff"]
plt.plot(df["x"], df["f'"], marker='*', label="f'")
for col in cols:
    if col in df.columns:
        plt.plot(df["x"], df[col], marker='.', label=col)
plt.title("Правая, левая и центральная разности")
plt.xlabel("x")
plt.ylabel("value")
plt.grid(True)
plt.legend()
plt.show()

plt.figure(figsize=(10,6))
cols = ["tri point 0", "tri point 1", "tri point 2"]
plt.plot(df["x"], df["f'"], marker='*', label="f'")
for col in cols:
    if col in df.columns:
        plt.plot(df["x"], df[col], marker='.', label=col)
plt.title("Трёхточечное дифференцирование f'")
plt.xlabel("x")
plt.ylabel("value")
plt.grid(True)
plt.legend()
plt.show()

plt.figure(figsize=(10,6))
cols = ["four point 0", "four point 1", "four point 2", "four point 3"]
plt.plot(df["x"], df["f'"], marker='*', label="f'")
for col in cols:
    if col in df.columns:
        plt.plot(df["x"], df[col], marker='.', label=col)
plt.title("Четырёхточечное дифференцирование f'")
plt.xlabel("x")
plt.ylabel("value")
plt.grid(True)
plt.legend()
plt.show()

plt.figure(figsize=(10,6))
cols_abs_f1 = ['left diff','right diff','mean diff',
               'tri point 0','tri point 1','tri point 2',
               'four point 0','four point 1','four point 2','four point 3']
for col in cols_abs_f1:
    if col in df.columns:
        df['abs_err_'+col] = abs(df["f'"] - df[col])
        plt.plot(df['x'], df['abs_err_'+col], marker='.', label=col)
plt.title("Абсолютная ошибка f'")
plt.xlabel("x")
plt.ylabel("absolute error")
plt.grid(True)
plt.legend()
plt.show()

plt.figure(figsize=(10,6))
for col in cols_abs_f1:
    if col in df.columns:
        df['rel_err_'+col] = df['abs_err_'+col] / abs(df["f'"]) * 100
        plt.plot(df['x'], df['rel_err_'+col], marker='.', label=col)
plt.title("Относительная ошибка f'")
plt.xlabel("x")
plt.ylabel("relative error, %")
plt.grid(True)
plt.legend()
plt.show()

plt.figure(figsize=(10,6))
cols = ["R_3pt_central", "R_3pt_edge"]
for col in cols:
    if col in df.columns:
        plt.plot(df["x"], df[col], marker='.', label=col)
plt.title("Максимальная теоретическая ошибка трехточечного дифференцирования f'")
plt.xlabel("x")
plt.ylabel("R value")
plt.yscale("log")
plt.grid(True)
plt.legend()
plt.show()

plt.figure(figsize=(10,6))
cols = ["four point 0", "four point 1", "four point 2", "four point 3"]
for col in cols:
    if col in df.columns:
        plt.plot(df["x"], df["R_"+col], marker='.', label=col)
plt.title("Максимальная теоретическая ошибка четырёхточечного дифференцирования f'")
plt.xlabel("x")
plt.ylabel("value")
plt.yscale("log")
plt.grid(True)
plt.legend()
plt.show()

plt.figure(figsize=(10,6))
cols = ["tri point sec"]
plt.plot(df["x"], df["f''"], marker='*', label="f'")
for col in cols:
    if col in df.columns:
        plt.plot(df["x"], df[col], marker='.', label=col)
plt.title("Трёхточечное дифференцирование f''")
plt.xlabel("x")
plt.ylabel("value")
plt.grid(True)
plt.legend()
plt.show()

plt.figure(figsize=(10,6))
cols = ["four point 0 sec", "four point 1 sec", "four point 2 sec", "four point 3 sec"]
plt.plot(df["x"], df["f''"], marker='*', label="f''")
for col in cols:
    if col in df.columns:
        plt.plot(df["x"], df[col], marker='.', label=col)
plt.title("Четырёхточечное дифференцирование f''")
plt.xlabel("x")
plt.ylabel("value")
plt.grid(True)
plt.legend()
plt.show()

plt.figure(figsize=(10,6))
cols_abs_f2 = ['tri point','four point 0','four point 1','four point 2','four point 3']
for col in cols_abs_f2:
    if col in df.columns:
        df['abs_err_'+col+' sec'] = abs(df["f''"] - df[col+' sec'])
        plt.plot(df['x'], df['abs_err_'+col+' sec'], marker='.', label=col+' sec')
plt.title("Абсолютная ошибка f''")
plt.xlabel("x")
plt.ylabel("absolute error")
plt.grid(True)
plt.legend()
plt.show()

plt.figure(figsize=(10,6))
for col in cols_abs_f2:
    if col in df.columns:
        df['rel_err_'+col+' sec'] = df['abs_err_'+col+' sec'] / abs(df["f'"]) * 100
        plt.plot(df['x'], df['rel_err_'+col+' sec'], marker='.', label=col+' sec')
plt.title("Относительная ошибка f''")
plt.xlabel("x")
plt.ylabel("relative error, %")
plt.grid(True)
plt.legend()
plt.show()

plt.figure(figsize=(10,6))
cols = ["R_3pt_central_sec", "R_3pt_edge_sec"]
for col in cols:
    if col in df.columns:
        plt.plot(df["x"], df[col], marker='.', label=col+' sec')
plt.title("Максимальная теоретическая ошибка трехточечного дифференцирования f''")
plt.xlabel("x")
plt.ylabel("R value")
plt.yscale("log")
plt.grid(True)
plt.legend()
plt.show()

plt.figure(figsize=(10,6))
cols = ["four point 0", "four point 1", "four point 2", "four point 3"]
for col in cols:
    if col in df.columns:
        plt.plot(df["x"], df["R_"+col+' sec'], marker='.', label=col)
plt.title("Максимальная теоретическая ошибка четырёхточечного дифференцирования f''")
plt.xlabel("x")
plt.ylabel("value")
plt.yscale("log")
plt.grid(True)
plt.legend()
plt.show()

print(df.to_string())
# df.to_excel('digit differ.xlsx')




