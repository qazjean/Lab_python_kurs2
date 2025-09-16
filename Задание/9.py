import random

l = [random.randint(-10, 10) for _ in range(15)]
positive_l = [x for x in l if x > 0]
squared_l = [x**2 for x in l]

print("Исходный список:", l)
print("Положительные числа:", positive_l)
print("Квадраты чисел:", squared_l)