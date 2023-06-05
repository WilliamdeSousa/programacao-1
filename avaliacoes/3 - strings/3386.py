num = input()
res = ''
for c in num:
    if c.isalpha():
        c = c.lower()
        if c in 'abc':
            res += '2'
        elif c in 'def':
            res += '3'
        elif c in 'ghi':
            res += '4'
        elif c in 'jkl':
            res += '5'
        elif c in 'mno':
            res += '6'
        elif c in 'pqrs':
            res += '7'
        elif c in 'tuv':
            res += '8'
        elif c in 'wxyz':
            res += '9'
    else:
        res += c
print(res)
