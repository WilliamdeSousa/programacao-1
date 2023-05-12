n = int(input())
r = [int(input()) for i in range(n)]
inversoes = 0
for i in range(n):
    for j in range(n):
        if i < j and r[i] > r[j]:
            inversoes += 1
print(inversoes)