data1 = {"X": [-1, 0, 1, 2], "p": [0.2, 0.1, 0.3, 0.4]}

data2 = {"X": [2, 3, 5], "p": [0.1, 0.6, 0.3]}


def calculate_mean(X, p):
    return sum(x * prob for x, prob in zip(X, p))


def calculate_variance(X, p, mean):
    return sum(prob * (x - mean) ** 2 for x, prob in zip(X, p))


mean1 = calculate_mean(data1["X"], data1["p"])
variance1 = calculate_variance(data1["X"], data1["p"], mean1)

mean2 = calculate_mean(data2["X"], data2["p"])
variance2 = calculate_variance(data2["X"], data2["p"], mean2)

print(f"Первый набор данных: Матожидание = {mean1}, Дисперсия = {variance1}")
print(f"Второй набор данных: Матожидание = {mean2}, Дисперсия = {variance2}")
