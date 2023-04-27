n = int(input())
resp = 'Falso'
i = 1
while i <= n-3 and resp != 'Verdadeiro':
    if i * (i + 1) * (i + 2) == n:
        print(f'{i} * {i + 1} * {i + 2} = {n}')
        resp = 'Verdadeiro'
    i += 1
print(resp)