n = int(input())
while n != -1:
    produto =1
    i = 2
    while i <= n:
        produto *= i
        i += 1
    print(produto)
    n = int(input())