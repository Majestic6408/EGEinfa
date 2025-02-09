def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]

def count_evens(num):
    evens = sum([1 for i in num if int(i, 8) % 2 == 0])
    return evens

for N in range(1, 10000):
    R = convert(N, 8)
    evens = sum([1 for i in R if int(i , 8) % 2 == 0])
    if count_evens(R) % 2:
        R = R[-3:] + '46'
    else:
        R = f'{(N % 8 * 5): o}' + R
    R = int(R, 8)
    if N == R:
        print(N)
        break