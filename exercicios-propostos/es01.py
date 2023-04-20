s = c = 0
while (n:=int(input('informe um número: (0 para parar) '))) != 0:
    if s > 0:
        s += n
        c += 1
print(f'a média dos números vale {s/c}')
