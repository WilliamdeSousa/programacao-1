n_cartas = int(input())
joao = list()
maria = list()
for i in range(n_cartas):
    carta = int(input())
    if carta % 2 == 0:
        joao.append(carta)
    else:
        maria.append(carta)
soma_joao = sum(set(joao))
soma_maria = sum(set(maria))
print(len(joao))
print(len(maria))
print(soma_joao if soma_joao > soma_maria else soma_maria)