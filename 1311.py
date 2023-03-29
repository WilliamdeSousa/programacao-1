dias = ['Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sabado']
dia = int(input())
if not 1 <= dia <= 7:
    print('valor invalido')
else:
    print(dias[dia - 1])
