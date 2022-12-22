# Task5
import itertools

with open('equation_1.txt', 'r') as f:
    pol = f.read().split()[:-2]
for i in pol:
    if i == '+':
        pol.remove(i)

with open('equation_2.txt', 'r') as f:
    pol1 = f.read().split()[:-2]
for j in pol1:
    if j == '+':
        pol1.remove(j)
lst = []
for i in pol:
    result = int(*(str(i).split('*')[:1]))
    lst.append(result)
lst_1 = []
for j in pol1:
    result_1 = int(*(str(j).split('*')[:1]))
    lst_1.append(result_1)

sum_coe = list(map(sum, zip(lst, lst_1)))
a = list('*'.join(str(pol1).split()).split('*')[1:-1])

lst_2 = []
for y in range(len(a)):
    if y % 2 == 0:
        lst_2.append('*' + a[y][:-2])

lst_3 = []
for v, w in itertools.zip_longest(sum_coe, lst_2, fillvalue=''):
    result = (str(v) + str(w))
    lst_3.append(result)

with open('equation_fin.txt', 'w') as file:
    print(' + '.join(lst_3), file=file, end=' = 0 ')





