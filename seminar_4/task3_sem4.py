# Task3

lst = input('Enter numbers separated by the spacebar: ').split()
new_lst = [int(i) for i in lst]
print(new_lst)
result = []
for n in range(len(new_lst)):
    for j in range(len(new_lst)):
        if n != j and new_lst[n] == new_lst[j]:
            break
    else:
        result.append(new_lst[n])
print(result)
