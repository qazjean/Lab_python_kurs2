print("Введите 3 числа")
a, s, d = int(input()), int(input()), int(input())
print("Минимальное число: ", end = "")
if a <= s and a <= d:
    print(a)
elif s <= d:
    print(s)
else:
    print(d)