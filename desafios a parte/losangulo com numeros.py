n = int(input())
matriz = []
[matriz.extend([[' ' for j in range(i - 1)].__add__([str(j) for j in range(n - i + 1, 0, -1)].__add__([str(j) for j in range(2, n - i + 2)].__add__([' ' for j in range(i, 1, -1)]))) for i in loop]) for loop in [range(n, 0, -1), range(2, n + 1, 1)]]
for linha in matriz:
    print(' '.join(linha))