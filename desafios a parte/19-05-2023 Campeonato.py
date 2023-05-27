a = input()
b = input()
c = input()
d = input()
e = input()
f = input()
g = input()
h = input()
satisfeito = True
if (a not in [b, d, f, h]) or (b in [a, d]) or (g == h and not d ==  c) or (h not in [g, f]) or (c == e and not f == a) or (c != e and f == a):
    satisfeito = False
if satisfeito:
    print('Conseguimos times suficientes!')
else:
    print('Alguem nao esta satisfeito...')