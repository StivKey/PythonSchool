# slov = int(input("Введите число ворон"))
# if slov == 0:
#     print("На ветке: ",slov, "Ворон" )
# elif slov == 1:
#     print("На ветке: ", slov, "Ворона")
# elif slov == 2:
#     print("На ветке: ", slov, "Вороны")
# elif slov == 3:
#     print("На ветке: ", slov, "Вороны")
# elif slov == 4:
#     print("На ветке: ", slov, "Вороны")
# elif slov == 5:
#     print("На ветке: ", slov, "Ворон")
# elif slov == 6:
#     print("На ветке: ", slov, "Ворон")
# elif slov == 7:
#     print("На ветке: ", slov, "Ворон")
# elif slov == 8:
#     print("На ветке: ", slov, "Ворон")
# elif slov == 9:
#     print("На ветке: ", slov, "Ворон")
# else:print("Ошибка вводда")
#
# sl = int(input("Введите число ворон"))
# if 0 <= sl <= 9:
#  if sl == 1:
#     print("Одна ворона")
#  elif 2 <= sl <= 4:
#      print("На ветке: ", sl, "Вороны")
#  elif 5 <= sl <= 9 or sl == 0:
#      print("На ветке: ", sl, "Ворон")
# else:
#     print("Ошибка вводда")

# a = int(input("Введите число от 1до 99 ->"))
# kop = a
# if 11 <= kop <= 14:
#     print(a, "Копеек")
# else:
#     kop = kop % 10
#     if kop == 1:
#         print(a, "Копейка")
#     elif 2 <= kop <= 4:
#         print(a, "Копейки")
#     else:
#         print(a, "Копеек")

# true if (Условие) else False - тернарное выражение

# a,b = 10,20
# minim = a if a < b else b
# print(minim)

# a,b = 20,20
# print("a == b" if a == b else ("a > b" if a > b else "a > b"))

# a, b = 10, 20
# print("делить нельзя" if a == 0 else (b/a))

# ------------ФИКСИМ ОШИБКИ-------------
# try:
#     n = int(input("Введи что то"))
#     print(n * 98)
# except ValueError:
#     print("Шата пашла не так")
# else:
#     print("Все огонь")
# finally:
#     print("Я вывожусь всегда в конце")

# a = input("введите число 1 -> ")
# b = input("введите число 2 -> ")
# try:
#     print(int(a) + int(b))
# except ValueError:
#     print(str(a) + str(b))
# else:
#     print("Все введено верно")
# -------------МОЙ ВАРИАНТ----------------
# i = 2
# while i < 22:
#     print("i =", i)
#     i += 2

# i = 0
# while i<20:
#     i+=1
#     if(i%2==0):
#         print(i)

# a = int(input("введи кол-во * ->"))
# i = 0
# while i <= a:
#     print("*", end="")
#     i += 1

# a = int(input('Введите ваше начало диапазона '))
# b = int(input('Введите ваш конец диапазона '))
# s = 0
# while a <= b:
#     if a % 2 != 0:
#        s += a
#     a += 1
# print(s)


