# # Task_1_sem2
#
# num = input('Enter the number`: ')
# sum_digit = 0
# for e in str(num):
#     if e != '.':
#         sum_digit += int(e)
# print(sum_digit)

num = input('Enter the number: ')
print(sum(map(int, filter(str.isdigit, num))))
