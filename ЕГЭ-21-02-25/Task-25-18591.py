from fnmatch import fnmatch

for i in range(923231 - 923231 % 1984, 10 ** 10, 1984):
    if fnmatch(str(i), '[02468]9?23?*23[13579][02468]'):
        print(i, i // 1984)