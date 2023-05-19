mensagem = '0ajsISdha&*!2'
chave = int(mensagem[-1]) if mensagem[0] == '0' else int(-mensagem[-1])
mensagem = mensagem[1:-1]
resultado = ''
for c in mensagem:
    if c.isalpha() and c.islower():
        resultado += chr((((ord('a') - 97) % 26) + chave + 97))
    else:
        resultado += c
print(resultado)