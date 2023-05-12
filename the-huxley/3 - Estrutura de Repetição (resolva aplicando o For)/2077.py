n = int(input())
resp = 'Falso'
for i in range(1, n - 2, 1):
    if i * (i + 1) * (i + 2) == n:
        print(f'{i} * {i + 1} * {i + 2} = {n}')
        resp = 'Verdadeiro'
        break
print(resp)