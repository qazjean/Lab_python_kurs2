start = int(input())
end = int(input())
z = []
if start <= end:
    nstart = start if start % 2 == 0 else start+1
    for i in range(nstart, end +1,2):
        z.append(i)
    if z:
        print(z)
    else:
        print("В этом диапазоне нет чётных чисел")
else:
    print("Старт должен быть меньше финиша")
