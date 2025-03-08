from itertools import product

cnt = 0
a = '0123456'

for val in product(a, repeat=7):
    val = ''.join(val)
    if val[0] != '0':
        for j in '0246':
            val = val.replace(j, '*')
        if val.count('*') == 2:
            cnt += 1

print(cnt)