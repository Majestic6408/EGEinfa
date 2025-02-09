from itertools import product

a = sorted(set('ЛАЙМ'))

for pos, val in enumerate(product(a, repeat=5), 1):
    val = ''.join(val)
    if val[0] != '0' and 'М' not in val and 'Л' not in val and 'ЙЙ' not in val:
        print(pos)