mensal = {
    '6 ef': 10000,
    '7 ef': 12000,
    '8 ef': 15000,
    '9 ef': 16000,
    '1 em': 20000,
    '2 em': 25000,
    '3 em': 30000,
}
series = list(mensal.keys())
inicial = series.index(input())
final = series.index(input())
c = 1
for i in range(inicial, final + 1):
    serie = series[i]
    print(f'na série {serie[0]}º {serie[2:].upper()}, o aluno pagará R$ {mensal[serie] * c:.2f} ({mensal[serie]} - {(1 - c) * 100:.2f}% ({(1 - c) * mensal[serie]:.2f}))')
    c -= 0.1