from string import ascii_uppercase, digits

a = digits +ascii_uppercase

a = a[:12]
def convert(num, sys):
    res = ''
    while num:
        res += a[num % sys]
        num //= sys
    return res[::-1]
ans = []
for N in range(1, 1000000):
    R = convert(N, 12)
    if N % 3 == 0:
        R = '1' + R + 'B'
    else:
        R = '2' + R + '0'
    R = int(R, 12)
    if R < 1996:
        ans.append(R)

print(max(ans))
