temp_minima = {"K": 0, "F": -459.67, "C":-273.15}
escala = str(input())
temp = float(input())
if temp_minima[escala] > temp:
    print("Valor de temperatura abaixo do minimo")
else:
    if escala == "C":
        C = temp
        F = (1.8 * C) + 32
        K = C + 273.15
        print(f'{F:.2f} F')
        print(f'{K:.2f} K')
    elif escala == "F":
        F = temp
        C = (F - 32) / 1.8
        K = (F - 32) * 5/9 + 273.15
        print(f'{C:.2f} C')
        print(f'{K:.2f} K')
    elif escala == "K":
        K = temp
        C = K - 273.15
        F = (K - 273.15) * 9/5 + 32
        print(f'{C:.2f} C')
        print(f'{F:.2f} F')