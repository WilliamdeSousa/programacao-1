maior_2m = 0
for i in range(20):
    alt = float(input(f'Informe a altura da {i+1}ª pessoa: '))
    if i == 0:
        soma = maior = alt
    else:
        soma += alt
        if alt > maior:
            maior = alt
    if alt > 2:
        maior_2m += 1
print(f'A maior altura foi {maior:.1f}m\nA média de altura foi {soma/20:.1f}\nE temos {maior_2m} pessoa(s) maior(es) que 2 metros.')