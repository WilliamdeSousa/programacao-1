n = int(input())
while n != 0:
    anterior = 0
    atual = 1
    print(anterior, end=' ') if n > 1 else print(0)
    for i in range(n - 1):
        print(atual, end=' ') if (i != (n - 2)) else print(atual)
        proximo = anterior + atual
        anterior = atual
        atual = proximo
    n = int(input())