from string import digits, ascii_uppercase

a = ascii_uppercase + digits
for x in a[:19]:
    st1 = int('98897' + x + '21', 19)
    st2 = int('2' + x + '923', 19)
    st = st1 + st2
    if st % 18 == 0:
        print(st // 18)