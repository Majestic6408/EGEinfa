with open('17_21416.txt') as file:
    data = [int(i) for i in file]

summ = sum(i for i in data if i < 0)

ans = []

for num1, num2, num3 in zip(data, data[1:], data[2:]):
    numbers = (num1, num2, num3)

    f1 = (max(numbers) * min(numbers)) > summ
    if f1:
        ans.append(sum(numbers))
print(len(ans), max(ans))