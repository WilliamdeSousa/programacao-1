n = [float(i) for i in input().split()]
credito = 0
debito = 0
while n[0] != -1:
    if n[0] == 0:
        debito += n[1]
    elif n[0] == 1:
        credito += n[1]
    n = [float(i) for i in input().split()]
print(f'''Creditos: R$ {credito:.2f}
Debitos: R$ {debito:.2f}
Saldo: R$ {credito - debito:.2f}''')