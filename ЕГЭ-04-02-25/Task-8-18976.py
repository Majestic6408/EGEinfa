from string import digits, ascii_uppercase
from itertools import product

a = digits + ascii_uppercase
cnt_1 = 0
cnt_2 = 0
num1 = ''
for val in product(a[:20], repeat=5):
    val = ''.join(val)
    if int(val[0], 20) + int(val[-1], 20) == 26 and val[0] != '0':
        if int(val[0], 20) % 2 == 0 and int(val[1], 20) % 2 != 0 \
                and int(val[2], 20) % 2 == 0 and int(val[3], 20) % 2 != 0 and int(val[4], 20) % 2 == 0:
            cnt_1 += 1
        if int(val[0], 20) % 2 != 0 and int(val[1], 20) % 2 == 0 \
                and int(val[2], 20) % 2 != 0 and int(val[3], 20) % 2 == 0 and int(val[4], 20) % 2 != 0:
            cnt_2 += 1

cnt = cnt_1 + cnt_2
print(cnt)
