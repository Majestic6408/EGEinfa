from itertools import permutations

graph = 'BE BD ED DG BC EH CH HF GF AF AG'.split()

matrix = '234 157 147 138 268 58 23 456'.split()

print(*range(1, 9))
for i in permutations('ABCDEFGH'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i)