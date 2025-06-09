from itertools import product

a = '0123456789'

cnt = 0
for val in product(a, repeat=4):
    val = ''.join(val)
    if val[0] != '0' and len(set(val)) == len(val):
        for i in '02468':
            val = val.replace(i, '*')
        for j in '13579':
            val = val.replace(j, '>')
        if '**' not in val and '>>' not in val:
            cnt += 1

print(cnt)