lista = []
matriz = []
for i in range(3):
    linha = []
    for j in range(3):
        linha.append(int(input()))
    matriz.append(linha)
    lista.extend(linha)
media = sum(lista) / len(lista)
maior = max(lista)
soma_delta = 1 if maior > 0 else 1 if maior < 0 else 0
soma_diag = sum([matriz[i][i] for i in range(3)])
print(f'{media:.2f} {maior} {soma_delta} {soma_diag}')
