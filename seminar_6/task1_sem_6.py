# Task1_sem_3

# numbers = input('Enter numbers separated by the spacebar: ').split()
# lst = [int(e) for e in numbers]
# print(lst)
# sum = 0
# for i in range(len(lst)):
#     if i % 2 != 0:
#         sum += lst[i]
# print(sum)


lst = [int(e) for e in input('Enter numbers separated by the spacebar: ').split()]
print(lst)
print(sum([v for i, v in enumerate(lst, start=1) if i % 2 == 0]))
