quant_numeros = int(input())
numeros = list()
for i in range(quant_numeros):
    numeros.append(int(input()))
maior = max(numeros)
menor = min(numeros)
print(f'Maior: {maior} apareceu {numeros.count(maior)} vezes')
print(f'Menor: {menor} apareceu {numeros.count(menor)} vezes')