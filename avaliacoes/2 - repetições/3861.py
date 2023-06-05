idade = int(input())
while idade != 0:
    if idade < 0:
        print('Você ainda não nasceu.')
    elif idade <= 11:
        print('Você é uma criança.')
    elif idade <= 17:
        print('Você é um adolescente.')
    elif idade <= 35:
        print('Você é um jovem.')
    elif idade <= 64:
        print('Você é um adulto.')
    else:
        print('Você é um idoso.')
    idade = int(input())
