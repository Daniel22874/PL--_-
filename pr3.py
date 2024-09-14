a = int(input('1 число: '))
b = int(input('2 число: '))
c = int(input('3 число: '))
if a < b and a < c:
    print(a)
elif b < a and b < c:
    print(b)
elif c < a and c < b:
    print(c)
elif a < b and a == c:
    print(a)
elif b < a and b == c:
    print(b)
elif c < a and c == b:
    print(c)
elif a == b and a < c:
    print(a)
elif b == a and b < c:
    print(b)
elif c == a and c < b:
    print(c)
elif a == b and b == c:
    print(a)
