# recebendo entradas
n = int(input())
matriz = [[(False, True)[int(i)] for i in input().split()] for j in range(n)]

# posição inicial
posicao = [0, 0]
ultima_posicao = [0, 0]

# posição final
chegada = [n - 1, n - 1]

while posicao != chegada:
    # posição x e y
    y, x = posicao
    
    # checar caminho possível
    ## se não estiver no canto esquerdo, checar se pode ir pra direita
    if not (matriz[0][0] and matriz[n - 1][n - 1]):
        print('NOT OK')
        break
    if x > 0 and matriz[y][x - 1] and [y, x - 1] != ultima_posicao:
        ultima_posicao = posicao
        posicao = [y, x - 1]
    elif x < n - 1 and matriz[y][x + 1] and [y, x + 1] != ultima_posicao:
        ultima_posicao = posicao
        posicao = [y, x + 1]
    elif y > 0 and matriz[y - 1][x] and [y - 1, x] != ultima_posicao:
        ultima_posicao = posicao
        posicao = [y - 1, x]
    elif y < n - 1 and matriz[y + 1][x] and [y + 1, x] != ultima_posicao:
        ultima_posicao = posicao
        posicao = [y + 1, x]
    else:
        print('NOT OK')
        break
else:
    print('OK')