def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]

ans = []
for N in range(1, 10000):
    R = convert(N, 2)
    summ = sum(map(int, R)) % 2
    R = R + str(summ)
    ostat = sum(map(int, R)) % 2
    R = R + str(ostat)
    R = int(R, 2)
    if R > 253:
        ans.append(N)

print(min(ans))