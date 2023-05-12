total_eleitores = int(input('Total de Eleitores: '))
votos_brancos = int(input('Quantidade de votos em branco: '))
votos_nulos = int(input('Quantidade de votos nulos: '))
votos_validos = int(input('Quantidade de votos válidos: '))

perc_brancos = votos_brancos * 100 / total_eleitores
perc_nulos = votos_nulos * 100 / total_eleitores
perc_validos = votos_validos * 100 / total_eleitores

print(f'''PERCENTUAIS RELATIVOS
Votos em branco: {perc_brancos:.1f} %
Votos nulos: {perc_nulos:.1f} %
Votos válidos: {perc_validos:.1f} %''')
