dia = str(input())
preco = float(input())
opcao = str(input())
nome = str(input())
if dia in ['seg', 'ter', 'qua'] and opcao == 'ouro':
    preco /= 2
elif dia in ['qui', 'sex'] and 10 <= preco <= 100:
    preco /= 3
elif dia == 'sab' and opcao == 'prata':
    preco *= 3
else:
    preco *= 2
print(f'O preco do produto {nome} no dia {dia} eh {preco:.2f}')
