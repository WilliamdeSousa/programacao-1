i = 0
q_homens = 0
q_mulheres = 0
media = 0
sal_maior = 0
media_homens = 0
while i < 10:
    sal = float(input())
    sexo = str(input())
    media += sal
    if sal > sal_maior:
        sal_maior = sal
        sexo_maior = sexo
    if sexo == 'f':
        q_mulheres += 1
    else:
        q_homens += 1
        media_homens += sal
    i += 1
print(q_homens)
print(q_mulheres)
print(f'{media / 10:.1f}')
print(sexo_maior)
print(f'{media_homens / q_homens:.1f}')