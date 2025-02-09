import sys
sys.setrecursionlimit(2025)
def f(n):
    if n < 4:
        return 1
    return f(n - 1) + n * 2

print(f(2025))

