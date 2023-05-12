n_notas = int(input())
notas = []
if n_notas <= 0:
    print('Numero de notas invalido.')
else:
    for i in range(n_notas):
        notas.append(float(input()))
    for i, nota in enumerate(notas):
        print(f'Nota {i + 1}: {nota:.1f}')
    print(f'Media: {sum(notas) / n_notas:.2f}')