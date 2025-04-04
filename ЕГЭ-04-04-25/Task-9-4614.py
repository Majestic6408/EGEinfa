def f1(nums):
    return max(nums) < sum(nums) - max(nums)

def f2(nums):
    cnt = [nums.count(i) for i in nums]
    return cnt.count(2) == 2 and cnt.count(1) == 2

with open('9_4614.txt') as file:
    data = [list(map(int, i.split())) for i in file]

cnt = 0
for i in data:
    if f1(i) and f2(i):
        cnt += 1
print(cnt)