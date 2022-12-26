# Task3.2

data1 = input("Enter your data: ")


def recovery(data1):
    number = ''
    res = ''
    for i in range(len(data1)):
        if not data1[i].isalpha():
            number += data1[i]
        else:
            res = res + data1[i] * int(number)
            number = ''
    print(res)


recovery(data1)
