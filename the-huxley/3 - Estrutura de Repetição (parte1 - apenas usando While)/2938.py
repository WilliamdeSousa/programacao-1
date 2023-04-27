doac = int(input())
total_agr = total_fut = 0
while doac >= 1:
    opc = int(input())
    while opc > 2:
        print('Valor invalido')
        opc = int(input())
    if opc == 1:
        total_agr += doac
    else:
        meses = int(input())
        while not 2 <= meses <= 12:
            print('Favor digitar valor entre 2 e 12, inclusive')
            meses = int(input())
        total_agr += doac
        total_fut += doac * (meses - 1)
    doac = int(input())
print(f'Total arrecadado para agora: R$ {total_agr:.2f}')
print(f'Total arrecadado para meses futuros: R$ {total_fut:.2f}')