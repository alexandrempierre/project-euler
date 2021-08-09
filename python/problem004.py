#!/usr/bin/env python3

def is_palindrome(n):
    number = n
    reverse = 0

    while number > 0:
        reverse = reverse * 10 + number % 10
        number //= 10
    
    return reverse == n

def largest_palindrome_product(factor_digits_number):
    largest_factor_candidate = 10**factor_digits_number - 1
    lowest_factor_candidate = 10**(factor_digits_number - 1)

    largest_palindrome_product = 0

    for i in range(largest_factor_candidate, lowest_factor_candidate-1, -1):
        for j in range(i, lowest_factor_candidate-1, -1):
            prod = i*j
            if prod > largest_palindrome_product and is_palindrome(prod):
                largest_palindrome_product = prod
            elif prod < largest_palindrome_product:
                break
        
        if i*i < largest_palindrome_product:
            break
    
    return largest_palindrome_product

def main():
    from sys import argv

    assert(len(argv) > 0)
    
    factor_digits_number = int(argv[1])
    
    lgst = largest_palindrome_product(factor_digits_number)

    print(lgst)



if __name__ == "__main__":
    main()