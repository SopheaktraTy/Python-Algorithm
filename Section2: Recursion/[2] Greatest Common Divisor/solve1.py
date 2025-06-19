def gcd(n, m):
    if m == 0:
        return n
    else:
        return gcd(m, n % m)

N = int(input())
M = int(input())
print(gcd(N, M))

## Excution in terminal to see the result
    # -  python solve1.py < 1.in > 1.out
    # -  python solve1.py < 2.in > 2.out
    # -  python solve1.py < 3.in > 3.out