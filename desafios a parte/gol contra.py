def tratamento(local, tipo, jogador) -> str:
    if local == 'c':
        jogador = inverter(jogador)
    if tipo == '1':
        jogador = jogador + (jogador[-1] * 4)
    return jogador
        

def inverter(nome) -> str:
    return nome[::-1].title()


entrada = input()
local = entrada.split()[0]
tipo = entrada.split()[1]
jogador = ' '.join(entrada.split()[2:])

resultado = tratamento(local, tipo, jogador)
print(resultado)