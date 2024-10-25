m = input().split(' ')   # VAR 2  основной
m = [int(x) for x in m]
mi = min(m)
print(m.index(mi))   # 1


m = input().split()
p = []
o = []
m = [int(x) for x in m]
for el in m:
    if el >= 0:
        p.append(el)
    if el < 0:
        o.append(el)
print(p)
print(o)    # 2


m = input().split()   # VAR 1
m = [int(x) for x in m]
ma = max(m)
print(ma)
print(m[::-1])   # 1


m = input().split()
mch = [int(x) for x in m]
sa = sum(mch) / len(mch)
sa = str(sa)
while '0' in m:
    m[m.index('0')] = sa
print(m)   # 2


D = input().split()   # VAR 3
D = [int(x) for x in D]
n = len(D)
D1 = D[1::2]
su = sum(D1)
print(D, su)   # 1


m = input().split()
mch = [int(x) for x in m]
for el in mch:
    if el < 15:
        mch[mch.index(el)] = el * 2
print(mch)    # 2


m = input().split()    # VAR 4
m = [int(x) for x in m]
ma = max(m)
print(m.index(ma) + 1)   # 1


m = input().split()
m = [int(x) for x in m]
n = []
for el in m:
    if el % 2 == 1:
        n.append(el)
if len(n) > 0:
    print(n[::-1])
else:
    print('Нечётных чисел нет')   # 2


m = input().split()   # VAR 5
m = [int(x) for x in m]
for i in range(len(m) - 1):
    if m[i] < 0 and m[i + 1] < 0:
        print(m[i], m[i + 1])   # 1


m = input().split()
m = [int(x) for x in m]
n = []
for el in m:
    if el not in n:
        n.append(el)
print(n)   # 2


m = input().split()   # VAR 6
m = [int(x) for x in m]
sa = sum(m) / len(m)
ma = max(m)
c = 0
for el in m:
    if el < ma and el > sa:
        print(el)
        c += 1
print(c)   # 1


m = input().split()
m = [int(x) for x in m]
m5 = [el for el in m if el > 5]
print(sum(m5))   # 2


m = input().split()   # VAR 7
m = [int(x) for x in m]
li1 = []
li2 = []
for el in m[::2]:
    li2.append(el)
for el in m[1::2]:
    li1.append(el)
print(sum(li1))
p = 1
for el in li2:
    p *= el
print(p)   # 1


m = input().split()
m1 = [int(x) for x in m]
m2 = [int(x) for x in m]
print(m1)
m1[m1.index(min(m1))] = max(m1)
m1[m2.index(max(m2))] = min(m2)
print(m1)   # 2