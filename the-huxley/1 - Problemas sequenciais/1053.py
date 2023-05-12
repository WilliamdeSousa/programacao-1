h = float(input()) # altura
r = float(input()) # raio
pi = 3.14
area = 2 * pi * r * h + 2 * pi * r ** 2
volume = (pi * r ** 2) * h
print(f'{volume:.2f}\n{area:.2f}')
