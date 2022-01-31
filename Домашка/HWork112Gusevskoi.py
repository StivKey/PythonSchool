#-----------Задание №1-----------

numa = int(input("введи кол-во символов -> "))
myb = input("введи тип символа -> ")
tc = int(input("введи ориентацию (0 - горизонт, 1 - верт) -> "))
i = 0
while i <= numa:
    if tc == 0:
        print(myb, end="")
        i += 1
    elif tc == 1:
        print(myb)
        i += 1

#-----------Задание №2-----------

numb = int(input("введите кол-во чисел -> "))
istr = 1
sums = 0
mini = float(99999999999)
maxi = float(-9999999999)
while istr <= numb:
    istr += 1
    numn = float(input("введите число -> "))
    sums = sums + numn
    # srArifm = sums / numb
    if numn < mini:
        # print("Что то минимал")
        mini = numn
    elif numn > maxi:
        # print("Что то макимал")
        maxi = numn
srArifm = sums / numb
print("Кол-во чисел: ", numb)
print("Сумма чисел: ", sums)
print("Среднее арифметическое: ", srArifm)
print("Минимальное Число: ", mini)
print("Максимальное Число: ", maxi)

#-----------Задание №3-----------

inp = int(input("Введите число: "))
num1 = 0
num2 = 0
rel = inp
while inp > 0:
    num1 = inp % 10
    num2 = num2 * 10 + num1
    inp = inp // 10
if num2 == rel:
    print("Число " + str(rel) + " - Палиндром")
else:
    print("Число " + str(rel) + " Не - палиндром")
