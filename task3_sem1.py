#Task_3

x = int(input('Enter X:'))
y = int(input('Enter Y:'))
if x > 0 and y > 0:
    print('quarter 1')
elif x > 0 and y < 0:
    print('quarter 4')
elif y > 0:
    print('quarter 2')
else:
    if y < 0:
        print('quarter 3')
