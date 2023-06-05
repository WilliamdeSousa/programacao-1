l = []
for i in range(10):
    n = int(input())
    if i == 0:
        l.append(n)
    else:
        tam = 0
        for j in l:
            tam += 1
        
        for j in range(tam):
            if n <= l[j]:
                l.insert(j, n)
                break
        tam = 0
        for j in l:
            tam += 1
        if tam == i:
            l.append(n)
print(l)