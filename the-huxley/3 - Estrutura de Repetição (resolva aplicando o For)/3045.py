for i in range(1000000):
    n = int(input())
    if n == 0:
        break
    print('S' if n % 7 == 0 else 'N')