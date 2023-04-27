l = []
for i in range(10):
    n = int(input())
    if i == 0:
        l.append(n)
    else:
        for j in range(len(l)):
            if n < l[j]:
                l.insert(j, n)
                break
        if len(l) < i + 1:
            l.append(n)
print(l)