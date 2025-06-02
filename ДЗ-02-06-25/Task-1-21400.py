from itertools import permutations

matrix = '457 567 45 136 123 247 126'.split()
graph = 'EG GB BC EC EF AF AB AD FD CD'.split()

print(*range(1, 8))
for i in permutations('ABCDEFG'):
   if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
       print(*i)