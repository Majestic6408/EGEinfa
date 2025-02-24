def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]

from itertools import product

ans = []
for r in range(2):
    for z in product('0123456789', repeat=r):
        z = ''.join(z)
        for v in '123456789':

            num1 = int(f'{v}213{z}5664')
            if num1 <= 10 ** 9:
                num1 = convert(num1, 7)
                delit = convert(333, 7)
                if int(num1) % int(delit) == 0:
                    ans.append([num1, num1 // delit])


ans = sorted(ans)
for i in ans:
    print(*i)
