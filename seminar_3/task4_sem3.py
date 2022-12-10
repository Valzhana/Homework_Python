#Task4

number = int(input('Enter the number: '))
lst = []
while number > 0:
    digit = number % 2
    number //= 2
    lst.insert(0, digit)
print(*lst)


