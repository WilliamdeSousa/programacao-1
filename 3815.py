dia = int(input())
if not 1 <= dia <= 31:
    print(f'Dia inexistente')
else:
    mes = int(input())
    if not 1 <= mes <= 12:
        print(f'Mês inexistente')
    elif ((mes == 4 or mes == 6 or mes == 9 or mes == 11) and dia > 30) or (mes == 2 and dia > 29):
        print(f'Esse dia não existe nesse mês')
    else:
        ano = int(input())
        if not 1900 <= ano <= 2020:
            print('Ano inexistente')
        elif not (ano % 4 == 0 and ((not ano % 100 == 0) or (ano % 100 == 0 and not ano % 400))) and dia == 29 and mes == 2:
            print('Esse ano não é bissexto')
        else:
            print('Data Validada')