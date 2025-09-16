l = []
for i in range(int(input())):
    l.append(int(input()))

print(f"Kоличество элементов в списке {len(l)}")
print(f"последний элемент списка {l[-1]}")
print(f"cписок в обратном порядке {list(reversed(l))}")
if 5 in l and 17 in l:
    print("Да")
else:
    print("Нет")