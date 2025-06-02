from itertools import permutations

matrix = '23 168 158 578 347 27 456 234'.split()
graph = 'EA ED DF AF FC CG GH EH HB GB BG'.split()

print(*range(1, 9))
for i in permutations('ABCDEFGH'):
   if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
       print(*i)