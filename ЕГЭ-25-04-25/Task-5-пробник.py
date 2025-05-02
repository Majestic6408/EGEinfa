def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]

for N in range(5, 100000):
    R = convert(N, 2)
    if R.count('1') > R.count('0'):
        R = R + '0'
    else:
        R = R + '1'
    if len(R) % 2 == 0:
        R = R[:len(R) // 2 - 1] + R[len(R) // 2 + 1:]
    else:
        R = R[:len(R) // 2 - 1] + R[len(R) // 2 + 2:]
    R = int(R, 2)
    if R == 55:
        print(N)
