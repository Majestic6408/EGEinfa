def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]

ans = []
for N in range(1, 100000):
    R = convert(N, 3)
    if N % 3 == 0:
        R = R + R[-2:]
    else:
        summ = sum(map(int, R))
        summ = convert(summ, 3)
        R = R + summ
    R = int(R, 3)
    if R > 220 and R % 2 == 0:
        ans.append(R)

print(min(ans))