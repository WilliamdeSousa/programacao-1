entrada = input()
soma = [0, 0]
if len(entrada.split()) == 1:
    n = int(entrada)
    for i in range(2):
        for j in range(n):
            for k in input().split():
                soma[i] += int(k)
else:
    n = len(entrada.split())
    for i in range(2):
        for j in range(n):
            if i == j == 0:
                for k in entrada.split():
                    soma[i] += int(k)
            else:
                for k in input().split():
                    soma[i] += int(k)
print('SIM' if soma[0] == soma[1] else 'NÃO')