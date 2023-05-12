n = int(input('Informe um número: '))
f = n
if n == 0:
    f = 1
elif n < 0:
    print(f'Não há fatorial de números negativos.')
else:
    for i in range(n - 1, 0, -1):
        f *= i
print(f'O fatorial de {n} é {f}.')