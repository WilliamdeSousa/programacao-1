nome = str(input())
soma = 0
quant = 0
if nome == 'sair':
    print('Nenhum jogador foi registrado.')
else:
    pont = float(input())
    soma += pont
    quant += 1
    me_pont = pont
    me_nome = nome
    ma_pont = pont
    ma_nome = nome
    nome = str(input())
while nome != 'sair':
    pont = float(input())
    soma += pont
    quant += 1
    if pont <= me_pont:
        me_pont = pont
        me_nome = nome
    if pont >= ma_pont:
        ma_pont = pont
        ma_nome = nome
    nome = str(input())
if quant >= 1:
    print(me_nome)
    print(ma_nome)
    print(f'{soma / quant:.2f}')