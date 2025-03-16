from itertools import product

a = sorted('ЛАЙМ')

for pos, val in enumerate(product(a, repeat=5), 1):
    val = ''.join(val)
    if val.count('М') == 0 and val.count('Л') == 0 and 'ЙЙ' not in val:
        print(pos)