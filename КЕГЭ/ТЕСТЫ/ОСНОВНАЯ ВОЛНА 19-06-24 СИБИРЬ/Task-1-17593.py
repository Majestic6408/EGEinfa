from itertools import permutations

graph = 'CG GD CD AC DB AB BF FE AE'.split()

matrix = '36 567 14 367 27 124 245'.split()

print(*range(1, 8))
for i in permutations('ABCDEFG'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i)