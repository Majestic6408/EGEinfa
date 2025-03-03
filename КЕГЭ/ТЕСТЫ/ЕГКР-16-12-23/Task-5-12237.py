def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]

ans = []
for N in range(1, 100000):
    R = convert(N, 2)
    if N % 2 == 0:
        R = R + R[-2:]
    else:
        R = '1' + R + '0'
    R = int(R, 2)
    if R < 100:
        ans.append(N)

print(max(ans))