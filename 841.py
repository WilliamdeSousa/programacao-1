numeros = list()
for i in range(3):
    numeros.append(float(input()))
media = sum(numeros) / 3
maiores = 0
for numero in numeros:
    if numero > media:
        maiores += 1
print(maiores)
