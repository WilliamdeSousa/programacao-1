salario = float(input())
comprometido = float(input())
parcela_maxima = salario * 0.3 - comprometido
if parcela_maxima < 0:
    parcela_maxima = 0
print(f'{parcela_maxima:.2f}')
