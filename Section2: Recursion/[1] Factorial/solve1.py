#Create solution (Solution 1 Recursion)
def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)

import sys
sys.setrecursionlimit(10**5)

N = int(input())
print(fact(N))

## Excution in terminal to see the result
    # -  python solve1.py < 1.in > 1.out
    # -  python solve1.py < 2.in > 2.out
    # -  python solve1.py < 3.in > 3.out