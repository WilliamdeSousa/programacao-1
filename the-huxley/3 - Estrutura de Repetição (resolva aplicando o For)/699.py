ano = int(input())
per = int(input())
print(' '.join([str(ano + (per * (i + 1))) for i in range(3)]))