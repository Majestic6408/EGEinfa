def f(st, end, cnt=0):
    if st % 2 == 0:
        cnt += 1
    if st > end:
        return 0
    if st == end and cnt <= 15:
        return 1
    return f(st + 2, end, cnt) + f(st + 3, end, cnt) + f(st * 2 + 1, end, cnt)

print(f(1, 55))