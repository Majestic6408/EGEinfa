from itertools import product

a = sorted(set('ШКОЛА'))

for pos, val in enumerate(product(a, repeat=5), 1):
    val = ''.join(val)
    if 'ШАЛАШ' in val:
        print(pos)