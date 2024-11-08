n = int(input())   # VAR 2
matr = []
res = []
resf = 0
f = 0
for i in range(n):
    s = input().split()
    s = [int(x) for x in s]
    matr.append(s)
for k in range(len(matr) - 1):
    if sum(matr[k]) == sum(matr[k + 1]):
        f = 1
    else:
        f = 0
if f == 1:
    for i in range(len(matr)):
        st = []
        for j in range(len(matr[i])):
            st.append(matr[j][i])
        res.append(st)
    for i in range(len(res) - 1):
        if sum(res[i]) == sum(res[i + 1]):
            resf = 1
        else:
            resf = 0
    if resf == 1:
        print('Квадрат магический')
    else:
        print('Квадрат не магический')
else:
    print('Квадрат не магический')   # 1


n = int(input())
matr = []
res = []
for i in range(n):
    s = input().split()
    s = [int(x) for x in s]
    matr.append(s)
for el in matr:
    n = el[0]
    el[0] = el[-1]
    el[-1] = n
    res.append(el)
for el in res:
    print(el)   # 2