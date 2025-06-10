def solve(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

N = int(input())
print("YES" if solve(N) else "NO")

## Excution in terminal to see the result
    # -  python solve2.py < 1.in > 1.out
    # -  python solve2.py < 2.in > 2.out
    # -  python solve2.py < 3.in > 3.out
    # -  python solve2.py < 4.in > 4.out
