A = int(input('1 число: '))
B = int(input('2 число: '))
if A < B:
    for i in range(A, B + 1):
        print(i)
if A > B:
    for i in range(A, B - 1, -1):
        print(i)       # 2 основное задание



A = int(input('1 число: '))
B = int(input('2 число: '))
for i in range(A, B - 1, -1):
    if i % 2 == 1:
        print(i)    # 3 всё ниже для тренировки



N = int(input('Количество чисел: '))
su = 0
for i in range(N):
    a = int(input(f'{i + 1} число: '))
    su += a
print(su)             # 4



N = int(input())
su = 0
for i in range(1, N + 1):
    su += i ** 3
print(su)             # 5



N = int(input())
p = 1
for i in range(1, N + 1):
    p *= i
print(p)             # 6



n = int(input())
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end='')
    print()        # 8



N = int(input())
p = 1
su = 0
for i in range(1, N + 1):
    p *= i
    su += p
print(su)             # 7



A = int(input('1 число: '))
B = int(input('2 число: '))
for i in range(A, B + 1):
    print(i)          # 1



n = int(input())
f1 = f2 = 1
su = 2
for i in range(2, n):
    f1, f2 = f2, f1 + f2
    su += f2
print(su)    # 9