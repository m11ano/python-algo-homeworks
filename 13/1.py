def runge_kutta_4(f, x0, y0, x, h):
    """
    Реализация метода Рунге-Кутта 4 порядка.

    :param f: Правая часть уравнения y' = f(x, y)
    :param x0: Начальное значение x
    :param y0: Начальное значение y
    :param x: Точка, в которой вычисляется решение
    :param h: Шаг интегрирования
    :return: Значение y в точке x
    """
    n = int((x - x0) / h)
    y = y0
    for i in range(n):
        k1 = h * f(x0, y)
        k2 = h * f(x0 + h / 2, y + k1 / 2)
        k3 = h * f(x0 + h / 2, y + k2 / 2)
        k4 = h * f(x0 + h, y + k3)
        y += (k1 + 2 * k2 + 2 * k3 + k4) / 6
        x0 += h
    return y


# Задано: y' = 2x, y(0) = 1
f = lambda x, y: 2 * x
x0 = 0
y0 = 1
x = 1
h = 0.1  # шаг интегрирования

# Решение методом Рунге-Кутта 4 порядка
y_rk4 = runge_kutta_4(f, x0, y0, x, h)


# Аналитическое решение: y = x^2 + 1
def analytical_solution(x):
    return x**2 + 1


y_exact = analytical_solution(x)

# Вывод результатов
print(f"Результат методом Рунге-Кутта 4 порядка: y({x}) = {y_rk4}")
print(f"Аналитическое решение: y({x}) = {y_exact}")
print(f"Погрешность: {abs(y_rk4 - y_exact)}")
