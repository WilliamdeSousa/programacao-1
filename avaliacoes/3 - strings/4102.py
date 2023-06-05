notas = [int(i) for i in input().split()]
while len(notas) < 5:
    print('Deve ser digitado pelo menos 5 notas.')
    notas = [int(i) for i in input().split()]
print('A lista de notas é:')
print(notas)
print('Foram lançadas as seguintes notas:')
unicas = []
for nota in notas:
    if nota not in unicas:
        unicas.append(nota)
print(unicas)
for nota in unicas:
    repetiu = notas.count(nota)
    print(f'A nota {nota} repetiu {repetiu} vezes.')
    if nota == notas[0]:
        repetida = [nota, repetiu]
    else:
        if repetiu > repetida[1]:
            repetida = [nota, repetiu]
print(f'A nota que mais se repetiu foi a: {repetida[0]}, ela foi responsável por {repetida[1] * 100 / len(notas):.1f}% das notas')
