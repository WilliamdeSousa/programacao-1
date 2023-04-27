cidade = str(input()).upper()
resp = 'SEM DESTINO'
maior_dist = 0
while cidade != 'FIM':
    dist = int(input())
    custo = float(input())
    if custo <= 150 and maior_dist < dist:
        maior_dist = dist
        resp = cidade
    cidade = str(input()).upper()
print(resp)