with open('17_21903.txt') as file:
    data = [int(i) for i in file]

minn = min(i for i in data if str(i)[-2:] == '15' and len(str(abs(i))) == 3)
minn = minn ** 2

ans = []
for num1, num2, num3 in zip(data, data[1:], data[2:]):
    numbers = (num1, num2, num3)
    summ = min(numbers) * max(numbers)

    u1 = num1 < 0 and num2 < 0 and num3 < 0
    u2 = num1 > 0 and num2 > 0 and num3 > 0
    f1 = u1 + u2 == 1
    f2 = (min(numbers) * max(numbers)) > minn
    if f1 and f2:
        ans.append(summ)

print(len(ans), min(ans))