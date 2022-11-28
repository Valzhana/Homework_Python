#Task_1

number = int(input('Enter a number from 1 to 7 :'))
if number == 6 or number == 7:
    print('Day off')
elif 0 < number < 6:
    print('Not a day off')
else:
    print('You have entered an invalid value')
