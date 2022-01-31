import random as r

# -----------Задание №1-----------

# a = [int(input("Введите элемент списка: ")) for i in range(int(input("Введите длину списка: ")))]
# b = a # Можно было и не делать, делал для себя, что бы полностью проверить работу цикла.
# c = []
# for j in b:
#     if j >= 0:
#         c.append(j)
# print("Полный список: ", b)
# print("Список из положительных элементов: ", c)
# print("Наибольший элемент: ", max(b))


# -----------Задание №2-----------

# lst = [int(input("Введите элемент списка: ")) for i in range(int(input("Введите длину списка: ")))]
# ind = int(input("Введите индекс: "))
# num = int(input("Введите Значение: "))
# # print(lst)
# lst.insert(ind, num)
# print(lst)

# -----------Задание №3-----------

# slut = [r.randint(-10, 100) for i in range(10)]
# print(slut)
# slut.sort()
# slut.reverse()
# print(slut)

# -----------Задание №4-----------

lst = [int(input("Введите элемент списка: ")) for i in range(int(input("Введите длину списка: ")))]
lst_copy = lst
ch = int(input("Введите Число: "))
for i in lst_copy:
    if i == ch:
        print("Число есть в списке!")
