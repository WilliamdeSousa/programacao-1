q_pessoas = int(input())
cidade = str(input()).upper()
q_quartos = int(input())
if cidade == 'PIPA':
    total = q_quartos * 300 + 75 * q_pessoas
elif cidade == 'FORTALEZA':
    if q_quartos == 3:
        total = 950
    else:
        total = 1120
    total += 60 * q_pessoas
print(f'{total:.2f}')
print(f'{total / q_pessoas:.2f}')
