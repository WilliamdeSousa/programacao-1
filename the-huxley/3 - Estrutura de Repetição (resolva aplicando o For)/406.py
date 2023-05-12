ini = int(input())
fim = int(input())
soma = 0
if ini < fim:
    pas = 1
else:
    pas = -1
for i in range(ini, fim + 1, pas):
    if i > 0:
        soma += i
print(soma)