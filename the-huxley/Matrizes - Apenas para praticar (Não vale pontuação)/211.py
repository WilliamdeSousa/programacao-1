n = int(input())
regioes = []
for i in range(2):
    regiao = []
    for j in range(n):
        linha = []
        for k in input().split():
            linha.append(int(k))
        regiao.append(linha)
    regioes.append(regiao)
for i in range(n):
    print(' '.join([str(regioes[0][i][j] + regioes[1][i][j]) for j in range(n)]), end=' \n')