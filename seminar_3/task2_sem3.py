# Task2

lst = [2, 7, 5, 3, 7, -1]
print(lst, '\n')
new_lst = []
for i in range(len(lst) // 2):
    if len(lst) % 2 == 0:
        new_lst.append(lst[i] * lst[-i - 1])
for e in range(len(lst) // 2 + 1):
    if len(lst) % 2 != 0:
        new_lst.append(lst[e] * lst[-e - 1])
print(new_lst)
