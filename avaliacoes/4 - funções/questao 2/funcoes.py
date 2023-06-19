def referencia(nome: str):
    resultado = f'{nome.split()[-1].upper()},'
    for palavra in nome.split()[:-1]:
        if preposicao(palavra):
            resultado += f' {palavra.lower()}'
        else:
            resultado += f' {palavra.capitalize()}'
    resultado += '.'
    return resultado 

def preposicao(palavra):
    return palavra in ['de', 'da', 'do', 'das', 'dos', 'e']
