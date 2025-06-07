with open('17_17873.txt') as file:
    data = [int(i) for i in file]

minn = min(i for i in data)

ans = []
for num1, num2 in zip(data, data[1:]):
    summ = num1 + num2

    u1 = num1 % 16 == minn
    u2 = num2 % 16 == minn
    f1 = u1 + u2 >= 1
    if f1:
        ans.append(summ)

print(len(ans), max(ans))