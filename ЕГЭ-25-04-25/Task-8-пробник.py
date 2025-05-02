from string import ascii_uppercase, digits
from itertools import product
a = digits + ascii_uppercase
a = a[:14]
cnt = 0
for val in product(a, repeat=8):
    val = ''.join(val)
    if val.count('0') == 2 and val[0] != '0' and (val.count('A') + val.count('B') + val.count('C') + val.count('D')) <= 4:
        cnt += 1


print(cnt)