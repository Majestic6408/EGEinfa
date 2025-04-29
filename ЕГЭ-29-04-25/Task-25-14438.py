from fnmatch import fnmatch
from math import sqrt, isqrt

for i in range(1746008 - 1746008 % 86513, 10 ** 12, 86513):
    if fnmatch(str(i), '17*46??8'):
        if sqrt(sum(map(int, str(i)))) == isqrt(sum(map(int, str(i)))):
            print(i, i // 86513)