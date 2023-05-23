# lendo a largura da matriz
l = int(input())

# recebendo a matriz LxL
matriz = []
entrada = [int(i) for i in input().split()]
if len(entrada) > l:
    for i in range(l):
        linha = [entrada[(i*l)+j] for j in range(l)]
        matriz.append(linha)
else:
    matriz.append(entrada)
    for i in range(l - 1):
        entrada = [int(i) for i in input().split()]
        matriz.append(entrada)

# testando somas
## horizontais
numero_magico = None
quadrado_magico = True
for entrada in matriz:
    if numero_magico is None:
        numero_magico = sum(entrada)
    elif sum(entrada) != numero_magico:
        quadrado_magico = False

## verticais
for i in range(l):
    soma = 0
    for entrada in matriz:
        soma += entrada[i]
    if soma != numero_magico:
        quadrado_magico = False

## diagonais
soma_diag_principal = 0
soma_diag_segundária = 0
for i in range(l):
    soma_diag_principal += matriz[i][i]
    soma_diag_segundária += matriz[l - i - 1][l - i - 1]
if soma_diag_principal != numero_magico or soma_diag_segundária != numero_magico:
    quadrado_magico = False
if quadrado_magico:
    print('A matriz e magica')
else:
    print('A matriz nao e magica')