q_vogais = [0, 0, 0, 0, 0]
vogais = ['a', 'e', 'i', 'o', 'u']
while (letra := str(input('Informe uma letra: ')).lower()) != 'z':
    if letra in vogais:
        q_vogais[vogais.index(letra)] += 1
print('Quantidade de vezes que repetiu as vogais:')
for i, v in enumerate(vogais):
    print(f'{v.upper()}: {q_vogais[i]}')