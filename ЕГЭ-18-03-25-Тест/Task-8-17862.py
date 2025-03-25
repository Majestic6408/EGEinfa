from itertools import product
from string import digits, ascii_uppercase

a = digits + ascii_uppercase
a = a[:12]
cnt = 0
for val in product(a, repeat=5):
    val = ''.join(val)
    if val[0] != '0' and val.count('7') == 1 and val.count('9') + val.count('A') + val.count('B') <= 3:
        cnt += 1

print(cnt)