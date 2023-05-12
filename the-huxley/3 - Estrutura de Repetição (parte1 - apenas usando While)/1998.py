init = int(input())
while not 1 <= init <= 9:
    print('Insira um número inicial entre 1 e 9')
    init = int(input())
end = int(input())
while not 1 <= end <= 9:
    print('Insira um número final entre 1 e 9')
    end = int(input())
if init > end:
    print('Nenhuma tabuada nesse intervalo')
i = init
while i <= end:
    j = 1
    while j <= 9:
        print(f'{i} x {j} = {i * j}')
        j += 1
    print()
    i += 1