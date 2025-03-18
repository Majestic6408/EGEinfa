from string import ascii_uppercase, digits

a = digits + ascii_uppercase
for x in a[:25]:
    num1 = int('11353' + x + '12', 25)
    num2 = int('135' + x + '21', 25)
    summ = num1 + num2
    if summ % 24 == 0:
        print(summ // 24)