with open('17_17530.txt') as file:
    data = [int(i) for i in file]

minn = min(i for i in data)
ans = []
for num1, num2 in zip(data, data[1:]):
    summ = num1 + num2
    ostat1 = num1 % 55
    ostat2 = num2 % 55

    u1 = ostat1 == minn
    u2 = ostat2 == minn
    f1 = u1 + u2 >= 1
    if f1:
        ans.append(summ)

print(len(ans), min(ans))