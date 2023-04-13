n = int(input('Quantos números mostrar? '))
i = 0
anter = 0
atual = 0
proxi = 1
while i < n:
    print(atual)
    anter = atual
    atual = proxi
    proxi = atual + anter
    i += 1