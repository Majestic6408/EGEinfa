from string import digits, ascii_uppercase
from itertools import product

a = digits + ascii_uppercase

a = a[:12]
cnt = 0
for val in product(a, repeat=5):
    val = ''.join(val)
    if val[0] != '0' and val.count('7') == 1 and val.count('9') + val.count('A') + val.count('B') + val.count('C') < 4:
        cnt += 1

print(cnt)