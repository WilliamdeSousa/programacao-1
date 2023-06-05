vogais = [0, 0, 0, 0, 0]
while not (letra := input().upper()).isnumeric():
    if letra == 'A':
        vogais[0] += 1
    elif letra == 'E':
        vogais[1] += 1
    elif letra == 'I':
        vogais[2] += 1
    elif letra == 'O':
        vogais[3] += 1
    elif letra == 'U':
        vogais[4] += 1
print(f'Foram digitadas {sum(vogais)} vogais. Sendo elas: ')
for i in range(5):
    print(f'{vogais[i]} letra(s) {["A", "E", "I", "O", "U"][i]}.')