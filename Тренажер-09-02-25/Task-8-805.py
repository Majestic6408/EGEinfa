from itertools import product

a = '0234567'
cnt = 0
for val in product(a, repeat=5):
    val = ''.join(val)
    if val[0] != '0' and len(set(val)) == 5:
        for i in '0246':
            val = val.replace(i, '*', 1)
        for i in '357':
            val = val.replace(i, '<', 1)
        if '**' not in val and '<<' not in val:
            cnt += 1

print(cnt)