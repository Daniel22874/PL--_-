from math import *

x = int(input('Введите x: '))
t = int(input('Введите t: '))
z = (9 * pi * t + 10 * cos(x)) / (sqrt(t) - abs(sin(t))) * (e ** x)
print(round(z, 2))
