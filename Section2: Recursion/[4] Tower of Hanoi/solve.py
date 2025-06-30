def hanoi(n, src, via, dst):
    if n == 1:
        print(f"{src} -> {dst}")
    else:
        hanoi(n - 1, src, dst, via)
        hanoi(1,     src, via, dst)
        hanoi(n - 1, via, src, dst)

N = int(input())
hanoi(N, "A", "B", "C")

## Excution in terminal to see the result
    # -  python solve.py < 1.in > 1.out
    # -  python solve.py < 2.in > 2.out
    # -  python solve.py < 3.in > 3.out