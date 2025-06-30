def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        a, b = 1, 1
        for _ in range(3, n + 1):
            a, b = b, a + b
        return b

N=int(input())
print(fib(N))


## Excution in terminal to see the result
    # -  python solve1.py < 1.in > 1.out
    # -  python solve1.py < 2.in > 2.out
    # -  python solve1.py < 3.in > 3.out