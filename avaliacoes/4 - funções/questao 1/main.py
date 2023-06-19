from funcoes import media

tamanho = int(input())
numeros = []
for i in range(tamanho):
    numeros.append(float(input()))
m = media(numeros)
print(f'{m}')