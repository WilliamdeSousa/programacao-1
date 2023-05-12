idade = int(input())
if idade <= 2:
    print('Bebe')
elif idade <= 12:
    print('O individuo eh uma Crianca Jovem Menor de Idade.')
elif idade <= 18:
    print('Adolescente')
elif idade <= 19:
    print('Jovem')
elif idade <= 45:
    print('Adulto')
elif idade <= 60:
    print('Adulto de Meia-idade')
elif idade <= 75:
    print('Idosos')
elif idade <= 90:
    print('Anciao')
else:
    print('O individuo eh um Idoso na Velhice Extrema Maior de Idade.')