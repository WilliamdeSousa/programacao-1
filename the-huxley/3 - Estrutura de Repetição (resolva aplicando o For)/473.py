aprovados = 0
for i in range(9999999):
    p = int(input())
    if p < 0:
        break
    m = int(input())
    r = float(input())
    if (p * 100 / 50) >= 80 and (m * 100 / 35) >= 60 and r >= 7:
        aprovados += 1
print(aprovados)