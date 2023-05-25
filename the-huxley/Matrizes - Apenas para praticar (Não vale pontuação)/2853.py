def transposta(matriz: list) -> list:
    """Recebe uma matriz IxJ e retorta a transposta, ou seja, a matriz JxI"""
    n_linhas = len(matriz)
    n_colunas = len(matriz[0])
    matriz_transposta = []
    for i in range(n_colunas):
        linha_atual = []
        for j in range(n_linhas):
            linha_atual.append(matriz[j][i])
        matriz_transposta.append(linha_atual)
    return matriz_transposta


n_linhas, n_colunas = [int(i) for i in input('Digite as dimensoes da matriz:\n').split()]
print('Digite os elementos da matriz:')
matriz = []
for i in range(n_linhas):
    linha = [int(j) for j in input().split()]
    matriz.append(linha)
matriz = transposta(matriz)
print(f'Matriz transposta:')
for linha in matriz:
    for e in linha:
        print(f'{e:<6}', end='')
    print()