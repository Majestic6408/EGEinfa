from itertools import product

a = sorted('ФОКУС')

for pos, val in enumerate(product(a, repeat=5), 1):
    val = ''.join(val)
    if val.count('У') == 2 and 'Ф' not in val:
        print(pos)