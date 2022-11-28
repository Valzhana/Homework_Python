#Task5

x1 = float(input('Enter x1 coordinate: '))
y1 = float(input('Enter y1 coordinate: '))
x2 = float(input('Enter x2 coordinate: '))
y2 = float(input('Enter y2 coordinate: '))
distance = round(((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5, 2)
print(f' The distance between two points is: {distance}')
