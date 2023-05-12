i = 0
q = 0
s = 0
while i < 7:
    n = int(input())
    if n >= 100:
        q += 1
    s += n
    i += 1
print(q)
print(s//7)