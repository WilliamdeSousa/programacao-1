impar = []
par = []
for i in range(15):
    num = int(input())
    if num % 2 == 1:
        impar.append(num)
    else:
        par.append(num)
    if len(impar) == 5:
        for c, j in enumerate(impar):
            print(f'impar[{c}] = {j}')
        impar.clear()
    if len(par) == 5:
        for c, j in enumerate(par):
            print(f'par[{c}] = {j}')
        par.clear()
if len(impar) > 0:
    for c, i in enumerate(impar):
        print(f'impar[{c}] = {i}')
if len(par) > 0:
    for c, i in enumerate(par):
        print(f'par[{c}] = {i}')