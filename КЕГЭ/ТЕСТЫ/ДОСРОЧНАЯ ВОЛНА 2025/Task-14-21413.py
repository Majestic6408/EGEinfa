from string import digits, ascii_uppercase

a = digits + ascii_uppercase

for x in a[:21]:
    num1 = int('82934' + x + '2', 21)
    num2 = int('2924' + x + x + '7', 21)
    num3 = int('67564' + x + '8', 21)
    summ = num1 + num2 + num3
    if summ % 20 == 0:
        print(summ // 20)