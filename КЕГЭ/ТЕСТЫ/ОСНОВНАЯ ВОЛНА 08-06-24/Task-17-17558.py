with open('17_17558.txt') as file:
    data = [int(i) for i in file]

chisl = sum(1 for i in data if abs(i) % 32 == 0)
ans = []
for num1 ,num2 in zip(data, data[1:]):
    summ = num1 + num2

    u1 = num1 < 0
    u2 = num2 < 0
    f1 = u1 + u2 >= 1
    f2 = summ < chisl
    if f1 and f2:
        ans.append(summ)

print(len(ans), max(ans))