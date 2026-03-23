import math as m

# Начальные условия
a=2
b=3
eps=10**-5

# Определение границ области изоляции
# for i in range(1,50,1):
#     print(i,f(i),sep=" ")

def f(x): return m.log(x)+2*x-6
def f1(x): return 1/x+2
def f2(x): return -1/(x**2)
def x1(x): return m.exp(6-2*x)
def x11(x): return -2*m.exp(6-2*x)
def x2(x): return (6-m.log(x))/2

# Метод половинок
def half(a,b,eps):
    n=m.ceil(m.log2((b-a)/eps))
    fa,fb=f(a),f(b)
    for i in range(n):
        x=(b+a)/2
        y=f(x)
        if fa*y<=0:
            fb=y
            b=x
        else:
            fa=y
            a=x
    print(f'Метод половинок.\nКоличество итераций: {n}\nЗначение x: {x}\n')
# Метод хорд
def chord(a,b,eps):
    iter=0
    max_iter=1000
    fa,f2a,fb=f(a),f2(a),f(b)
    if fa*f2a>0: fix='a'; x=b;
    else: fix='b'; x=a
    while abs(f(x))>=eps and iter<max_iter:
        if fix=='a':
            x=a-((b-a)*fa)/(fb-fa)
            b=x
            fb=f(x)
        else:
            x = b - ((b - a) * fb) / (fb - fa)
            a = x
            fa=f(x)
        iter+=1
    print(f'Метод хорд.\nКоличество итераций: {iter}\nЗначение x: {x}\n')
# Метод касательных
def tangent(a,b,eps):
    iter=0
    max_iter=1000
    fa, f2a = f(a), f2(a)
    if fa*f2a>0: c=a;
    else: c=b
    while abs(f(c))>=eps and iter<max_iter:
        x=c-f(c)/f1(c)
        c=x
        iter+=1
    print(f'Метод касательных.\nКоличество итераций: {iter}\nЗначение x: {x}\n')
# Метод простых итераций
def simp_iter(a,b,eps):
    iter=0
    max_iter=1000
    x=a
    while abs(f(x))>=eps and iter<max_iter:
        if abs(x11(x))<1:
            x=x1(x)
        else: x=x2(x)
        iter+=1
    print(f'Метод простых итераций.\nКоличество итераций: {iter}\nЗначение x: {x}\n')

half(a,b,eps)
chord(a,b,eps)
tangent(a,b,eps)
simp_iter(a,b,eps)

