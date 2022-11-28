#Task4

number = int(input('Enter the number of a quarter from 1 to 4: '))
if number == 1:
    print('x > 0, y > 0')
elif number == 2:
    print('x < 0, y > 0')
elif number == 3:
    print('x < 0, y < 0')
elif number == 4:
    print('x > 0, y < 0')
else:
    print('You have entered an invalid value')
