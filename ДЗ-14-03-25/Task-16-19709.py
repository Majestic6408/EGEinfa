import sys
sys.setrecursionlimit(2030)

def f(n):
    if n == 1:
        return 1
    if n > 1:
        return n ** 3 + f(n - 1)

print(f(2025) - f(2022))