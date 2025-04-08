with open('17.txt') as file:
    data = [int(i) for i in file]

summ = sum([i for i in data if i < 0])
ans = []
for num1, num2, num3 in zip(data, data[1:], data[2:]):
    ans1 = [num1, num2, num3]
    summ1 = max(ans1) * min(ans1)
    summ2 = num1 + num2 + num3

    f1 = summ1 > summ
    if f1:
        ans.append(summ2)

print(len(ans), max(ans))