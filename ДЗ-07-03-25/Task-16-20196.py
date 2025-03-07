import sys
sys.setrecursionlimit(2025)

def f(n):
    if n < 110:
        return n
    return n + f(n - 1)

print(f(2025) - f(2021))