# -----------Задание №1-----------
a = 0
i = 0
for i in range(5):
    print(" ")
    for a in range(8):
        print("+", end="")
        print("-", end="")

# -----------Задание №2-----------

nums1 = int(input("Введите Начало диапазона: -> "))
nums2 = int(input("Введите Конец диапазона: -> "))
b = nums1
while nums2 > b:
    b += 1
    if b % 2 != 0:
        print(b, " ", end="")


# -----------Задание №2-----------
import random

sicret = random.randint(1, 100)
print(sicret)
nums3 = 0
while 0 != sicret:
    nums4 = int(input("Введите число от 1 до 100: -> "))
    nums3 += 1
    if nums4 > sicret:
            print("Загаданное число меньше")
    elif nums4 < sicret:
            print("Загаданное число больше")
    elif nums4 == sicret:
        break
if nums4 == sicret:
    print("Вы угадали заданное число с", nums3, "попытки поздравляем!")
