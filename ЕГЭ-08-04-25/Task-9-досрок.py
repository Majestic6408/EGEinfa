def f1(num):
    cnt = [num.count(i) for i in num]
    return cnt.count(2) == 3 and cnt.count(2) == 3 and cnt.count(1) == 1

def f2(num):
    pov = [i for i in num if num.count(i) > 1]
    nepov = [i for i in num if num.count(i) == 1]
    return max(pov) > nepov[0]

with open('9.txt') as file:
    num = [list(map(int, i.split())) for i in file]

cnt = 0
if f1 and f2:
    cnt += 1

print(cnt)