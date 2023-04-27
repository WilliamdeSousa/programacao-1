n = int(input())
while n != -1:
    i = 1
    nd = 0
    while i <= n:
        if n % i == 0:
            nd += 1
        i += 1
    if nd == 2:
        print(1)
    else:
        print(0)
    n = int(input())