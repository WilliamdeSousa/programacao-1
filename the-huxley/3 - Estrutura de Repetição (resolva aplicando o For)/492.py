capsulas = 0
for i in range(7):
    quant = int(input())
    taman = input().upper()
    if taman == 'P':
        capsulas += (10 * quant)
    else:
        capsulas += (16 * quant)
print(capsulas)
print(capsulas * 2 // 7)
