# -----------Задание №1-----------

a = [int(input("->")) for i in range(int(input("n: ")))]
b = a[::2]
print(b)

# -----------Задание №2-----------

a = [int(input("->")) for i in range(int(input("n: ")))]
b = a
for i in range(len(b)):
    if b[i] > b[i - 1]:
     print(b[i], end=" ")

# -----------Задание №3-----------

a = [1, 3, 5, 6, 2, 4, 6, 1, 2, 7]
for i in range(len(a)):
    for j in range(len(a)):
        if i != j and a[i] == a[j]:
            break
    else:
        print(a[i], end=" ")
