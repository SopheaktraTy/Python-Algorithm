# The python code to solve the problem is implemented as follows.
def solve(N):
    s = 0
    for i in range(1, N + 1):
        s += i
    return s

N = int(input())
print(solve(N))

## Excution in terminal to see the result
    # -  python solve1.py < 1.in > 1.out
    # -  python solve1.py < 2.in > 2.out
    # -  python solve1.py < 3.in > 3.out