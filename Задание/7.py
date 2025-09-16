import math
def calculate_circle_area(radius):
    return math.pi * radius ** 2
def is_positive(number):
    return number > 0
radius = int(input("Ведите радиус: "))
print(f"Площадь круга с радиусом {radius}: {calculate_circle_area(radius):.2f}")

num = int(input("Ведите число: "))
print(f"Число {num} положительное? {is_positive(num)}")