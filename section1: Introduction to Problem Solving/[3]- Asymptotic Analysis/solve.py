def solve(N, S):
    maxn, maxi = S[0], 0
    for i in range(1, N):
        if maxn < S[i]:
            maxn, maxi = S[i], i
    return maxn, maxi

N = int(input())
S = list(map(int, input().split()))
maxn, maxi = solve(N, S)
print(maxn, maxi)


## Excution in terminal to see the result
    # -  python solve.py < 1.in > 1.out
    # -  python solve.py < 2.in > 2.out
    # -  python solve.py < 3.in > 3.out