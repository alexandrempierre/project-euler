'''sieve module

Sieve methods.
'''


__all__ = ['eratosthenes']
__author__ = 'Alexandre Pierre'


import pair


def eratosthenes(upper_limit):
    '''Sieve of eratosthenes to find all primes up to (inclusive) a number n'''
    is_prime = [False, False] + [True] * (upper_limit - 1)
    for num, prime in enumerate(is_prime):
        if prime:
            is_prime[num*num::num] = (
                [False] * ((upper_limit - num * num) // num + 1))

    return map(pair.first, filter(pair.second, enumerate(is_prime)))
