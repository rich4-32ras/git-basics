import math

array = []

for a in range(1, 30):
    if a % 2 == 0:
        array.append(a)

print('чётные числа из последовательности (1, 30) -', list(array))