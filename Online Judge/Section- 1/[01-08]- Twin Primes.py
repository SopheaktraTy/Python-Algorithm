def twin_prime(limit):
    previous_prime = 3
    count = 0
    for candidate in range(5, limit + 1):
        if is_prime(candidate):
            if candidate - 2 == previous_prime:
                print(previous_prime, candidate)
                count += 1
                previous_prime = candidate
    print(count)

def is_prime(number):
    for divisor in range(2, int(number ** 0.5) + 1):
        if number % divisor == 0:
            return False
    return True

twin_prime(10)
