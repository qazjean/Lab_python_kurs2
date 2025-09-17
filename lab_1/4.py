import numpy as np
from numpy.linalg import det, inv, solve

A = np.random.randint(1, 11, (5, 5))
B = np.random.randint(1, 11, (5, 5))

print("Матрица A:\n", A)
print("Матрица B:\n", B)

# Поэлементное произведение
elementnoe_proizvedenie = A * B
print("Поэлементное произведение:\n", elementnoe_proizvedenie)

# Матричное произведение
matrix_proizvedenie = A @ B
print("Матричное произведение:\n", matrix_proizvedenie)

# Определитель A
opredelitel_A = det(A)
print("Определитель A:", round(opredelitel_A, 4))

# Транспонирование B
transponir_B = B.T
print("Транспонированная B:\n", transponir_B)

# Обратная матрица A
try:
    obr_A = inv(A)
    print("Обратная матрица A:\n", np.round(obr_A, 4))
except np.linalg.LinAlgError:
    print("Матрица A вырождена")

# Решение системы уравнений
#C = A.sum(axis=1)  # Вектор сумм строк
#x = solve(A, C)
#print(C)
#print("Решение системы A*x=C:\n", x)

C = A.sum(axis=1).reshape(-1, 1)  # Преобразуем в вектор-столбец
print("Вектор C (суммы строк матрицы A):\n", C)

try:
    x = solve(A, C)
    print("Решение системы A*x=C:\n", np.round(x, 3))
except np.linalg.LinAlgError:
    print("Матрица A вырождена, система не имеет единственного решения")