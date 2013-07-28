# Name: yummy.bian@gmail.com
# Login:
# TA:
# Section:
# Q1.


def smooth(f, dx):
    """Returns the smoothed version of f, g where

    g(x) = (f(x - dx) + f(x) + f(x + dx)) / 3

    >>> square = lambda x: x ** 2
    >>> round(smooth(square, 1)(0), 3)
    0.667
    """
    return lambda x: (f(x - dx) + f(x) + f(x + dx)) / 3

def compose1(f, g):
    """Return a function h, such that h(x) = f(g(x))."""
    return lambda x: f(g(x))

def repeated(f, n):
    """Return the function that computes the nth application of f.

    f -- a function that takes one argument
    n -- a positive integer
    """
    "*** YOUR CODE HERE ***"
    rep_fun = lambda x: x
    while n > 0:
        n, rep_fun = n-1, compose1(f, rep_fun)
    return rep_fun

def n_fold_smooth(f, dx, n):
    """Returns the n-fold smoothed version of f

    >>> square = lambda x: x ** 2
    >>> round(n_fold_smooth(square, 1, 3)(0), 3)
    2.0
    """
    # def wrapper(x): 
    #     def g(x):
    #         return (f(x-dx) + f(x) + f(x+dx)) / 3
    #     ret = g(x)
    #     for i in range(1, n):
    #         ret = g(ret)
    #     return ret
    # return wrapper

    # fun = smooth(f, dx)
    # return repeated(fun, n)

    smooth_with_dx = lambda g: smooth(g, dx)
    return repeated(smooth_with_dx, n)(f)

    
# Q2.

def iterative_continued_frac(n_term, d_term, k):
    """Returns the k-term continued fraction with numerators defined by n_term
    and denominators defined by d_term.

    >>> # golden ratio
    ... round(iterative_continued_frac(lambda x: 1, lambda x: 1, 8), 3)
    0.618
    >>> # 1 / (1 + (2 / (2 + (3 / (3 + (4 / 4))))))
    ... round(iterative_continued_frac(lambda x: x, lambda x: x, 4), 6)
    0.578947
    """
    "*** YOUR CODE HERE ***"
    ret = 0
    for i in range(k, 0, -1):
        ret =  n_term(i) / (d_term(i) + ret)
    return ret


def recursive_continued_frac(n_term, d_term, k):
    """Returns the k-term continued fraction with numerators defined by n_term
    and denominators defined by d_term.

    >>> # golden ratio
    ... round(recursive_continued_frac(lambda x: 1, lambda x: 1, 8), 3)
    0.618
    >>> # 1 / (1 + (2 / (2 + (3 / (3 + (4 / 4))))))
    ... round(recursive_continued_frac(lambda x: x, lambda x: x, 4), 6)
    0.578947
    """
    "*** YOUR CODE HERE ***"
    def wrapper(n_term, d_term, k, ret):
        if k == 0:
            return ret
        return wrapper(n_term, d_term, k-1, 
                        n_term(k)/(d_term(k)+ret))
    return wrapper(n_term, d_term, k, 0)


# Q3.

def g(n):
    """Return the value of G(n), computed recursively.

    >>> g(1)
    1
    >>> g(2)
    2
    >>> g(3)
    3
    >>> g(4)
    10
    >>> g(5)
    22
    """
    "*** YOUR CODE HERE ***"
    if n < 4:
        return n
    return g(n - 1) * 1 + g(n - 2) * 2 + g(n - 3) * 3


def g_iter(n):
    """Return the value of G(n), computed iteratively.
    >>> g_iter(1)
    1
    >>> g_iter(2)
    2
    >>> g_iter(3)
    3
    >>> g_iter(4)
    10
    >>> g_iter(5)
    22
    """
    "*** YOUR CODE HERE ***"
    if n < 4:
        return n
    a1, a2, a3 = 1, 2, 3
    ret = 0
    for i in range(4, n+1):
        ret = a1*3 + a2*2 + a3*1
        a1, a2, a3 = a2, a3, ret 
    return ret
        

# Q4.

from operator import sub, mul

def make_anonymous_factorial():
    """Return the value of an expression that computes factorial.

    >>> make_anonymous_factorial()(5)
    120
    """
    return lambda n: 1 if n <= 1 else \
                        mul(n, make_anonymous_factorial()(sub(n, 1)))

if __name__ == '__main__':
    from doctest import run_docstring_examples
    run_docstring_examples(smooth, globals(), True)
    run_docstring_examples(n_fold_smooth, globals(), True)
    run_docstring_examples(iterative_continued_frac, globals(), True)
    run_docstring_examples(recursive_continued_frac, globals(), True)
    run_docstring_examples(g, globals(), True)
    run_docstring_examples(g_iter, globals(), True)
    run_docstring_examples(make_anonymous_factorial, globals(), True)
