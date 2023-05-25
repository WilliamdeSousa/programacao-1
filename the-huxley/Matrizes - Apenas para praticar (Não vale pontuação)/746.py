linhas_a, colunas_a_linhas_b, colunas_b = [int(i) for i in input().split()]
colunas_a = linhas_b = colunas_a_linhas_b
a = []
b = []
for i in range(linhas_a):
    a.append([int(j) for j in input().split()])
for i in range(linhas_b):
    b.append([int(j) for j in input().split()])
c = []
for i in range(linhas_a):
    linha_c = []
    for j in range(colunas_b):
        soma = 0
        for k in range(colunas_a_linhas_b):
            soma += (a[i][k] * b[k][j])  
        linha_c.append(soma)
    c.append(linha_c)
for linha in c:
    print(' '.join([str(e) for e in linha]))