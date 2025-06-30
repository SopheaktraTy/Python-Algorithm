def perm(i, n, s):
    if i == n - 1:
        print("".join(s))
    else:
        for j in range(i, n):
            # swap s[i] and s[j]
            s[i], s[j] = s[j], s[i]
            perm(i + 1, n, s)
            # swap back to restore original order
            s[i], s[j] = s[j], s[i]

N = int(input())
S = [chr(ord('A') + i) for i in range(N)]
perm(0, N, S)

## Excution in terminal to see the result
    # -  python solve.py < 1.in > 1.out
    # -  python solve.py < 2.in > 2.out
    # -  python solve.py < 3.in > 3.out