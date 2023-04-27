pares = []
impares = []
while (numero := int(input('Informe um número: '))) != 0:
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)
print(f'Os números pares são: {pares}')
print(f'Os números impares são: {impares}')
