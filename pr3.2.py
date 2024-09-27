summ = lambda x, y, z: (x + y + z)
print(summ(int(input()), int(input()), int(input()))) # 1


def s(a, b):
    return 1/2 * a * b


print(s(int(input()), int(input()))) # 2


def less(a, b, c):
    li = []
    li.append(a)
    li.append(b)
    li.append(c)
    return min(li)


print(less(int(input()), int(input()), int(input()))) # 5