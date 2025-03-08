from itertools import product

a = sorted('ПАРУС')

for pos, val in enumerate(product(a, repeat=5), 1):
    val = ''.join(val)
    if val.count('У') <= 1 and 'АА' not in val:
        print(pos)