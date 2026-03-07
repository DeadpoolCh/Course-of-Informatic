import math as m
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def y(x):
    return m.sin(1-0.4*x)**2
def y_proiz(x):
    return -0.4*m.sin(2-0.8*x)
def left_diff(y0,y1,step):
    return (y1-y0)/step
def right_diff(y0,y1,step):
    return (y1-y0)/step
def mean_diff(y0,y2,step):
    return (y2-y0)/(2*step)
def tri_point_0(y0,y1,y2,step):
    return 0.5*step*(-3*y0+4*y1-y2)
def tri_point_1(y0,y2,step):
    return 0.5*step*(-y0+y2)
def tri_point_2(y0,y1,y2,step):
    return 0.5*step*(-y0+4*y1-3*y2)


step = 0.07
a, b = 1.5, 2.9
x=[i for i in np.arange(a,b+step,step)]
function=[]
proiz=[]
for i in np.arange(a,b+step,step):
    function.append(y(i))
    proiz.append(y_proiz(i))
# print(x,function,sep='\n')
plt.plot(x,function)
plt.plot(x,proiz)
plt.xlabel('x')
plt.ylabel('y(x)')
plt.show()





