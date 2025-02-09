from itertools import product

a = sorted(set('ЯНВАРЬ'))

for pos, val in enumerate(product(a, repeat=5), 1):
    val = ''.join(val)
    if val[0] != '0' and val[0] != 'Я' and val.count('Ь') < 2 and 'ЯЯ' not in val:
        print(pos)