import numpy as np
def seidel(A, b, eps, max_iter=1000):
    A = np.array(A)
    b = np.array(b)
    n = len(b)
    x = np.zeros(n) # начальные значения
    for k in range(max_iter):
        x_new = x.copy()
        for i in range(n):
            s1 = sum(A[i][j] * x_new[j] for j in range(i))  # обновлённые значения
            s2 = sum(A[i][j] * x[j] for j in range(i + 1, n))  # старые значения
            x_new[i] = (b[i] - s1 - s2) / A[i][i]
        if np.max(np.abs(x_new-x)) < eps:
            return x_new, k + 1
        x = x_new

A = [[6, 2, 1],
    [2, 7, 2],
    [1, 2, 6]]
b = [9, 13, 11]
x, iterations = seidel(A, b, eps=10**-6)
print(f"Решение: x={x[0]}, y={x[1]}, z={x[2]}")
print("Итераций:", iterations)