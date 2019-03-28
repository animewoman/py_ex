
def eratosthenes(n=100):
    sieve = list(range(n+1))
    sieve[1] = 0
    prime_numbers = [1]
    for i in sieve:
        if i > 1:
            prime_numbers.append(i)
            for j in range(i + i, len(sieve), i):
                sieve[j] = 0
    return prime_numbers

