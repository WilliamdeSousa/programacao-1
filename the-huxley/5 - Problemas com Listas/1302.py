matriz = []
for i in range(3):
    linha = []
    for j in range(3):
        linha.append(int(input().strip()))
    matriz.append(linha)
matriz_ext = []
[matriz_ext.extend(linha) for linha in matriz]
matriz_pos = [i for i in matriz_ext if i > 0]
print(f'{sum(matriz_pos)/len(matriz_pos):.2f}', end=' ')
menor = min(matriz_ext)
print(menor, end=' ')
print(1 if menor % 2 == 0 else 0, end=' ')
print(sum(matriz_ext) - sum([matriz[i][i] for i in range(3)]))