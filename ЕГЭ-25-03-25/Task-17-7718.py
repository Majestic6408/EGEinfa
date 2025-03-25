from itertools import combinations

with open('17 (2)_7718.txt') as file:
    data = [int(i) for i in file]
ans = []
for num1, num2 in combinations(data, 2):
    summ = num1 + num2
    summ1 = num1 * num2

    u1 = summ % 18 == 0
    u2 = summ1 % 18 == 0
    f1 = u1 + u2 == 1
    if f1:
        ans.append(summ)

print(len(ans), max(ans))