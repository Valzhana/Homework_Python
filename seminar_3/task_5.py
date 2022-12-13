# Task5
n = int(input())


def fib():
    lst = [0, 1]
    for i in range(2, n + 1):
        lst.append(lst[i - 2] + lst[i - 1])
    lst1 = [0, 1]
    for e in range(2, n + 1):
        lst1.append(lst1[e - 2] - lst1[e - 1])
    lst1.reverse()
    lst1.pop()
    print(lst1 + lst)



