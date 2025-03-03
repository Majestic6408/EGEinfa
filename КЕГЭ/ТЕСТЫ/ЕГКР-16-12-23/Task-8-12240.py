from itertools import product

a = '012345678'
cnt = 0
for val in product(a, repeat=5):
    val = ''.join(val)
    if val[0] != '0' and val.count('5') == 1 and '00' not in val and '11' not in val and '22' not in val and '33' not in val and '44' not in val and '55' not in val and '66' not in val and '77' not in val and '88' not in val:
        cnt += 1

print(cnt)