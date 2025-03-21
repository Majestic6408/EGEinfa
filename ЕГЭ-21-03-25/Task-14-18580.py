from string import ascii_uppercase, digits

a = ascii_uppercase + digits

a = a[:25]
for x in a:
    st1 = int('A4' + x + '7F2', 25)
    st2 = int('N' + x + 'G5' + x + 'H', 25)
    st3 = int('74' + x + 'M26', 25)
    summ = st1 + st2 + st3
    if summ % 24 == 0:
        print(summ // 24)