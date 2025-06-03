from itertools import product
from string import ascii_uppercase, digits

a = digits + ascii_uppercase
a = a[:15]
cnt = 0
for val in product(a, repeat=5):
    val = ''.join(val)
    if val[0] != '0' and val.count('8') == 1 and val.count('A') + val.count('B') + val.count('C') + val.count('D') + val.count('E') >= 2:
        cnt += 1


print(cnt)