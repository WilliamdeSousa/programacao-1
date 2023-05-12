l = int(input())
c = str(input())
p = str(input())
if not 0 < l <= 100 or c not in ['d', 'g', 'e', 'f'] or p not in ['d', 'c']:
    print('Entrada invalida')
else:
    if p == 'c':
        d = 0
    else:
        d = 0.05
    if c == 'g':
        v = 7.3 * l
        print(f'Total a ser pago: {v * (1 - d):.2f}')
        print(f'Valor do desconto: {d * v:.2f}')
    elif c == 'd':
        v = 6.6 * l
        print(f'Total a ser pago: {v * (1 - d):.2f}')
        print(f'Valor do desconto: {d * v:.2f}')
    elif c == 'e':
        v = 5.6 * l
        print(f'Total a ser pago: {v * (1 - d):.2f}')
        print(f'Valor do desconto: {d * v:.2f}')
    else:
        print(f'''Carro Flex - Gasolina
Total a ser pago: {7.3 * l * (1 - d):.2f}
Valor do desconto: {7.3 * l * d:.2f}
Carro Flex - Etanol
Total a ser pago: {5.6 * l * (1 - d):.2f}
Valor do desconto: {5.6 * l * d:.2f}''')