#Task3

import random
lst = []
for i in range(5):
    lst.append(round(random.uniform(2, 10), 2))
print(lst)
new_lst = lst
for e in range(len(new_lst)):
    new_lst[e] %= 1
    new_lst.append(new_lst[e])
print(round(max(new_lst) - min(new_lst), 2))

