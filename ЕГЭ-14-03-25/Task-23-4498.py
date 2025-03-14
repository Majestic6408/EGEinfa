def f(st, end, cnt1=0, cnt2=0, cnt3=0):
    if st > end:
        return 0
    if st == end and cnt1 <= 4 and cnt2 >= 2 and cnt3 == 5:
        return 1
    return f(st * 5, end, cnt1 + 1, cnt2, cnt3) + f(st * 3, end, cnt1, cnt2 + 1, cnt3) + f(st + 45, end, cnt1 ,cnt2, cnt3 + 1)

print(f(1, 2970))