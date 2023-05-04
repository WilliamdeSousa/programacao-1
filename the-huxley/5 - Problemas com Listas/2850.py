pokemons = [{}, {}]
for i in range(2):
    for j in range(6):
        if j == 0:
            pokemons[i] = {
                'nome': str(input()),
                'id': int(input()),
                'ataque': int(input()),
                'vida': int(input())
            }
        else:
            atual = {
                'nome': str(input()),
                'id': int(input()),
                'ataque': int(input()),
                'vida': int(input())
            }
            if (pokemons[i]['ataque'] == atual['ataque'] and atual['id'] < pokemons[i]['id']) or (pokemons[i]['ataque'] < atual['ataque']):
                pokemons[i] = atual
red, blue = pokemons
while red['vida'] > 0 and blue['vida'] > 0:
    red['vida'] -= blue['ataque']
    blue['vida'] -= red['ataque']
print(f"""Pokemon do Red: {red['nome']}
Pokemon do Blue: {blue['nome']}""")
if red['vida'] <= 0 and blue['vida'] <= 0:
    print('Empate')
else:
    print(f'Vencedor: {"Red" if blue["vida"] <= 0 else "Blue"}')