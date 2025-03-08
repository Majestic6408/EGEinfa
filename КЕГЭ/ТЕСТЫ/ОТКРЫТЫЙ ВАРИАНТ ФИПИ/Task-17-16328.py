with open('17_16328.txt') as file:
    data = [int(i) for i in file]

minn = min(i for i in data if i % 19 == 0)

ans = []
for num1, num2 in zip(data, data[1:]):
     summ = num1 + num2

     u1 = num1 % minn == 0
     u2 = num2 % minn == 0

     f1 = u1 + u2 >= 1

     if f1:
         ans.append(summ)

print(len(ans), max(ans))