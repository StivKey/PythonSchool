from random import *  # Импортируем все способы из метода рандом
from random import choice  # Выбираем метод из модуля
import random as r  # Обращаемся по букве за место random или иных модулей

# city_list = ['Москва', 'Новосибирск', 'Воронеж', 'Сочи', 'Екатеренбург']
# print(r.choice(city_list))
#
# s = [55, 66, 77, 88, 99]
# print(choice(s))
#
# s3 = [20, 30, 40, 50, 60, 70, 80]
# print(r.choices(s3, k=3))
#
# r.shuffle(s3)
# print(s3)

# print(r.uniform(10.4, 28.4))
# print(round(r.uniform(10.4, 28.4)))

# mas = [i for i in range(10)]
# print(mas)
#
# mas1 = [r.randint(0, 100) for i in range(10)] # РАндомно 10 чисел
# print(mas1)

# lst = [5,3,6,7,9,9]
# print(len(lst))
# print(min(lst)) # Минимальный элемент списка
# print(max(lst)) #Максимальный элемент списка
# print(sum(lst)) # Сумма чисел в списке

# slut = [r.randint(0, 100) for i in range(10)] # Вывести максимальное в 0 индекс т.е первым в списке
# print(slut)
# hg = max(slut)
# print("max: ", max(slut))
# slut.remove(hg)
# slut.insert(0, hg)
# print(slut)

# sl = [r.randint(-100, 100) for i in range(10)] # Вывести все минимальные числа в конец списка
# print(sl)
# sl.sort(reverse=True)
# print(sl)

# sl = [r.randint(0, 100) for i in range(10)]
# print(sl)
# lk = min(sl)
# print(lk)
# index = sl.index(lk)
# del sl[0:lk]
# print(sl)

# x = list('1a2b3c') # Проверяем наличие элемента в списке
# print(x)
# print('a' in x)
# print('5' in x)
# print('6' not in x) # Если его нет вернет True


# lst = []
# # if len(lst) == 0:
# #     print('Спсиок пустенький')
#
# if not lst:
#     print('Спсиок пустенький')
# else:
#     print('В списке куча элементов)')


# a = 5
# b = 4
# sl = [r.randint(0, 10) for i in range(a)]
# io = [r.randint(0, 10) for j in range(b)]
# print("Первый список", sl)
# print("Первый список", io)
# c = sl + io
# print("Третий список",c)
# c = []
# for i in range(len(sl)):
#     if sl[i] not in c:
#         c.append(sl[i])
# for i in range(len(io)):
#     if io[i] not in c:
#         c.append(io[i])
# print("Элементы без повторений ",c)
# c =[]
# for i in range(len(sl)):
#     if sl[i] in io and sl[i] not in c:
#         c.append(sl[i])
# print("Элементы общие для 2ух списков",c)


m = [
    [1, 2, 3, 4, 5, 6, 7],
    [6, 7, 32, 33, 2],
    [10, 22, 99, 77]
]
print(m)
print(m[1][2])
for row in range(len(m)):
    for col in range(len(m[row])):
        print(m[row][col], end="\t\t")
    print()
print()
for row in m:
    for col in row:
        print(col, end="\t")
    print()

print()
# for row in m:
#     for col in row:
#         print(col, end="\t")
#     print()
#
# print()
# for row in m:
#     for col in row:
#         print(col * col, end="\t")
#     print()