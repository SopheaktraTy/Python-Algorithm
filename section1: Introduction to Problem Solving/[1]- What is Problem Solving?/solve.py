
## Implement the madd() method that performs matrix addition
def madd(A, B):
    n, m = len(A), len(A[0])
    C = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            C[i][j] = A[i][j] + B[i][j]
    return C

# Implement the mprint() method for printing a matrix
def mprint(A):
    for i in range(len(A)):
        print(" ".join(map(str, A[i])))


## Implement the following code to solve problem
N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
B = [list(map(int, input().split())) for _ in range(N)]
C = madd(A, B)
print(C)

## To excution the code run
    # -  python solve.py < 1.in > 1.out
    # -  python solve.py < 2.in > 2.out