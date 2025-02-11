from itertools import product

a = sorted(set('ЯСНОВИДЕЦ'))
cnt = 0
for val in product(a, repeat=5):
    val = ''.join(val)
    if val[0] != '0' and val.count(val[0]) == 1 and val.count(val[-1:]):
        for i in 'СНВДЦ':
            val = val.replace(i, '*', 1)
        for i in 'ЯОИЕ':
            val = val.replace(i, '>', 1)
        if val[0] == '*' and val[-1:] == '>':
            cnt += 1

print(cnt)
