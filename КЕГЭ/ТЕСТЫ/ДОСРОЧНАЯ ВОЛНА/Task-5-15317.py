def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]

ans = []
for N in range(1, 1000000):
    R = convert(N, 2)
    if N % 2 == 0:
        R = R + '01'
    else:
        R = '1' + R + '1'
    R = int(R, 2)
    if R > 156:
        ans.append(N)

print(min(ans))