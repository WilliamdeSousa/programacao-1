glic = soma = int(input())
c = 0
while glic != 0:
    glic = int(input())
    soma += glic
    c += 1
media = soma / c
if media < 110:
    print('Glicose Normal')
elif media < 200:
    print('Glicose Alterada')
else:
    print('Glicose Muito Alta')