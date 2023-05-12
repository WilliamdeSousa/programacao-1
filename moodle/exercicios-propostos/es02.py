n = int(input('quantos números? '))
s = 0
while n > 0:
    s += float(input('informe um número: '))
    n -= 1
print(f'a soma dos números digitados vale {s}')