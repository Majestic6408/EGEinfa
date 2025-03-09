def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]

ans = []
for N in range(1, 100000):
    R = convert(N, 2)
    summ = sum(map(int, R))
    if summ % 2 == 0:
        R = '10' + R[2:] + '0'
    else:
        R = '11' + R[2:] + '1'
    R = int(R, 2)
    if R > 50:
        ans.append(N)

print(min(ans))