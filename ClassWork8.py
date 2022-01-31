import random

# w, h = 5, 4
# matrix = [[random.randint(1, 30) for x in range(w)] for y in range(h)]  # Заполнение случайными числами
# matrix = list()
# for y in range(h):  # Тот же самый способ что и вышще только длиннее
#     m = list()
#     for x in range(w):
#         m.append(random.randint(1, 30))
#     matrix.extend([m])

# print(matrix)
# for h in matrix:
#     for w in h:
#         print(w, end="\t\t")
#     print()

# w, h = 3, 4
# k = 0
# matrix = [[random.randint(-20, 10) for x in range(w)] for y in range(h)]
# # print(matrix)
# for row in matrix:
#     for col in row:
#         if col < 0:
#             k += 1
#         print(col, end="\t\t")
#     print()
# print("Отрецательных: ", k)

# w, h = 3, 4
# k = 1
# matrix = [[random.randint(0, 4) for x in range(w)] for y in range(h)]
# # print(matrix)
# for row in matrix:
#     for col in row:
#         if col > 0:
#             k = k * col
#         print(col, end="\t\t")
#     print()
# print("Произведение равно: ", k)

# w, h = 6, 6
#
# matrix = [[random.randint(0, 4) for x in range(w)] for y in range(h)]
# # print(matrix)
# for row in matrix:
#     for col in row:
#         print(col, end="\t\t")
#     print()
# print()
# for h in range(len(matrix)):
#     if h % 2 == 0:
#         for w in range(len(matrix[h])):
#             print(matrix[h + 1][w], end="\t\t")
#         print()


#     row = matrix[row + 1]
# else:
#     row = matrix[row - 1]
# for col in row:
#     print(col, end="\t\t")
# print()

# Календарь юез выходных
# 1 2 3 4 5
# 8 9 10 11 12
# 15 16 17 18 19
# 22 23 24 25 26
# 29 30 31

# days = [d for d in range(1, 32)]
# print(days)
# print(len(days))
# weeks = [days[i:i+5] for i in range(0, len(days),7)]
# print(weeks)
# for row in weeks:
#     for x in row:
#         print(x, end="\t\t")
#     print()

import \
    math as m  # ПОДКЛЮЧАЕМЫЙ МОДУЛЬ --------------------------------------------------------------------------------------
from math import *

# print(m.sqrt(2))
# print(m.floor(3.8)) # Округление вниз
# print(m.ceil(3.8)) #Округление вверх
#
# from math import sqrt, floor, ceil
#
# print(m.sqrt(2))
# print(m.floor(3.8)) # Округление вниз
# print(m.ceil(3.8)) #Округление вверх


# r = float(input("Введите радиус окпужности: "))
# f = 2 * pi * r
# print("Длина окружности:", round(f, 2))

# lst = [1, 5, 3, 8.4]
# print(sum(lst))
# print(fsum(lst))
#
# print(degrees(3.14159)) # перевод из радиан в градусы
# print(radians(180)) # обратно в радианы
# print(cos(radians(60)))
# print(sin(radians(60)))

# a = int(input("a = "))
# b = int(input("b = "))
# print('Гипотенуза равна:', sqrt((a ** 2) + (b ** 2)))

import time

# seconds = time.time()
# print(seconds)
# localtime = time.ctime()
# print(localtime)
# res  =time.localtime(seconds)
# print(res)
# print(res.tm_hour)
# print(time.strftime("Today is %B %d, %Y", time.localtime(13252353477)))
# print(time.strftime("%m/%d/%Y, %H:%M:%S", time.localtime()))

# pause = 5
# print("Programm startted....")
# time.sleep(pause)
# print(pause, "seconds")

text = input("Название напоминания")
t = float(input("Введите время"))
t *= 60
time.sleep(t)
print(text)