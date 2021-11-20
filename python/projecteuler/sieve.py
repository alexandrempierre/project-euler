'''sieve module

Sieve methods.
'''


__all__ = ['eratosthenes']
__author__ = 'Alexandre Pierre'


import pair


def eratosthenes(n):
    '''Sieve of eratosthenes to find all primes up to (inclusive) a number n'''
    is_prime = [False, False] + [True] * (n - 1)
    for m, prime in enumerate(is_prime):
        if prime:
            is_prime[m*m::m] = [False] * ((n - m * m) // m + 1)
    
    return map(pair.first, filter(pair.second, enumerate(is_prime)))