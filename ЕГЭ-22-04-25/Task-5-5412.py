from string import digits, ascii_uppercase

a = digits + ascii_uppercase
a = a[:16]
cnt = 0
def convert(num, sys):
    res = ''
    while num:
        res += a[num % sys]
        num //= sys
    return res[::-1]

for N in range(1, 100000):
    R = convert(N, 16)
    if R.count('B') % 2 == 0:
        R = '1' + R
    else:
        R = R + '1'
    R = int(R, 16)
    R = str(R)
    if len(R) == 2:
        cnt += 1


print(cnt)
