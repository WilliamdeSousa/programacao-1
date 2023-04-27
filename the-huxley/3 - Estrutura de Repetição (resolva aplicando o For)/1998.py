ini = int(input())
while not 1 <= ini <= 9:
	print('Insira um n�mero inicial entre 1 e 9')
	ini = int(input())
fim = int(input())
while not 1 <= fim <= 9:
	print('Insira um n�mero final entre 1 e 9')
	fim = int(input())
if fim < ini:
	print('Nenhuma tabuada nesse intervalo')
else:
	for i in range(ini, fim + 1, 1):
		for j in range(1, 10, 1):
			print(f'{i} x {j} = {i * j}')
		print()