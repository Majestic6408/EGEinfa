def f(st, end, cnt=0):
    if st > end:
        return 0
    if st == end and cnt == 51:
        return 1
    return f(st * 4, end, cnt + 1) + f(st + 1, end, cnt + 1) + f(st * 3, end, cnt + 1)


print(f(2, 404))