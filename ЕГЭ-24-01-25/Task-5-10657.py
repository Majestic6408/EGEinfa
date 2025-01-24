def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]

ans = []
for N in range(1, 10000):
    R = convert(N, 3)
    if sum(map(int, R)) % 3 == 0:
        R = '20' + R
    else:
        R = '10' + R
    if int(R, 3) < 100:
        ans.append(N)

print(max(ans))