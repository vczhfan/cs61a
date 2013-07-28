from math import sqrt

def is_prime(n):
    k = 2
    while k < n:
        if n % k == 0:
            return False
        k += 1
    return True

def is_prime2(n):
    k = 2
    while k < sqrt(n):
        if n % k == 0:
            return False
        k += 1
    return True

def nth_prime(n):
    nth, i = 1, 2

    while nth < (n+1):
        if is_prime2(i):
            if nth == n:
                return i
            else:
                nth += 1
        i += 1

def nth_prime2(n):
    cnt, curr = 1, 2
    while cnt < n:
        curr += 1
        if is_prime2(curr):
            cnt += 1
    return curr

def print_primes(n):
    for i in range(1, n+1):
        print (nth_prime(i))

def nth_fibo(n):
    cnt, curr, next = 1, 0, 1
    while cnt < n:
        curr, next, cnt = next, curr + next, cnt + 1
    return curr

def square(i):
    return pow(i, 2)

def double(i):
    return (i*2)

def every(func, n):
    i = 1
    while i <= n:
        print (func(i))
        i += 1

def square_every_number(n):
    every(square, n)

def double_every_number(n):
    every(double, n)

def keep(cond, n):
    i = 1
    while i <= n:
        if cond(i):
            print(i)
        i += 1

def and_add_one(f):
    def f_wrapper(x):
        return f(x) + 1
    return f_wrapper

def and_add(f, n):
    def f_wrapper(x):
        return f(x) + n
    return f_wrapper

def identity(x):
    return x
    
def lazy_accumulate(f, start, n, term):
    """
    A function (call it h) h(m) where m is the number of
    additional values to combine.
    >>> # The following does
    >>> # (1 + 2 + 3 + 4 + 5) + (6 + 7 + 8 + 9 + 10)
    >>> lazy_accumulate(add, 0, 5, identity)(5)
    55
    """
    def second_accumulate(m):
        return lazy_accumulate(f, start, n+m, term)
    return second_accumulate 

if __name__ == '__main__':
    # print_primes(10)
    # print (nth_fibo(10))
    # square_every_number(10)

