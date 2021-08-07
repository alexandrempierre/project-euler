#!/usr/bin/env python3

def fibonacci():
    f0, f = 1, 1
    while True:
        yield f
        f0, f = f, f0 + f

def even_fibonacci():
    fibo = fibonacci()
    for f in fibo:
        if f % 2 == 0:
            yield f

def main():
    upper_limit = 4_000_000
    even_fibo = even_fibonacci()
    s = sum(f if f <= upper_limit else [even_fibo.close(), 0][1] for f in even_fibo)

    print(s)

if __name__ == "__main__":
    main()