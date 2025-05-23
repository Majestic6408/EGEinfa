from itertools import product

a = '0123456'
cnt = 0
for val in product(a, repeat=5):
    val = ''.join(val)
    if val[0] != '0':
        for i in '0246':
            val = val.replace(i, '^')
        if val.count('^^') >= 2 and '^^^' not in val:
            cnt += 1

print(cnt)