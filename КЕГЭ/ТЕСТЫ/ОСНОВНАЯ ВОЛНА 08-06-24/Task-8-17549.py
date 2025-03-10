from itertools import product

a = sorted('ФОКУС')

for pos, val in enumerate(product(a, repeat=5), 1):
    val = ''.join(val)
    if 'Ф' not in val and val.count('У') == 2:
        print(pos)