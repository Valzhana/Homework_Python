# Task2
number = int(input('Enter the number: '))
factor = 2
lst = []
while number > 1:
    if number % factor == 0:
        lst.append(factor)
        number //= factor
    else:
        factor += 1
print(*lst)
