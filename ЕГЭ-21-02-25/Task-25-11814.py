from fnmatch import fnmatch

for i in range(2100045 - 2100045 % 1777, 10 ** 10, 1777):
    if fnmatch(str(i), '21???68?79'):
        print(i, i // 1777)