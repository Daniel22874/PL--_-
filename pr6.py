t = input().split()
c = 0
for sl in t:
    if sl[0] == 'е' or sl[0] == 'Е':
        c += 1
print(c)   # 1


s = input()
c = s.count(':')
s = s.replace(':', '%')
print(s)
print(c)   # 2


s = input()
c = s.count('.')
s = s.replace('.', '')
print(s)
print(c)   # 3


s = input()
c = s.lower().count('а')
s = s.replace('а', 'о')
s = s.replace('А', 'О')
symb = 0
for el in s:
    if el != ' ':
        symb += 1
print(s)
print(c)
print(symb)   # 4


s = input()
s = s.lower()
print(s)   # 5


s = input().lower()
c = s.count('а')
s = s.replace('а', '')
print(s)
print(c)   # 6


s = input()
n = len(s)
p = n // 2
s1 = s[:p]
s2 = s[p:]
s1 = s1.replace('п', '*').replace('П', '*')
print(s1 + s2)   # 7


s = input().split()
print(len(s))   # 8


text = input().lower()
text = text.replace('.', '')
text = text.split()
sl = input().lower()
print(text.count(sl))   # 9


s = input().split()
s = [el.capitalize() for el in s]
print(' '.join(s))   # 10


s = input().split()
li = [el for el in s if el[-1] == 'я' or el[-1] == 'Я']
for el in li:
    print(el)   # 12


s = input()
sk1 = s.index('(')
sk2 = s.index(')')
print(s[sk1:sk2 + 1])   # 13


s = input().split()
li1 = [el for el in s if el[-1] == 'я' or el[-1] == 'Я']
li2 = [el for el in s if el[0] == 'а' or el[0] == 'А']
for el in li1:
    print(el)
for el in li2:
    print(el)    # 14


s = input().lower()
print(s.count('т'))   # 15
