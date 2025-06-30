def collatz(n):
    if n == 1:
        return [1]
    elif n % 2 == 0:
        return [n] + collatz(n // 2)
    else:
        return [n] + collatz(3 * n + 1)

M = int(input())
S = collatz(M)
print (len(S))
print (" ".join (map(str, S)))

## Excution in terminal to see the result
    # -  python solve.py < 1.in > 1.out
    # -  python solve.py < 2.in > 2.out
    # -  python solve.py < 3.in > 3.out