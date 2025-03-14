def f(st, cnt=0):
    if cnt == 13 and st < 0:
        return [st]
    if cnt == 13 and st >= 0:
        return []
    return f(st - 3,cnt + 1) + f(st * (-3), cnt + 1)

print(len(set(f(333))))