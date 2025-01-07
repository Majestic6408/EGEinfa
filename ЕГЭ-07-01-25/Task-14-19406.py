from string import digits, ascii_uppercase

a = digits + ascii_uppercase

for x in a[1:35]:
    num1 = int('6' + x + 'qr' + x, 35)
    num2 = int(f'{x}59sh', 35)
    num3 = int(f'ph{x}69yw', 35)
    num = num1 + num2 + num3
    maxx = 0
    let = 0
    for i in digits:
        if str(num).count(i) >= maxx:
            maxx = str(num).count(i)
            let = int(i)
    if num % let ** 2 == 0:
        print(num // let ** 2)