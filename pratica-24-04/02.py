pares = []
impares = []
q_pares = q_impares = 0
while (numero := int(input('Informe um número: '))) != 0:
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)
media = (sum(impares) + sum(pares)) / (len(impares) + len(pares))
media_impares = (sum(impares) / len(impares))
media_pares = (sum(pares) / len(pares))
print(f'Os números pares são: {pares}, a média é {media_pares:.2f}')
print(f'Os números impares são: {impares}, a média é {media_impares:.2f}')
