q_livros = int(input())
q_alunos = int(input())
conceito = q_alunos / q_livros
if conceito <= 8:
    print('A')
elif conceito <= 12:
    print('B')
elif conceito <= 18:
    print('C')
else:
    print('D')