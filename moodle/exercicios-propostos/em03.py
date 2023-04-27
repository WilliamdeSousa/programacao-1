n_maior = n_menor = n_boi = int(input('Informe o número do boi: '))
peso_maior = peso_menor = peso = int(input('Informe o peso do boi: (kg) '))
for i in range(89):
    n_boi = int(input('Informe o número do boi: '))
    peso = int(input('Informe o peso do boi: (kg) '))
    if peso > peso_maior:
        peso_maior = peso
        n_maior = n_boi
    elif peso < peso_menor:
        peso_menor = peso
        n_menor = n_boi
print(f'O boi mais gordo é o nº{n_boi}, pesando {peso_maior} kg e o mais magro é o {n_boi}, pesando {peso_menor}')
