nc = 0
mm = 0
for i in range(1000000):
    qc = int(input())
    if qc == 999:
        break
    if qc > 2:
        nc += 1
        mm += (12.89 * (qc - 2))
print(f'{mm:.2f}\n{nc}')