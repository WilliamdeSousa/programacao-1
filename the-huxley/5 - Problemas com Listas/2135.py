n1 = int(input())
if n1 <= 0:
    print('Erro - A lista deve ter pelo menos 1 elemento.')
else:
    lista1 = []
    for i in range(n1):
        lista1.append(int(input()))
    n2 = int(input())
    if n2 <= 0:
        print('Erro - A lista deve ter pelo menos 1 elemento.')
    else:
        lista2 = []
        for i in range(n2):
            lista2.append(int(input()))
        lista3 = lista1.copy()
        lista3.extend(lista2)
        print(' '.join([str(i) for i in lista3]))