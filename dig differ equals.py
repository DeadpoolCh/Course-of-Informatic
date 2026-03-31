"y''-y=x**2; y(0)=1, y'(0)=0. Делаем до x**6"
import sympy as sp
import math

n=6
x = sp.symbols('x')
c = sp.symbols(f'c0:{n+1}')
y = sum(c[n] * x**n for n in range(n+1))
y2 = sp.diff(y, x, 2)
expr = y2 - y - x**2
expr_series = sp.series(expr, x, 0, n+1).removeO()
equations = []
for k in range(n-1):
    coeff = expr_series.coeff(x, k)
    equations.append(coeff)

# Задаем начальные условия
equations.append(c[0] - 1)  # y(0)=1
equations.append(c[1] - 0)  # y'(0)=0

solution = sp.solve(equations, c,dict=True)[0]

print("Коэффициенты:")
for i in range(n+1):
    print(f"c{i} =", solution[c[i]])

y_series = sum(solution[c[n]] * x**n for n in range(n+1))

print(f"Решение методом разложения в степенные ряды: {y_series}")

# Функция для решения диффуров методом последовательного дифференцирования
def solve_diff_series_symbolic(N):
    x = sp.symbols('x')
    # массив функции и ее значения производных
    d = [0]*(N+1)
    # начальные условия
    d[0] = 1
    d[1] = 0
    # правая часть f = x^2
    def f_derivative(n):
        if n == 2: return 2
        else: return 0
    # считаем производные
    for n in range(2, N+1):
        d[n] = d[n-2] + f_derivative(n-2)
    print(f'\nЗначения фукнции и производных: {d}')
    # строим символьную функцию
    y_series = sum(sp.Rational(d[n], sp.factorial(n)) * x**n for n in range(N+1))
    return y_series

y = solve_diff_series_symbolic(n)
print(f"Решение методом последовательного дифференцирования: {y}")


