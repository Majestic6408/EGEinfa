from itertools import product

a = '01234567'
cnt = 0
for val in product(a,repeat=6):
    val = ''.join(val)
    if val[0] != '0' and len(set(val)) == len(val) and int(val, 8) % 5 == 0:
        for i in '1357':
            val = val.replace(i, '*')
        for i in '0246':
            val = val.replace(i, '<')
        if '**' not in val and '<<' not in val:
            cnt += 1

print(cnt)