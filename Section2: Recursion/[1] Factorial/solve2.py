#Improve Solution (Solution 2 Iteration or While loop)
def fact(n):
    result = 1
    while n != 0:
        result *= n
        n -= 1
    return result

N = int(input())
print(fact(N))

## Excution in terminal to see the result
    # -  python solve2.py < 1.in > 1.out
    # -  python solve2.py < 2.in > 2.out
    # -  python solve2.py < 3.in > 3.out