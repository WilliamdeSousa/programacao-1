q = 1
q_v = tot_v = tot_c = 0
jovem = i = int(input())
maior = v = float(input())
p = str(input())
e = str(input()).upper()
for j in range(9999999): # mesma coisa que while True
    if p == 'V':
        tot_v += v
        q_v += 1
    elif p == 'C':
        tot_c += v
    if v > maior:
        maior = v
    if i < jovem:
        jovem = i
    if e == 'N':
        break
    q += 1
    i = int(input())
    v = float(input())
    p = str(input())
    e = str(input()).upper()
print(q)
print(f'{tot_v:.2f}') if tot_v > 0 else print('0')
print(f'{tot_c:.2f}') if tot_c > 0 else print('0')
print(jovem)
print(f'{maior:.2f}')
print(f'{tot_v / q_v:.2f}') if q_v > 0 else print('0')