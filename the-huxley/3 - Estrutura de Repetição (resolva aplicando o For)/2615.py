divida = int(input())
pagar_mes = int(input())
for i in range(divida, 0, - pagar_mes):
    print(f'(antes) {i}')
    depois = i - pagar_mes
    print(f'(depois) {depois if depois >= 0 else 0}')