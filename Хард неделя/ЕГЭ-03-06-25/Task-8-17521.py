from itertools import product

a = '01234567'
cnt  = 0
for val in product(a, repeat=5):
    val = ''.join(val)
    if val[0] != '0' and val[0] != '1' and val[0] != '3' and val[0] != '5' and val[0] != '7' and val[-1] != '2' and val[-1] != '6' and val.count('7') <=2:
        cnt += 1

print(cnt)