import sys
sys.setrecursionlimit(3013)
def f(n):
    if n < 13:
        return 13
    if n >= 13 and n % 5 != 0:
        return 13 - f(n - 1)
    return 13 + f(n - 1)

print(f(3013))