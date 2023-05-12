marca_esc = marca = str(input())
preco_esc = preco = 0
while marca != 'sair':
    alcance = int(input())
    usada = str(input())
    if usada == 'U':
        pontos = str(input())
        avarias = str(input())
        if pontos == avarias == 'N' and (marca == 'Nikkor' or marca == 'Sigma') and alcance >= 300: 
            preco = float(input())
            if preco < preco_esc or preco_esc == 0:
                preco_esc = preco
                marca_esc = marca
    elif (marca == 'Nikkor' or marca == 'Sigma') and alcance >= 300:
        preco = float(input())
        if preco < preco_esc or preco_esc == 0:
            preco_esc = preco
            marca_esc = marca
    marca = str(input())
print(marca_esc)
print(preco_esc)