from fnmatch import fnmatch

for i in range(9231, 10 ** 10, 9231):
    for j in range(6):
        if fnmatch(str(i), f'{'[02468]' * j}12[13579]4[13579]'):
            print(i, i // 9231)