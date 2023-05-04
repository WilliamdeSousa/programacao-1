num = int(input())
matriz = []
for i in range(2):
    lista = []
    for j in range(num):
        lista.append(int(input()))
    matriz.append(lista)
for i in range(num):
    print(matriz[0][i])
    print(matriz[1][i])