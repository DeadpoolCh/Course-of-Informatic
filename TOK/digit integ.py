import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Определяем необходимые функции
def f(x): return 1/(1+x**2)
def fr(x): return 0.9/(1+(0.9*x+0.9)**2)
# def f(x): return 1/x
# def fr(x): return np.log(x/2+1.5)
def trap(y,h):
    n=len(y)-1
    return h/2*(y[0]+y[n]+2*sum(y[1:n]))
# def pnt4(y0,y1,y2,y3,h): return 3*h/8*(y0+3*y1+3*y2+y3)
def simpson(y,h):
    n=len(y)-1
    s=0
    for i in range(0,n-2,2):
        s+=h/3*(y[i]+4*y[i+1]+y[i+2])
    return s
def gauss(type):
    if type==1: return 2*fr(0)
    elif type==2: return fr(-1/np.sqrt(3))+fr(1/np.sqrt(3))
    elif type==3: return 5/9*fr(-np.sqrt(3/5))+8/9*fr(0)+5/9*fr(np.sqrt(3/5))
def error(x,pure,type):
    if type==1: return abs(pure-x)
    if type==2: return round(abs(pure-x)/pure*100,2)

# Начальные условия
low=0
up=1.8
h=0.18
pure=1.0637

x=np.arange(low,up+h,h)
x_half=np.arange(low+h/2,up+h,h)
df = pd.DataFrame({"x":x})
df['x+h/2'] = pd.Series(x_half)
df["f"] = df["x"].apply(f)
df['rr']=df.loc[1:,'x'].apply(f)
df['cr']=df['x+h/2'].apply(f)
n=len(df['f'])

# for i in range(len(df['x'])//3):
#     y0, y1, y2 = df.loc[i*2:i*2 + 2, 'f']
#     df.loc[i,'3pt']=pnt3(y0,y1,y2,h)
# for i in range(len(df['x'])//4):
#     y0, y1, y2, y3 = df.loc[i*3:i*3 + 3, 'f']
#     df.loc[i,'4pt']=pnt4(y0,y1,y2,y3,h)

# print(df.to_string())
# df.to_excel('di.xlsx',index=False)

# lr=df['f'].sum()*h
lr_wl=df.loc[:n-2,'f'].sum()*h
rr=df['rr'].sum()*h
cr=df['cr'].sum()*h
trap_res=trap(df['f'],h)
# point3=df['3pt'].sum()
# point4=df['4pt'].sum()
simp=simpson(df['f'],h)
gausse1=gauss(1)
gausse2=gauss(2)
gausse3=gauss(3)

# plt.figure(figsize=(10,10))
# plt.plot(df['x'],df['f'],color='red')
# plt.bar(df.loc[:n-1,'x']+h/2,df.loc[:n-1,'f'],color='yellow',width=h,alpha=0.2)
# plt.bar(df.loc[:n-2,'x']+h/2,df.loc[:n-2,'f'],color='green',width=h,alpha=0.1)
# plt.show()

data={'lr':lr_wl,'rr':rr,'cr':cr,'trap':trap_res,'simp':simp,'gausse1':gausse1,'gausse2':gausse2,'gausse3':gausse3}
dfa=pd.DataFrame.from_dict(data,orient='index',columns=['res'])
dfa['abs_err']=dfa['res'].apply(error, args=(pure,1,))
dfa['rel_err']=dfa['res'].apply(error, args=(pure,2,))
print(dfa.to_string())