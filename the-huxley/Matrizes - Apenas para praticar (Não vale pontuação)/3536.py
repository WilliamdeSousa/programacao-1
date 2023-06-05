n = int(input())
matriz = [[int(i) for i in input().split()] for j in range(n)]
posicao = [0, 0]
ultima_posicao = [0, 0]
chegada = [n - 1, n - 1]
while posicao != chegada:
    # checar caminho possível
    if posicao[0] > 0 and matriz[posicao[0]] - 1 == 1 and [posicao[0] - 1, posicao[1]] != ultima_posicao:
        print('vai pra cima')
    if posicao[0] < n - 1 and matriz[posicao[0] + 1]