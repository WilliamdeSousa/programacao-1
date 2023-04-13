f = int(input())
i = 1
while i < f:
    sdiv = 0
    j = 1
    while j <= i:
        if i % j == 0:
            sdiv += j
        j += 1
    if sdiv == (2 * i):
        print(i)
    i += 1