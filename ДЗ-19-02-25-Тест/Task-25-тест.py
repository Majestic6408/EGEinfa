from fnmatch import fnmatch

for i in range(125670 - 125670 % 7777, 10 ** 10, 7777):
    if fnmatch(str(i), '12*567?'):
        if i % 7777 == 0:
            print(i, i // 7777)
from itertools import product

ans = []
for r in range(6):
    for z in product('0123456789', repeat=r):
        z = ''.join(z)
        for v in '0123456789':

            num = int(f'12{z}567{v}')

            if num <= 10 ** 10 and num % 7777 == 0:
                ans.append([num, num // 7777])

ans = set(sorted(ans))
for i in ans:
    print(*i)