import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Начальные условия
x0=1
y0=1
h=0.15
eps=10**-3
# Уравнение y'-y/x=2ln(x)/x

def y(x): return 3*x-2*np.log(x)-2
def y_p(x,y): return 2*np.log(x)/x+y/x
def euler(x,y0,h):
    y=[y0]
    for i in range(len(x)-1):
        y.append(y[i] + y_p(x[i], y[i]) * h)
    return y
def up_euler(x,y0,h):
    y=[y0]
    for i in range(len(x) - 1):
        y_half=y[i]+y_p(x[i],y[i])*0.5*h
        y.append(y[i]+h*y_p(x[i]+h/2,y_half))
    return y
def up_euler_cor(x,y_r,h,eps):
    y=[y_r[0],y_r[1]]
    for i in range(len(x)-2):
        max_iter=0
        y_old = y[i+1]+2*h*y_p(x[i+1],y[i+1])
        while True:
            y_new = y[i+1]+(h/2)*(y_p(x[i+1],y[i+1])+y_p(x[i+2],y_old))
            if abs(y_new-y_old)<eps or max_iter >= 100:
                break
            y_old = y_new
            max_iter+=1
        y.append(y_new)
    return y
def rk4(x,y0,h):
    y=[y0]
    for i in range(len(x)-1):
        k0=h*y_p(x[i],y[i])
        k1=h*y_p(x[i]+h/2,y[i]+k0/2)
        k2=h*y_p(x[i]+h/2,y[i]+k1/2)
        k3=h*y_p(x[i]+h,y[i]+k2)
        y.append(y[i]+1/6*(k0+2*k1+2*k2+k3))
    return y
def miln(x,y,h):
    y_m=[y[0],y[1],y[2],y[3]]
    for i in range(3,len(x)-1):
        y_m.append(y_m[i-3]+(4/3)*h*(2*y_p(x[i-2],y_m[i-2])-y_p(x[i-1],y_m[i-1])+2*y_p(x[i],y_m[i])))
    return y_m
def miln_cor(x,y,h,eps):
    y_m = [y[0], y[1], y[2], y[3]]
    for i in range(3, len(x) - 1):
        max_iter=0
        y_old=y_m[i-3]+(4/3)*h*(2*y_p(x[i-2], y_m[i-2])-y_p(x[i-1],y_m[i-1])+2*y_p(x[i],y_m[i]))
        while True:
            y_new=y_m[i-1]+(h/3)*(y_p(x[i-1],y_m[i-1])+4*y_p(x[i],y_m[i]))
            if abs(y_new - y_old) < eps or max_iter >= 100:
                break
            y_old = y_new
            max_iter += 1
        y_m.append(y_new)
    return y
def adams(x,y,h):
    y_m=[y[0],y[1],y[2],y[3]]
    for i in range(3,len(x)-1):
        y_m.append(y_m[i]+(1/24)*h*(55*y_p(x[i],y_m[i])-59*y_p(x[i-1],y_m[i-1])+37*y_p(x[i-2],y_m[i-2])-9*y_p(x[i-3],y_m[i-3])))
    return y_m
def adams_cor(x,y,h,eps):
    y_m = [y[0], y[1], y[2], y[3]]
    for i in range(3, len(x) - 1):
        max_iter=0
        y_old=(y_m[i]+(1/24)*h*(55*y_p(x[i],y_m[i])-59*y_p(x[i-1],y_m[i-1])+37*y_p(x[i-2],y_m[i-2])-9*y_p(x[i-3],y_m[i-3])))
        while True:
            y_new=y_m[i]+(h/24)*(9*y_p(x[i+1],y_old)+19*y_p(x[i],y_m[i])-5*y_p(x[i-1],y_m[i-1])+y_p(x[i-2],y_m[i-2]))
            if abs(y_new - y_old) < eps or max_iter >= 100:
                break
            y_old = y_new
            max_iter += 1
        y_m.append(y_new)
    return y_m
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



step=10
x=np.arange(x0,x0+h*(step+1),h)
df=pd.DataFrame({"x":x})
df["real_y"]=df['x'].apply(y)
df['y_euler']=euler(df['x'],y0,h)
df["y_up_euler"]=up_euler(df['x'],y0,h)
df["y_up_euler_cor"]=up_euler_cor(df['x'],df['y_up_euler'],h,eps)
df['y_rk4']=rk4(df['x'],y0,h)
df['y_miln']=miln(df['x'],df['y_rk4'],h)
df['y_miln_cor']=miln_cor(df['x'],df['y_rk4'],h,eps)
df['y_adams']=adams(df['x'],df['y_rk4'],h)
df['y_adams_cor']=adams_cor(df['x'],df['y_rk4'],h,eps)


methods=['y_euler','y_up_euler','y_up_euler_cor','y_rk4','y_miln','y_miln_cor','y_adams','y_adams_cor']
for m in methods:
    df[f'abs_err_{m}'] = abs(df["real_y"] - df[m])
    df[f'rel_err_{m}'] = df[f'abs_err_{m}']/abs(df["real_y"])*100


plot([f'abs_err_{m}' for m in methods],"Абсолютные ошибки f'",ylabel="absolute error",log=True)
plot([f'rel_err_{m}' for m in methods],"Относительные ошибки f'",ylabel="relative error, %")

print(df.to_string())