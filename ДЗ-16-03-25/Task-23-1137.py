def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]

def f(st, end):
    if int(st, 2) > int(end, 2):
        return 0
    if st == end:
        return 1
    return f(bin(int(st, 2) + 1)[2:], end) + f(st + '0', end) + f(st + '1', end)

print(f('100', '11101'))