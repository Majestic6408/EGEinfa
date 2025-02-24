from fnmatch import fnmatch

for i in range(157424 - 157424 % 111, 10 ** 8, 111):
    if fnmatch(str(i), '*15*7424'):
        print(i, i // 111)

for i in range(157424 - 157424 % 113, 10 ** 8, 111):
    if fnmatch(str(i), '*15*7424'):
        print(i, i // 113)


for i in range(157424 - 157424 % 127, 10 ** 8, 111):
    if fnmatch(str(i), '*15*7424'):
        print(i, i // 127)