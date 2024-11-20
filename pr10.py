# VAR 2
matr = []
fi = open('C:/Users/Daniel/Desktop/VS Code/PL-Rodionov/PL-Rodionov/Rodionov_Y242_vvod.txt', 'r+', encoding='utf-8').readlines()
fi = [el.replace('\n', '') for el in fi]
fi = [el.split() for el in fi]
for el in fi:
    el = [int(x) for x in el]
    matr.append(el)
res = []
resf = 0
f = 0
f2 = open('C:/Users/Daniel/Desktop/VS Code/PL-Rodionov/PL-Rodionov/Rodionov_Y242_vivod.txt', 'w', encoding='utf-8')
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
        f2.write('Квадрат магический')
    else:
        f2.write('Квадрат не магический')
else:
    f2.write('Квадрат не магический')   # 1



matr = []
fi = open('C:/Users/Daniel/Desktop/VS Code/PL-Rodionov/PL-Rodionov/Rodionov_Y242_vvod.txt', 'r+', encoding='utf-8').readlines()
fi = [el.replace('\n', '') for el in fi]
fi = [el.split() for el in fi]
for el in fi:
    matr.append(el)
res = []
for el in matr:
    n = el[0]
    el[0] = el[-1]
    el[-1] = n
    res.append(el)
f2 = open('C:/Users/Daniel/Desktop/VS Code/PL-Rodionov/PL-Rodionov/Rodionov_Y242_vivod.txt', 'w', encoding='utf-8')
for el in res:
    f2.write(f"{' '.join(el)}\n")   # 2