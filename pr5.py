digit = int(input())
for i in range(2, digit + 1):
    if digit % i == 0:
        print(i)
        break     # 2 основное задание



n = int(input())
for i in range(1, n + 1):
    print(i ** 2)     # 1 всё ниже для тренировки



def square(n):
    p = 1
    for i in range(n):
        p *= 2
    return p


pokaz = []
step = []
n = int(input())
for i in range(1, n + 1):
    if square(i) <= n:
        step.append(square(i))
        pokaz.append(i)
print(f'Основание: 2, Показатель: {pokaz[-1]}, Степень: {step[-1]}') # 3



x = int(input())     # 1 день
y = int(input())     # найти номер дня, в который спортсмен пробежит у км
c = 0     # номер дня
while x < y:
    x += x * 10 / 100
    c += 1
if x >= y:
    print(c)   # 4



ch = int(input())
c = 0
while ch != 0:
    c += 1
    ch = int(input())
if ch == 0:
    print(c)    # 5



ch = int(input())
c = 0
s = 0
while ch != 0:
    c += 1
    s += ch
    ch = int(input())
if ch == 0:
    print(s / c)    # 6



a = int(input())
b = int(input())
c = 0
while a != 0 and b != 0:
    if b > a:
        c += 1
    a, b = b, int(input())
if a == 0 or b == 0:
    print(c)        # 7



a = int(input())
b = int(input())
c = 0
while a != 0 and b != 0:
    if b == a:
        c += 1
    a, b = b, int(input())
if a == 0 or b == 0:
    print(c)        # 8



