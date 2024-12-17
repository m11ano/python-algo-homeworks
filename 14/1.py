import numpy as np
from scipy.optimize import linprog

# Данные задачи
supply = [100, 200]  # Запасы на складах C1 и C2
demand = [50, 100, 75, 75]  # Потребности магазинов M1, M2, M3, M4
costs = [  # Стоимость перевозки из складов в магазины
    [1, 4, 3, 2],  # Из C1
    [3, 8, 4, 7],  # Из C2
]

# Проверка баланса задачи
if sum(supply) != sum(demand):
    raise ValueError("Задача не сбалансирована: общая поставка != общей потребности")

# Преобразование данных для линейного программирования
num_sources = len(supply)  # Количество складов
num_destinations = len(demand)  # Количество магазинов

# Вектор коэффициентов (стоимости перевозки)
c = np.array(costs).flatten()

# Матрица ограничений для запасов
A_eq = []
b_eq = []

# Ограничения по поставке (строки матрицы)
for i in range(num_sources):
    constraint = [0] * (num_sources * num_destinations)
    for j in range(num_destinations):
        constraint[i * num_destinations + j] = 1
    A_eq.append(constraint)
    b_eq.append(supply[i])

# Ограничения по потребности (столбцы матрицы)
for j in range(num_destinations):
    constraint = [0] * (num_sources * num_destinations)
    for i in range(num_sources):
        constraint[i * num_destinations + j] = 1
    A_eq.append(constraint)
    b_eq.append(demand[j])

# Границы переменных (все перевозки >= 0)
bounds = [(0, None) for _ in range(num_sources * num_destinations)]

# Решение задачи линейного программирования
result = linprog(c, A_eq=A_eq, b_eq=b_eq, bounds=bounds, method="highs")

# Проверка результата
if result.success:
    print("Оптимальное решение найдено.")
    print("Общая стоимость перевозок:", result.fun)

    # Формирование матрицы перевозок
    transportation = np.array(result.x).reshape((num_sources, num_destinations))
    print("Матрица перевозок:")
    print(transportation)
else:
    print("Решение не найдено:", result.message)
