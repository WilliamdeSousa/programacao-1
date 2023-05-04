n = int(input())
notas = []
for i in range(n):
    notas.append(float(input()))
media = sum(notas) / len(notas)
print(f'{media:.2f}')
print(len([i for i in notas if i > media * 1.1]))
print(len([i for i in notas if i < media * 0.9]))