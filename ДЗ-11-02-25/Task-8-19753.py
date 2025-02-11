from itertools import permutations
from string import digits, ascii_uppercase

a = digits + ascii_uppercase
a= a[:10]
cnt = 0
for val in permutations(a, 6):
    val = ''.join(val)
    if val[0] != '0' and int(val) % 4 == 0 and len(set(val)) == 6:
        for i in '02468':
            val = val.replace(i, '*', 1)
        if '**' not in val:
            cnt += 1

print(cnt)