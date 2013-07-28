def sum(n):
	if n == 0:
		return 0
	return n + sum(n-1)


def ab_plus_c(a, b, c):
	if a == 0:
		return c
	return b + ab_plus_c(a-1, b ,c)

def summation(n, term):
	if n == 0:
		return term(0)
	return term(n) + summation(n-1, term)

def hailstone(n):
    """Print the hailstone sequence starting at n and return its length.

    >>> a = hailstone(10)  # Seven elements are 10, 5, 16, 8, 4, 2, 1
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    print (n)
    if n == 1:
        return 1
    elif n % 2 == 0:
        return 1 + hailstone(n//2)
    else:
        return 1 + hailstone(3*n+1)

def square(x):
    """Return x squared."""
    return x * x

def repeated(f, n):
    """Return the function that computes the nth application of f.

    f -- a function that takes one argument
    n -- a positive integer

    >>> repeated(square, 2)(2)
    16
    >>> repeated(square, 2)(5)
    625
    >>> repeated(square, 4)(5)
    152587890625
    """
    "*** YOUR CODE HERE ***"
    if n == 0:
        return lambda x: x
    else:
        return compose1(f, repeated(f, n-1))

def compose1(f, g):
    """Return a function h, such that h(x) = f(g(x))."""
    return lambda x: f(g(x))

f1 = 8
f2 = lambda: 8
f3 = lambda x: x
f4 = lambda: lambda: 8
f5 = lambda: lambda x: lambda: 8
f6 = lambda: lambda x: lambda: x

def curry2(f):
    return lambda x: lambda y: f(x, y)

def divide(x, y):
    return x / y

def inverse_curry2(f):
    return lambda x, y: f(x)(y)

def falling(n, k):
    ret = 1
    while k > 0:
        ret, n, k = ret*n, n-1, k-1
    return ret

if __name__ == '__main__':
    from doctest import run_docstring_examples
    run_docstring_examples(hailstone, globals(), True)
    run_docstring_examples(repeated, globals(), True)
    print (inverse_curry2(curry2(divide))(4, 2))
    print (falling(10, 3))

