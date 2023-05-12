n_pessoas = soma = 0
maior = menor = None
while (i := int(input())) != 0:
    n_pessoas += 1
    soma += i
    if maior is None:
        maior = menor = i
    elif i > maior:
        maior = i
    elif i < menor:
        menor = i
print(f'Foram lidos os dados de {n_pessoas} pessoa(s).')
print(f'A média de idade é de {soma/n_pessoas:.2f} anos')
print(f'A maior idade foi de {maior} anos e a menor foi de {menor} anos')