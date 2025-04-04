def f1(nums):
    cnt = [nums.count(i) for i in nums]
    return cnt.count(3) == 3 and cnt.count(1) == 4

def f2(nums):
    ans = []
    ans1 = []
    for i in nums:
        if nums.count(i) == 1:
            ans.append(i)
        if nums.count(i) > 1:
            ans1.append(i)
    summ1 = sum(map(int, ans)) / len(ans)
    summ2 = sum(map(int, ans1)) / len(ans1)
    if summ1 <= summ2:
        return 1
    return 0

with open('9_9740.txt') as file:
    data = [list(map(int, i.split())) for i in file]

cnt = 0
for i in data:
    if f1(i) and f2(i):
        cnt += 1
print(cnt)
