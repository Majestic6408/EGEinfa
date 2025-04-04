from itertools import permutations, combinations

def f1(nums):
    return max(nums) < sum(nums) - max(nums)

def f2(nums):
    for i in permutations(nums):
        if sum(i[:2]) == sum(i[2:]):
            return 1
    return 0

def f3(nums):
    for i in combinations(nums, 2):
        if sum(i) == sum(nums) - sum(i):
            return 1
    return 0

def f4(nums):
    return min(nums) + max(nums) == sum(nums) - min(nums) - max(nums)

with open('9_4589.txt') as file:
    data = [list(map(int, i.split())) for i in file]

cnt = 0
for i in data:
    if f1(i) and f3(i):
        cnt += 1
print(cnt)