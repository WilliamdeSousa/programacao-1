total = cont = 0
print('Insira os valores das doacoes:')
for i in range(100000):
    doacao = float(input())
    if doacao < 0:
        break
    total += doacao
    cont += 1
if cont == 0:
    cont = 1
print(f"""Total arrecadado: {total:.2f}
Valor medio da doacao: {total / cont:.2f}""")