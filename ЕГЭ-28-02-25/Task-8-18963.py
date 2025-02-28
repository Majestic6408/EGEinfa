from itertools import product

a = set(sorted('КОТБУС'))

cnt = 0
for val in product(a, repeat=8):
    val = ''.join(val)
    if val[0] != 'О' and val[0] != 'У' and 'КОТ' in val:
        cnt += 1


print(cnt)