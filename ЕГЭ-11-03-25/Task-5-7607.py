def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]
ans = []
for N in range(1, 10000):
    R = convert(N, 2)
    if N % 3 == 0:
        R = R + R[-3:]
    else:
        ostat = N % 3
        ostat = ostat * 3
        ostat = convert(ostat, 2)
        R = R + str(ostat)
    R = int(R, 2)
    if R > 76:
        ans.append(N)

print(min(ans))