with open('17_17680.txt') as file:
    data = [int(i) for i in file]

minn = min(i for i in data if i > 0 and i % 41 == 0)

ans = []
for num1, num2 in zip(data, data[1:]):
    summ = num1 + num2

    f1 = num1 != num2
    f2 = abs(num1 - num2) % minn == 0
    if f1 and f2:
        ans.append(summ)

print(len(ans), max(ans))