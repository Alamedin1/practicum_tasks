# # Используйте векторы из Numpy, чтобы считать сразу по всем ингредиентам.
# import numpy as np

# # Функция для красивого вывода ингредиентов на экран.


# def print_ingredients(ingredients):
#     print("Яйца:", ingredients[0], "шт.")
#     print("Мука:", ingredients[1], "ст.")
#     print("Молоко:", ingredients[2], "л")
#     print("Сахар:", ingredients[3], "ст. л.")
#     print("Соль:", ingredients[4], "ч. л.")
#     print("Растительное масло:", ingredients[5], "ст. л.")


# def calc_ingredients(n_portions):
#     # portion_for_4 = np.array([3/4, 1/4, 0.4/4, 1/4, 0.5/4, 1.5/4])
#     portion_for_4 = np.array([3, 1, 0.4, 1, 0.5, 1.5])
#     portion_for_1 = portion_for_4/4
#     vec = portion_for_1 * n_portions
#     return vec


# # print(calc_ingredients(4))

# ingredients_5 = calc_ingredients(5)
# # ingredients_8 = calc_ingredients(8)
# # ingredients_10 = calc_ingredients(10)
# print_ingredients(np.array([1, 2, 3, 4, 5, 6]))

# # Пример использования функции print_ingredients
# # ingredients_3 = calc_ingredients(3)
# # print_ingredients(ingredients_)

"""
По длине плечевой кости можно примерно оценить 
рост человека по следующей линейной зависимости (в сантиметрах):
 - для женщин: рост = длина плеча * 2.75 + 71.48
 - для мужчин: рост = длина плеча * 2.89 + 70.64

Во время раскопок древних руин были обнаружены плечевые кости длиной 
36,28,42 и 32 см, принадлежащие четырём разным людям.

Оцените рост этих людей с помощью зависимости и выведите
два вектора: в первом оценки роста из предположения, что они женщины, 
во втором — из предположения, что они мужчины.
"""

# import numpy as np

# sholder_height = np.array([36, 28, 42, 32])


# def woman_height(x):
#     y = 2.75*x + 71.48
#     return y


# def men_height(x):
#     y = 2.89*x + 70.64
#     return y


# print(woman_height(sholder_height))
# print(men_height(sholder_height))

"""
Блогер заметил, что на его видеоканале количество подписчиков растёт линейно 
с каждым прошедшим месяцем, начиная с января этого года. 
На начало января было 3210 подписчиков, и каждый месяц в среднем прибавляется по 130. 
Спрогнозируйте, сколько подписчиков ожидается в конце мая, августа, сентября и декабря.
"""

# import numpy as np
# month = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

# first_followers = 3210
# increas_followers = 130


# def sub_forecast(month):
#     y = month*increas_followers + first_followers
#     return y


# may = sub_forecast(month[4])
# august = sub_forecast(month[7])
# september = sub_forecast(month[8])
# december = sub_forecast(month[11])


# print('За май: ', may, "\n",
#       'За август: ', august, "\n",
#       'За сентябрь: ', september, "\n",
#       'За декабрь: ', december)

# # Воспользуйтесь векторами для прогноза сразу для всех месяцев.
# month = np.array([5, 8, 9, 12])

# first_followers = 3210
# increas_followers = 130


# def sub_forecast(month):
#     y = month*increas_followers + first_followers
#     return y


# month = sub_forecast(month)
# print(month)
