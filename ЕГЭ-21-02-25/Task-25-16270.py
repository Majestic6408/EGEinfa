from fnmatch import fnmatch

for i in range(1203450670890 - 1203450670890 % 206, 10 ** 13, 206):
    if fnmatch(str(i), '12?345?67089?'):
        print(i, i // 206)