def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]

def f(st, end):
    st = convert(st, 2)
    end = convert(end, 2)
    if st > end:
        return 0
    if st == end:
        return 1
    return f(st + 1, end) + f(int(st + '0'), end) + f(int(st + '1'), end)

print(f(100, 11101))