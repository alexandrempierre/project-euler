#!/usr/bin/env python3

def multiples(base):
    """Generate the multiples of the base"""
    multiple = base
    while True:
        yield multiple
        multiple += base

def main():
    """Sum of multiples of 3 or 5 under 1000"""
    ceiling = 1000

    mult3 = multiples(3)
    mult5 = multiples(5)
    
    m3 = set(m if m < ceiling else [mult3.close(), 3][1] for m in mult3)
    m5 = set(m if m < ceiling else [mult5.close(), 5][1] for m in mult5)

    print(sum(m3 | m5))


if __name__ == "__main__":
    main()