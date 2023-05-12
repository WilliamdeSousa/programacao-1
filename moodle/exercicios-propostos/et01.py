n_entrevistados = 2000
respostas = []
for i in range(n_entrevistados):
    resposta = str(input('Informe o seu sexo: ').strip()[0] + 
                   input('Informe sua resposta: ').strip()[0]).upper()
    respostas.append(resposta)
sexos = []
escolhas = []
for resposta in respostas:
    sexos.append(resposta[0])
    escolhas.append(resposta[1])
print(f'Número de respostas favoráveis: {escolhas.count("S")}')
print(f'Número de respostas desfavoráveis: {escolhas.count("N")}')
n_feminino = sexos.count('F')
n_masculino = sexos.count('M')
print(f'Porcentagem de mulheres: {n_feminino * 100 / n_entrevistados:.2f}%')
print(f'Porcentagem de homens: {n_masculino * 100 / n_entrevistados:.2f}%')
print(f'Porcentagem de mulheres favoráveis: \
      {respostas.count("FS") * 100 / n_feminino:.2f}%')
print(f'Porcentagem de homens desfavoráveis: \
      {respostas.count("MN") * 100 / n_masculino:.2f}%')
