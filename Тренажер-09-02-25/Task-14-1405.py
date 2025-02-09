from string import digits, ascii_uppercase

a = digits + ascii_uppercase
for x in a[:27]:
    st1 = int('123' + x + '24', 27)
    st2 = int('135' + x + '78', 27)
    st = st1 + st2
    if st % 26 == 0:
        print(st // 26)