preco = {
    'lasanha': 8, 
    'estrogonofe': 11,
    'refrigerante': 3,
    'suco': 2.5
}
comida = str(input()).lower()
bebida = str(input()).lower()
total = preco[comida] + preco[bebida]
print(f'{total:.2f}')
