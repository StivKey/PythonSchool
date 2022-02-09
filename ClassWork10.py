# Функции
# def- функция hello - имя функции(место для ...):


# def hello(name, word):  # функция принимает аргументы
#     print("Hello,", name, ". say ", word, sep="")
#
#
# hello("Iros", "HI")  # и получает параметры
# hello("Ivan", "OMG")


# def get_sum(a, b):
#     print(a + b)
#
#
# x = 3
# y = 5
# get_sum(x, y)
# n = 3
# v = 22
# get_sum(n, v)
# get_sum("yuung", "voor")
# get_sum(2.5, 4.8)


# def symbol(x, y, z):
#     s = ''
#     for i in range(x):
#         if i % 2 == 0:
#             s += y
#         else:
#             s += z
#     print(s)

#
# symbol(9, "+", "-")
# symbol(7, "X", "0")

# def get_sum(a, b):
#     return a + b # Все что после ретерна т.е возврата не работает
#
#
# n = 2
# m = 5
# res = get_sum(n, m)
#
# print(res)


# def maximum(one, two):
#     if one > two:
#         return one
#     elif two > one:
#         return two
#     else:
#         return
#
#
# m = maximum(9, 11)
# print(m)

# def primer(num1, num2):
#     if num1 > num2:
#        return num1 - num2
#     elif num2 > num1:
#         return num2 + num1
#     else:
#         return
#
#
# num1 = int(input("num1 = "))
# num2 = int(input("num2 = "))
# m = primer(num1, num2)
# print(m)

# def cube(a):
#     return a * a * a
#
#
# for i in range(1,11):
#     print(i,"в кубе = ",cube(i))

# Ряд Фибоначчи

# 1 1 2 3 5 8

# def fib(n):
#     a, b = 0, 1
#     while a < n:
#         print(a, end=" ")
#         # a, b = b, a + b
#         c = a + b
#         a = b
#         b = c
#
# fib(15)


# def change(lst):
#     return lst[::-1]
#
#
# print(change([1, 2, 3]))
# print(change([9, 12, 33, 54, 105]))
# print(change(['c', 'l', 'o', 'n']))
