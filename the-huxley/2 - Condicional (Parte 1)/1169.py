lvl = int(input())
if lvl <= 20:
    pot = lvl ** 3 + 20
elif lvl <= 40:
    pot = 8000 + (lvl - 10) ** 2
elif lvl <= 60:
    pot = 9000 + lvl * 5
elif lvl <= 80:
    pot = 9300 + lvl * 2
else:
    pot = 9500 + lvl
print(f'Potencia de : {pot} W')
