# for i in range(3):
#     print("+++")
#     for j in range(2):
#         print("---------")


# w = int(input("widht: "))
# h = int(input("height: "))
# for i in range(h):
#     for j in range(w):
#         print("*", end="")
#     print()

# w = int(input("widht: "))
# h = int(input("height: "))
# for i in range(h):
#     for j in range(w):
#         if i == 0 or j == 0 or i == (h - 1) or j == (w - 1):
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()
#
# for i in range(10):
#     if i % 2 == 0:
#         print(i, end=" ")
# print()
#
# print([i for i in range(10) if i % 2 == 0]) #В одну строку
#
# print([letter * 2 for letter in "BANANA"])

# nums = [8, 3, 9, 7, 3]
# print(nums)
# print(type(nums))
#
# print(type([2.3.2, "there", True]))

# nums = [8, 3, 9, 7, 3]
# print(nums[0])
# print(nums[1])
# print(nums[3])
# print(nums[-1])
# nums[-1] = 123
# print(nums)
# nums[3] += 100
# print(nums)
# print("Длина списка ", len(nums))

# a = [1, 2]
# print((id(a)))
# a[1] = 3
# print(a)
# print((id(a)))

# s = list("Hello")
# print(s)

# n = [5, 1] * 7
# print(n)

# n = list(range(10, 2, -2))
# print(n)


# n = 5
# a = [i ** 2 for i in range(1, n+1)]
# print(a)

# a = [1, 2, 3]
# b = [4, 5]
# a += b
# c = a + b
# print(c)

# a = [0] * int(input("Введите кол-во  эл. списка: "))
# print(a)
# for i in range(len(a)):
#     a[i] = int(input("=>"))
#     print(a)

# a = [int(input("->")) for i in range(int(input()))] #
# print(a)
# for i in range(len(a)):
#     print(a[i], end=" ")

# a = [int(input("->")) for i in range(int(input("Ведите число: ")))]
# b = 0
# for i in range(len(a)):
#     if a[i] < 0:
#         b += a[i]
# print(b)

# a = list(range(10))
# print(a)
# for i in range(len(a)):
#     print(i, end=" ")
# print()
# for i in a:
#     print(i,end=" ")

# a = [21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]
# b = 0
# s = 0
# for i in range(len(a)):
#     if a[i] % 2 == 0:
#         b += 1
#     else:
#         s += a[i]
# print("Четных чисел: ", b)
# print("Сумма: ", s)

# a = [int(input("->")) for i in range(int(input("Ведите число: ")))]
# s = k = 0
# for i in range(len(a)):
#     if a[i] != 0:
#         s += a[i]
#         k += 1
#
# print(s /k)
# print(k)
# print(s)

# Список [start:stop:step]

# s = [4, 6, 0, 2, 4, 77, 8, 11]
# print(s[1:7:2])

# a = [1, 2, 3, 4, 5, 6, 7]
# print(a[0:7])
# print(a[::-1])
# print(a[0:7:2])
# print(a[1:7:2])
# print(a[0:1])
# print(a[6:7])
# print(a[4:7])
# print(a[4:1:-1])
# print(a[2:5])
