import random as r

# -----------Задание №1-----------

# slut = [r.randint(0, 101) for i in range(20)]
# print(slut)
# print("Summa: ", sum(slut))

# -----------Задание №2-----------

# lst = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
#
# row = 0
# for row in lst: # Бежим по списку
#     for col in row: # Выводим значени по порядку отсекая табуляцией
#         print(col, end="\t")
#     print()
# print()
# a = 0
# for col in row:
#     for row in lst: # Бежим по индексам выводит я 0 0 0 затем 1 1 1, 2 2 2 и т.д
#         print(row[a], end="\t")
#     a += 1
#     print()

# -----------Задание №3(ДОП)-----------

slut = [r.randint(0, 10) for i in range(10)]
new_slut = list() # Новый список для записи

while len(new_slut) != 10: # Генирируем пока не равно 10
    n = r.randint(0, 9) # Генерируем случайное целое число
    if n not in new_slut: # Сравниваем полученное выше число с НЕ наличием его в списке
        new_slut.extend([n]) # Добавляем элементы в конец списка list
print(new_slut)
