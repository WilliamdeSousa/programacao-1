i = 0 
while i < 100:
    n = int(input(f'Informe o {i + 1}º número: '))
    if i == 0:
        maior = menor = soma = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
        soma += n
    i += 1
print(f'O maior é {maior}, o menor é {menor} e a média é {soma/100}')