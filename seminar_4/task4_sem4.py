# Task4

import random

k = int(input('Enter k, k != 0: '))
coef = [random.randint(0, 100) for i in range(0, k + 1)]
poly = ' + '.join([f'{(j, "")[j == 1]}*x^{i}' for i, j in enumerate(coef) if j][::-1])
poly = poly.replace('x^1 + ', 'x + ')
poly = poly.replace('x^0', '')
poly = poly[:-1]
with open('polynom.txt', 'w') as f:
    f.write(poly.__add__(' = 0'))
