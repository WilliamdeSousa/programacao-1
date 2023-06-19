def media(lista):
    return soma(lista) / tamanho(lista)

def soma(lista):
    if tamanho(lista) > 1:
        return lista[0] + soma(lista[1:])
    else:
        return lista[0]

def tamanho(lista):
    c = 0
    for i in lista:
        c += 1
    return c