sal = float(input())
if sal > 500:
    sal *= 1.1
elif sal > 300:
    sal *= 1.07
else:
    sal *= 1.05
print(f'{sal:.2f}')
