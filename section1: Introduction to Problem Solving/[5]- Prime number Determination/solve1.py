def solve(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
import time
start = time.time()
N = int(input())
print("YES" if solve(N) else "NO")
end = time.time()
print(f' slove() elapsed time: {end - start}')

## Excution in terminal to see the result
    # -  python solve1.py < 1.in > 1.out
    # -  python solve1.py < 2.in > 2.out
    # -  python solve1.py < 3.in > 3.out
    # -  python solve1.py < 4.in > 4.out
