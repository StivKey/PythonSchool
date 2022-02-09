import random as r

# -----------Задание №1-----------

# w, h = 6, 6
# lst = []
# k = 0
# slut = [[r.randint(0, 100) for x in range(w)] for y in range(h)]
# print('Массив из случайных чисел от 1 до 100: ')
# for row in slut: # Строки
#     # print(row[k])
#     lst.append(row[k])
#     k += 1
#     for col in row: # Столбцы
#         if col >= 0:
#             print(col, end="\t\t") # выводим числа по 1 му и табулируем
#     print()
# # print(lst)
# a = min(lst)
# print('Минимальный элемент массива: ',a)


# -----------Задание №2-----------

w, h = 6, 6
spis = [0, 8, 10, 0, 10, 7]
slut = [[r.randint(0, 10) for x in range(w)] for y in range(h)]
print(slut)
for row in slut:  # Строки
    for col in row:  # Столбцы
        if col >= 0:
            print(col, end="\t\t")
    print()
print()
for i in range(len(slut)):
    if i % 2 != 0:
        for z in range(len(slut[i])):
            print(slut[i][z], end="\t\t")
        # print()
    elif i % 2 == 0:
        for g in spis:
            if g >= 0:
                print(g, end="\t\t")
    print()
