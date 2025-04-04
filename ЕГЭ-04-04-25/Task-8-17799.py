from itertools import product

a = sorted('АРГУМЕНТ')

for pos, val in enumerate(product(a, repeat=4), 1):
    val = ''.join(val)
    if len(val) == len(set(val)) and list(val) == sorted(val):
        print(pos)