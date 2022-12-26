# Task1.1

import random
count = random.randint(0, 1)
groot = 0
hulk = 0
balance = 2021
while balance > 0:
    if count == 1:
        groot = int(input('Groot is taking candy: '))
        if groot > 28:
            print("You can't take more than 28 candies at a time.Try again! ")
            continue
        elif groot < 0:
            print("You've entered an invalid value. Try again!")
            continue
        else:
            balance -= groot
            print(f'balance: {balance}')
            if balance < 0:
                print(f'You can take no more than {balance + groot} candy')
                groot = int(input('Groot is taking candy: '))
            count -= 1
    elif count == 0:
        hulk = int(input('Hulk is taking candy: '))
        if hulk > 28:
            print("You can't take more than 28 candies at a time.Try again!")
            continue
        elif hulk < 0:
            print("You've entered an invalid value. Try again!")
            continue
        else:
            balance -= hulk
            print(f'balance: {balance}')
            if balance < 0:
                print(f'You can take no more than {balance + hulk} candy')
                hulk = int(input('Hulk is taking candy: '))
            count += 1
if count == 0:
    print('I Am Groot')
else:
    print('Hulk smash!')
