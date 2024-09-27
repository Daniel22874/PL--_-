summ = lambda x, y, z: (x + y + z)
print(summ(int(input('1 число: ')), int(input('2 число: ')), int(input('3 число: ')))) # 1 тренировался


def s(a, b):
    return 1/2 * a * b


print(s(int(input('1 катет: ')), int(input('2 катет: ')))) # 2 основное задание


def less(a, b, c):
    li = []
    li.append(a)
    li.append(b)
    li.append(c)
    return min(li)


print(less(int(input('1 число: ')), int(input('2 число: ')), int(input('3 число: ')))) # 5 тренировался