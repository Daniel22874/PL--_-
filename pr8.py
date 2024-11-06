def s6(a):   # VAR 2 основной
    return 3 * (3 ** 0.5) * a ** 2 / 2


a = int(input())
print(s6(a))   # 1


def spr(a, b):
    return a * b


c = 1
for i in range(3):
    a = int(input('1 сторона: '))
    b = int(input('2 сторона: '))
    print(f"Площадь {c} прямоугольника: {spr(a, b)}")
    c += 1   # 2



def s6(a):   # VAR 1
    return 3 * (3 ** 0.5) * a ** 2 / 2

def spr(a, b):
    return a * b

def s3(a, h):
    return 0.5 * a * h


fi = input('Выберите фигуру, площадь которой требуется найти(правильный шестиугольник, прямоугольник, треугольник): ')
if fi == 'правильный шестиугольник':
    a = int(input('Введите длину стороны шестиугольника: '))
    print(f"Площадь шестиугольника: {s6(a)}")
if fi == 'прямоугольник':
    a = int(input('1 сторона: '))
    b = int(input('2 сторона: '))
    print(f"Площадь прямоугольника: {spr(a, b)}")
if fi == 'треугольник':
    a = int(input('сторона: '))
    h = int(input('высота: '))
    print(f"Площадь треугольника: {s3(a, h)}")   # 1


m1 = input().split()
m2 = input().split()
m3 = input().split()
m1 = [int(x) for x in m1]
m2 = [int(x) for x in m2]
m3 = [int(x) for x in m3]
print('1 массив', sum(m1), sum(m1) / len(m1))
print('2 массив', sum(m2), sum(m2) / len(m2))
print('3 массив', sum(m3), sum(m3) / len(m3))   # 2


def pifagor(k1, k2):  # VAR 3
    return (k1 ** 2 + k2 ** 2) ** 0.5


print('введите катеты 1 треугольника: ')
k1 = int(input('1 катет: '))
k2 = int(input('2 катет: '))
g1 = pifagor(k1, k2)
print('гипотенуза 1: ', g1)
print('введите катеты 2 треугольника: ')
k3 = int(input('1 катет: '))
k4 = int(input('2 катет: '))
g2 = pifagor(k3, k4)
print('гипотенуза 2: ', g2)
if g1 < g2:
    print('гипотенуза 1 меньше гипотенузы 2')
else:
    print('гипотенуза 2 меньше гипотенузы 1')  # 1


s = input()
li = []
for el in s:
    li.append(el)
li = sorted(li)
print(''.join(li))   # 2



def evklid(a, b):   # VAR 4
    while a % b != 0:
        r = a % b
        a = b
        b = r
        if a % b == 0:
            return b
            break


a = int(input())
b = int(input())
c = int(input())
d = int(input())
res1 = a * d
res2 = b * c
hod = evklid(res1, res2)
while hod > 1:
    res1 //= hod
    res2 //= hod
    hod = evklid(res1, res2)
if hod == 1:
    print(res1, '/', res2)   # 1