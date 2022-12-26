# Task1.2

import random
count = random.randint(0, 1)
human = 0
bot = 0
balance = 2021
while balance > 0:
    if count == 1:
        human = int(input('Human is taking candy: '))
        if human > 28:
            print("You can't take more than 28 candies at a time.Try again! ")
            continue
        elif human < 0:
            print("You've entered an invalid value. Try again!")
            continue
        else:
            balance -= human
            print(f'balance: {balance}')
            if balance < 0:
                print(f'You can take no more than {balance + human} candy')
                human = int(input('Human is taking candy: '))
            count -= 1
    elif count == 0:
        bot = random.randint(0, 28)
        print(f'Bot is taking candy: {bot}')
        balance -= bot
        print(f'balance: {balance}')
        count += 1
if count == 0:
    print('Human is the winner! ')
else:
    print('Bot is the winner!')
