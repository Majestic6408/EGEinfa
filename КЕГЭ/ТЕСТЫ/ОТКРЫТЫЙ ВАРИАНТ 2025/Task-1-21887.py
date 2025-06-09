from itertools import permutations

graph = 'FG GC CE GE AE AD DB DF FB'.split()

matrix = '234 136 12 157 467 25 45'.split()

print(*range(1, 8))
for i in permutations('ABCDEFG'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i)