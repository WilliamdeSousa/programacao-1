temperatura = float(input())
sintomas = str(input())
if sintomas not in ['S', 'N']:
    print('Erro')
elif temperatura >= 37 and sintomas == 'S':
    print('Exames Especiais')
elif temperatura < 37 and sintomas == 'N':
    print('Liberado')
else:
    print('Exames Basicos')
