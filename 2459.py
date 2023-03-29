heroi = {
    'Homem de Ferro': ['Armadura de Ferro', 10],
    'Hulk': ['Força Bruta', 5],
    'Capitão América': ['Escudo', 7],
    'Thor': ['Martelo', 4],
    'Gavião Arqueiro': ['Arco e Flecha', 12],
    'Viúva Negra': ['Inteligência', 20]
}
nome = str(input())
if nome not in heroi.keys():
    print('Vingador Inválido')
else:
    poder = str(input())
    energia = int(input())
    if heroi[nome][0] == poder:
        if heroi[nome][1] > energia:
            print(f'{nome} NAO conseguiu derrotar Thanos, chamem outro Vingador')
        else:
            print(f'{nome} conseguiu derrotar Thanos')
    else:
        print(f'{nome} NAO conseguiu derrotar Thanos')
        for v in heroi.keys():
            if heroi[v][0] == poder:
                print(f'Esse é o poder do {v}')