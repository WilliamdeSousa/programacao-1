maior = 0
num_maior = 0
for i in range(5):
    soma = 0
    num = int(input())
    for j in range(1, num + 1):
        if num % j == 0:
            soma += j
    if soma > maior:
        num_maior = num
        maior = soma
print(num_maior)