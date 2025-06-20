def list_divisors(n):
    small_divs = []
    large_divs = []
    i = 1
    while i * i <= n:
        if n % i == 0:
            small_divs.append(i)
            j = n // i
            if j != i:
                large_divs.append(j)
        i += 1
    return small_divs + large_divs[::-1]

# example
n = 211224
for d in list_divisors(n):
    print(d)