from fnmatch import fnmatch

for i in range(2023, 10 ** 10, 2023):
    if fnmatch(str(i), '1?1?1?1*1'):
        if i % 2023 == 0 and sum(map(int, str(i))) == 22:
            print(i)