def solve(n):
    cnt = 0
    for i in range(1, n + 1):
        if n % i == 0:
            cnt += 1
    return cnt

N = int(input())

import time
start = time.time()
print(solve(N))
end = time.time()
print(f' slove() elapsed time: {end - start}')

## Excution in terminal to see the result
    # -  python solve.py < 1.in > 1.out
    # -  python solve.py < 2.in > 2.out
    # -  python solve.py < 3.in > 3.out
    # -  python solve.py < 4.in > 4.out