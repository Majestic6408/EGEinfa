from itertools import product
alph = sorted(set('QAZWSXEDCRFVTGBYHNUJMIKOLP'))
cnt = 0
for i in range(1, 7):
    for val in product(alph, repeat=i):
        val = ''.join(val)
        cnt += 1
     if val == 'FEDABC':
            print(cnt)

