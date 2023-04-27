d = int(input())
e = [False, True][int(input())]
s = [False, True][int(input())]
fds = d >= 5
i = 15
c = 'COMUM'
if fds:
    i *= 2
if e:
    i *= 0.7
    c = 'ESTUDANTE'
if s:
    c = 'SOCIO'
    if fds:
        i *= 0.8
print(f'{c}: R$ {i:.2f}')