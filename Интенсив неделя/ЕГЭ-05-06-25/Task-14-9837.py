from string import digits, ascii_uppercase

a = digits + ascii_uppercase

for x in a[:23]:
    s1 = int('7' + x + '38596', 23)
    s2 = int('14' + x + '36', 23)
    s3 = int('61' + x + '7', 23)
    st = s1 + s2 + s3
    if st % 22 == 0:
        print(st // 22)