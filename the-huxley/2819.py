aborda = {
    'Interface Grafica': bool, 
    'Inteligencia Artificial': bool, 
    'Encapsulamento': bool, 
    'Indentacao': bool, 
    'Structs': bool
    }
for requisito in aborda.keys():
    aborda[requisito] = (False, True)[int(input(f'Trabalho aborda {requisito}? (0 - Nao 1 - Sim)\n'))]
if (aborda['Interface Grafica'] or aborda['Inteligencia Artificial']) and (aborda['Encapsulamento'] and aborda['Indentacao']) and aborda['Structs']:
    print('Seu trabalho sera avaliado.')
else:
    print('Seu trabalho nao sera avaliado, nota 0.')