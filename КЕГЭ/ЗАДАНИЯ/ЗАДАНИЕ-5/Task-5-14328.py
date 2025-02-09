from string import digits, ascii_uppercase

a = digits + ascii_uppercase
def convert(num, sys):
    res = ''
    while num:
        res += a[num % sys]
        num //= sys
    return res[::-1]

ans = []
for N in range(1, 10000):
    R = convert(N, 12)
    if N % 3 == 0:
        R = '1' + R + 'B'
    else:
        R = '2' + R + '0'
    R = int(R, 12)
    if R < 1996:
        ans.append(R)

print(max(ans))

