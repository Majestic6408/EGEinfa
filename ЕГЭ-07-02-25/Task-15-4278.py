def f(A):
    for x in range(1, 1000):
            f = (A % 12 == 0) and ((530 % x == 0) <= ((A % x != 0) <= (170 % x != 0)))
            if not f:
                return 0
    return 1

cnt = 0
for A in range(1, 1001):
    if f(A):
        cnt += 1

print(cnt)