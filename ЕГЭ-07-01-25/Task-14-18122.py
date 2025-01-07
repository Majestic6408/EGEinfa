for x in range(1, 5556)[::-1]:
    num = 5**150 + 5**135 - x
    count_4 = 0
    while num:
        if num % 5 == 4:
            count_4 += 1
        num //= 5
    if count_4 == 134:
        print(x)
