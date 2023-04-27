q_linhas = int(input())
q_funcoes = int(input())
tamanho_eq = int(input())
n_bugs = int(input())
eficiencia = (q_linhas / q_funcoes) / tamanho_eq - 4.2 * n_bugs
print(f'{eficiencia:.1f}')
