from itertools import product

a = sorted('ПОБЕДА')

for pos, val in enumerate(product(a, repeat=6), 1):
    val = ''.join(val)
    if val[0] == 'О' and len(set(val)) == len(val):
        print(pos)