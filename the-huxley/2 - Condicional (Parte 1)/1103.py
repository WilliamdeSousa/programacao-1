idade = int(input())
if not 0 <= idade <= 130:
    print('Idade invalida.')
else:
    jogo = str(input())
    limite = {'azar': 21, 'mmorpg': 14, 'moba': 10, 'casual': 0}
    if jogo not in limite.keys():
        print('Jogo invalido.')
    elif idade >= limite[jogo]:
        print('Pode entrar!')
    else:
        print('Volte daqui há alguns anos.')
