quant = int(input('Quantos números? '))
soma = 0
for i in range(quant):
    soma += int(input(f'Informe o {i + 1}º número: '))
print(f'A soma vale {soma}')