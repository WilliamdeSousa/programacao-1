total_instalados, total_programas = [int(i) for i in input().split()]
programas_instalados = dict()
for i in range(total_instalados):
    programa, versao = [int(j) for j in input().split()]
    programas_instalados[programa] = versao
atualizacoes = dict()
for i in range(total_programas):
    programa, versao = [int(j) for j in input().split()]
    if programa in list(programas_instalados.keys()):
        if versao > programas_instalados[programa]:
            if programa in list(atualizacoes.keys()):
                if versao > atualizacoes[programa]:
                    atualizacoes[programa] = versao
            else:
                atualizacoes[programa] = versao
atualizacoes_programas = sorted(list(atualizacoes.keys()))
for atualizacao in atualizacoes_programas: 
    print(f'{atualizacao} {atualizacoes[atualizacao]}')
