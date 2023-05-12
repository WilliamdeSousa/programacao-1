s = xa = float(input())
i = c = 0
while i < 6:
    x = float(input())
    s += x
    if x >= xa + 0.5:
        c += 1
    xa = x
    i += 1
print(f'R$ {s:.2f}')
print(c)