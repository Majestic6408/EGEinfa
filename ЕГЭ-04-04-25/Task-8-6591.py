from itertools import product

a = '0123456789'
cnt = 0
for val in product(a[:7], repeat=5):
    val = ''.join(val)
    if val[0] != '0' and val.count('6') == 1:
        summ1 = 0
        summ2 = 0
        for j in val:
            if int(j) % 2 == 0:
                summ1 += int(j)
        for k in val:
            if int(k) % 2 != 0:
                summ2 += int(k)
        if summ1 < summ2:
            cnt += 1

print(cnt)
