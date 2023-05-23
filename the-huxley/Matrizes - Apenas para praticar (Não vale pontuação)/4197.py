alf = 'abcdefghijklmnopqrstuvwxyz'
n = int(input())
cadastros = []
for i in range(n):
    senha = ''
    nome, cpf = input().split()
    for i in range(len(nome)):
        senha += alf[(alf.index(nome[i]) + int(cpf[i])) % 26]
    senha += cpf[-2:]
    cadastros.append(f'{nome} {senha}')
cadastros.sort()
for cadastro in cadastros:
    print(cadastro)