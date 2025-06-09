from itertools import product

a = sorted('ДГИАШЭ')
cnt = 0
for pos, val in enumerate(product(a, repeat=5), 1):
    val = ''.join(val)
    if val[0] != 'И' and val[0] != 'А' and val[0] != 'Э' and val[-1] != 'Д' and val[-1] != 'Г' and val[-1] != 'Ш':
        cnt += 1

print(cnt)