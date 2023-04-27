i = int(input())
if i <= 2:
    sit = ' Bebe Jovem Menor de Idade'
elif i <= 12:
    sit = 'a Crianca Jovem Menor de Idade'
elif i < 18:
    sit = ' Adolescente Jovem Menor de Idade'
elif i <= 19:
    sit = ' Jovem Maior de Idade'
elif i <= 45:
    sit = ' Adulto Maior de Idade'
elif i < 60:
    sit = ' Adulto de Meia Idade Maior de Idade'
elif i <= 75:
    sit = ' Idoso Maior de Idade'
elif i <= 90:
    sit = ' Idoso Ansiao Maior de Idade' #mudei no vscode e esqueci daqui
else:
    sit = ' Idoso na Velhice Extrema Maior de Idade'
print(f'O individuo eh um{sit}.')