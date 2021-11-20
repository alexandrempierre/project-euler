#!/usr/bin/env python3

'''main module
'''


__all__ = []
__author__ = 'Alexandre Pierre'


from projecteuler import sieve


def quadratic_formula(coeff_a, coeff_b):
    '''Returns the quadratic formula with a and b as coefficients.'''
    return lambda n: n**2 + coeff_a * n + coeff_b


def quadratic_primes_count(coeff_a, coeff_b, primes_set):
    '''Returns the count of sequential prime results.'''
    quad = quadratic_formula(coeff_a, coeff_b)
    count_results, input_n = 0, 0
    while quad(input_n) in primes_set:
        count_results += 1
        input_n += 1

    return count_results

if __name__ == '__main__':
    primes = set(sieve.eratosthenes(4_000_000))
    count = -1
    for a in range(-999, 1_000):
        for b in range(-1_000, 1_000):
            curr_count = quadratic_primes_count(a, b, primes)
            if curr_count > count:
                count = curr_count
                coeffs_product = a * b

    print(coeffs_product)
