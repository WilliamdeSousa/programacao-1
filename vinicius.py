dia = int(input(""))
if dia < 1 or dia > 31:
    print("Dia inexistente")
else:
    mes = int(input(""))
    if mes < 1 or mes > 12:
        print("Mês inexistente")
    elif mes == 2:
        if dia < 1 or dia > 29:
            print("Esse dia não existe nesse mês")

    ano = int(input(""))
    if ano < 1900 or ano > 2020:
        print("Ano inexistente")

    else:
        if mes in [1, 3, 5, 7, 8, 10, 12]:
            if dia < 1 or dia > 31:
                print("Esse dia não existe nesse mês")
            else:
                print("Data Validada")
        elif mes in [4, 6, 9, 11]:
            if dia < 1 or dia > 30:
                print("Esse dia não existe nesse mês")
            else:
                print("Data Validada")
        elif mes == 2:
            if dia < 1 or dia > 29:
                print("Esse dia não existe nesse mês")
            elif dia == 29 and (ano % 4 != 0 or (ano % 100 == 0 and ano % 400 != 0)):
                print("Esse ano não é bissexto")
            else:
                print("Data Validada")
        else:
            print("Mês inexistente")