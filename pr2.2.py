from math import *

x = eval(input('Введите x: '))
y = eval(input('Введите y: '))
z = eval(input('Введите z: '))
s = ((9 + ((x - y) ** 2)) ** (1 / 3)) / (x ** 2 + y ** 2 + 2) - (e ** (abs(x - y)) * (tan(z) ** 3))
print(s)