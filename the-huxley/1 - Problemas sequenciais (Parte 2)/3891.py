n = list()
for i in range(3):
    n.append(float(input()))
print(f'{sum(n) / 3:.2f}')
for peso in [[2, 2, 3], [1, 2, 2]]:
    soma = 0
    for i in range(3):
        soma += n[i] * peso[i]
    print(f'{soma / sum(peso):.2f}')
