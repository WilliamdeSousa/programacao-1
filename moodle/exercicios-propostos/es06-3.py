for i in range(100):
    numero = int(input(f'Informe o {i + 1}º número: '))
    if i == 0:
        maior = menor = soma = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
        soma += numero
print(f'O maior é {maior}, o menor é {menor} e a média vale {soma / 100}')