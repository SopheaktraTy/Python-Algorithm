def solve(n):
    cnt = 0
    sqrtn = int(n ** 0.5)
    for i in range (1, sqrtn + 1 ):
        if n % i == 0:
            cnt += 2
    if sqrtn*sqrtn == n:
        cnt -= 1
    return cnt

N = int(input())

import time
start = time.time()
print(solve(N))
end = time.time()
print(f' slove() elapsed time: {end - start}')

## Excution in terminal to see the result
    # -  python solve1.py < 1.in > 1.out
    # -  python solve1.py < 2.in > 2.out
    # -  python solve1.py < 3.in > 3.out
    # -  python solve1.py < 4.in > 4.out