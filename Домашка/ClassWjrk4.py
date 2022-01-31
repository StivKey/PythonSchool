# i = 0
# while i < 10:
#     if i == 3:
#         i += 1
#         continue # пропускает все условия цикла после себя
#     print(i, end " ")
#     if i == 5:
#         break
#
# while True:
#     n = int(input("Введите положительное число: "))
#     if not n > 0:
#         break
#
# n = 1
# while n != 0:
#     ng = int(input("Введите число: "))
#
#     print(n)
#     if n == 0:
#         break
#     n *= ng
# #
# i = 0
# while i < 10:
#     print(i)
#     i +=1
# else:    # Редкий случай использования ELSE после WHILE
#     print("Цикл ограничен, i =", i)
# print("За передлами цикла")
#
# i = 1
# while i < 5:
#     print("Внешний цикл: i=", i)
#     j = 1
#     while j < 4:
#         print("Внутренний цикл: j=", j)
#         j += 1
#     i += 1
#
#
# МОЙ ВАРИАНТ ТАБЛИЦЫ
#
#
# num1 = 1
# while num1 < 10:
#     # print(num1)
#     num2 = 1
#     while num2 < 10:
#         # print(num2)
#         print(num1, "*", num2, "= HZ")
#         num2 += 1
#     num1 += 1
#
# Рабочий варик
#
# i = 1
# while i < 10:
#     j = 1
#     while j < 10:
#         print(i, "*", j , "=", i * j, end="\t\t")
#         j += 1
#     print()
#     i += 1

# i = 0
# while i < 5:
#     j = 0
#     while j < 16:
#         if i % 2 == 0:
#             print("+", end="")
#         else:
#             print("-", end="")
#         j += 1
#     print()
#     i += 1
#
# i = 0
# while i < 5:
#     print(" " * i, "*")
#     i += 1
#
# i = 0
# c = " "
# d = '%'
# while i < 1:
#     j = 0
#     while j < 5:
#         print(c * j, d)
#         j += 1
#     i += 1
#
# Решение учителя
# i = 0
# while i < 5:
#     j = 0
#     while j < i:
#         print(" ", end="")
#         j += 1
#     print("*")
#     i += 1
#
# for i in "Hello":
#     print(i)
#
# i = 1
# for color in 'red', 'green', 'blue':
#     print(i, "color:", color)
#     i += 1
#
# for i in range(2, 9, 3):
#     print(i, end=" ")
# print()
# for i in range(9, 0, -1):
#     print(i, end=" ")
#
#
# a = int(input("Введите целое число"))
# for i in range(1, a):
#     if a % i == 0:
#         print(i, end=" ")
#
#
# a = int(input("Введите  число"))
# b = int(input("Введите  число"))
# for i in range(a, b):
#     if i % 10 == i // 10:
#         print(i, end=" ")
#
# for i in range(3):
#     print(i)
#     if i == 1:
#         break
# else:
#     print("done")