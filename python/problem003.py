#!/usr/bin/env python3

def reversed_eratosthenes(n, eps=None):
    greatest_factor_candidate = int(n**.5)
    
    is_prime = [True]*(greatest_factor_candidate+1)
    is_prime[0] = False ; is_prime[1] = False
    
    for i,prime in enumerate(is_prime):
        if prime:
            start, stop, step = i*i, greatest_factor_candidate+1, i
            is_prime[start:stop:step] = tuple(False for _ in range(start, stop, step))

    return (i for i in range(greatest_factor_candidate,-1,-1) if is_prime[i])

def largest_factor(n):
    prime_factor_candidates = reversed_eratosthenes(n)

    for p in prime_factor_candidates:
        if n % p == 0:
            return p
    
    return 1

def main():
    n = 600_851_475_143
    print( largest_factor(n) )

if __name__ == "__main__":
    main()