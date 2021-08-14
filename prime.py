from functools import lru_cache

n = int(input("Maximum prime?"))

@lru_cache(maxsize=3000)
def get_primes(n):
    numbers = set(range(n, 1, -1))
    primes = []
    while numbers:
        p = numbers.pop()
        primes.append(p)
        numbers.difference_update(set(range(p*2, n+1, p)))
    return primes[-100:-1]
    
print(get_primes(n))