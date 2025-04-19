# NumPy Categorization Tasks
# Анализ категориальных признаков и построение масок

import numpy as np

# ==============================
# 📦 Исходные массивы
# ==============================

# Задача 1: Подсчёт категорий
orders = np.array(['A', 'B', 'A', 'C', 'B', 'A', 'C', 'C', 'B', 'A'])
segments, counts = np.unique(orders, return_counts=True)
print("Сегменты:", segments)
print("Частоты:", counts)

# Задача 2: Пол клиентов
genders = np.array(['male', 'female', 'male', 'male', 'female', 'female', 'male', 'female'])
sex, counts = np.unique(genders, return_counts=True)
print("Пол:", sex)
print("Количество:", counts)

# Задача 3: Возраст и группы
ages = np.array([22, 35, 40, 19, 33, 25, 28, 41])
groups = np.array(['A', 'B', 'B', 'C', 'B', 'A', 'C', 'B'])
mask = (groups == 'B') & (ages > 30)
count = np.sum(mask)
print("Клиентов из группы 'B' старше 30:", count)

# Задача 4: Сегмент + покупки
purchases = np.array([1, 3, 0, 4, 2, 5, 3, 1])
segments =  np.array(['X', 'Y', 'X', 'X', 'Y', 'X', 'Y', 'X'])
mask = (segments == 'X') & (purchases > 2)
count = np.sum(mask)
print("Сегмент X, покупки > 2:", count)

# Задача 5: Премиум-клиенты + траты
is_premium = np.array([True, False, True, True, False, True, False, True])
spends =     np.array([  90,   150,  110, 130,    80, 200,   70,  105])
mask = is_premium & (spends > 100)
count = np.sum(mask)
print("Премиум-клиенты с тратами > 100:", count)

# Задача 6: Регион + покупки >= 3
regions =    np.array(['North', 'South', 'North', 'East', 'South', 'North', 'East', 'North'])
purchases = np.array([2,        4,        3,       1,      5,        6,       2,       3])
mask = (regions == 'North') & (purchases >= 3)
count = np.sum(mask)
print("Клиенты из North с >= 3 покупками:", count)

# Задача 7: A или B + траты > 100
segments = np.array(['A', 'B', 'C', 'A', 'B', 'C', 'B', 'A'])
spends =   np.array([120,  80, 150,  90, 200, 130,  50,  60])
mask = ((segments == 'A') | (segments == 'B')) & (spends > 100)
count = np.sum(mask)
print("Сегменты A или B с тратами > 100:", count)

# Задача 8: B + не премиум + траты > 100
segments =    np.array(['A', 'B', 'B', 'C', 'B', 'A', 'B', 'C'])
is_premium = np.array([True, False, True, False, False, True, False, True])
spends =     np.array([  80,   120,   90,   150,  130,   60,   105,  170])
mask = ((segments == 'B') & (is_premium == False) & (spends > 100))
count = np.sum(mask)
print("Не премиум B с тратами > 100:", count)

# Задача 9: Новый клиент из South + покупки > 3
region =    np.array(['North', 'South', 'South', 'East', 'South', 'North', 'East', 'South'])
is_new =    np.array([False,  True,    True,    True,  False,    True,   False,  True])
purchases = np.array([2,      5,       1,       4,     3,        6,      2,      7])
mask = ((region == 'South') & (is_new == True) & (purchases > 3))
count = np.sum(mask)
print("Новые клиенты из South с покупками > 3:", count)

# Задача 10: Женщины из C, траты в диапазоне
segments = np.array(['A', 'C', 'B', 'C', 'C', 'A', 'B', 'C'])
gender =   np.array(['female', 'female', 'male', 'female', 'male', 'female', 'female', 'female'])
spends =   np.array([  80,      150,     200,   110,    90,    130,     140,     100])
mask = ((segments == 'C') & (gender == 'female') & (spends >= 100) & (spends <= 200))
count = np.sum(mask)
print("Женщины из C с тратами 100–200:", count)

# Задача 11: Города со средней тратой > 120
cities = np.array(['Paris', 'London', 'Paris', 'Berlin', 'London', 'Paris', 'Berlin', 'London'])
spends = np.array([100,     150,      200,     130,      110,     180,     95,      160])

unique_cities = np.unique(cities)
count = 0
for city in unique_cities:
    city_mask = cities == city
    mean_spend = np.mean(spends[city_mask])
    if mean_spend > 120:
        count += 1
print("Городов со средней тратой > 120:", count)
