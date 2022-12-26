# Task3.1

data = input("Enter your data: ")


def compression(data):
    count = 1
    result = ''
    for i in range(len(data) - 1):
        if data[i] == data[i + 1]:
            count += 1
        else:
            result += str(count) + data[i]
            count = 1
    if count > 1 or (data[len(data) - 2] != data[-1]):
        result += str(count) + data[-1]
    print(result)


compression(data)




