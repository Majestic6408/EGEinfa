from string import digits, ascii_uppercase

alph = digits + ascii_uppercase

for x in alph[:24]:
    res1 = int('11353' + x + '12', 25)
    res2 = int('135' + x + '21', 25)
    res = res1 + res2
    if res % 24 == 0:
        print(res // 24)