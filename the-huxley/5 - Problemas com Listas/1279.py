tamanho = range(int(input()))
if tamanho.stop == 0:
    print('Vazia')
else:
    matriz = list()
    for i in tamanho:
        linha = list()
        for j in tamanho:
            linha.append(int(input()))
        matriz.append(linha)
    for i in tamanho:
        for j in tamanho:
            matriz[i][j] += int(input())
    for i in tamanho:
        for j in tamanho:
            print(matriz[i][j])