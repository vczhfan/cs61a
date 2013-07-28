# Name:
# Login:
# TA:
# Section:
# Q1.

empty_rlist = None

def rlist(first, rest):
    """Construct a recursive list from its first element and the
    rest."""
    return (first, rest)

def first(s):
    """Return the first element of a recursive list s."""
    return s[0]

def rest(s):
    """Return the rest of the elements of a recursive list s."""
    return s[1]

def len_rlist(s):
    """Return the length of recursive list s."""
    length = 0
    while s != empty_rlist:
        s, length = rest(s), length + 1
    return length

def getitem_rlist(s, i):
        """Return the element at index i of recursive list s."""
        while i > 0:
            s, i = rest(s), i - 1
        return first(s)

def reverse_rlist_iterative(s):
    """Return a reversed version of a recursive list s.

    >>> primes = rlist(2, rlist(3, rlist(5, rlist(7, empty_rlist))))
    >>> reverse_rlist_iterative(primes)
    (7, (5, (3, (2, None))))
    """
    "*** YOUR CODE HERE ***"
    len = len_rlist(s)
    r = empty_rlist
    for i in range(len):
        r = rlist(getitem_rlist(s, i), r)
    return r

def reverse_rlist_recursive(s):
    """Return a reversed version of a recursive list s.

    >>> primes = rlist(2, rlist(3, rlist(5, rlist(7, empty_rlist))))
    >>> reverse = reverse_rlist_recursive(primes)
    >>> reverse(primes)
    (7, (5, (3, (2, None))))
    """
    "*** YOUR CODE HERE ***"
    cdr = (empty_rlist)
    def inner(s):
        nonlocal cdr
        if s == empty_rlist:
            return empty_rlist
        item = first(s)
        cdr = rlist(item, cdr)
        inner(rest(s))
        return cdr
    return inner


# Q2.

def interleave_recursive(s0, s1):
    """Interleave recursive lists s0 and s1 to produce a new recursive
    list.

    >>> evens = rlist(2, rlist(4, rlist(6, rlist(8, empty_rlist))))
    >>> odds = rlist(1, rlist(3, empty_rlist))
    >>> interleave_recursive(odds, evens)
    (1, (2, (3, (4, (6, (8, None))))))
    >>> interleave_recursive(evens, odds)
    (2, (1, (4, (3, (6, (8, None))))))
    >>> interleave_recursive(odds, odds)
    (1, (1, (3, (3, None))))
    """
    "*** YOUR CODE HERE ***"

def interleave_iterative(s0, s1):
    """Interleave recursive lists s0 and s1 to produce a new recursive
    list.

    >>> evens = rlist(2, rlist(4, rlist(6, rlist(8, empty_rlist))))
    >>> odds = rlist(1, rlist(3, empty_rlist))
    >>> interleave_iterative(odds, evens)
    (1, (2, (3, (4, (6, (8, None))))))
    >>> interleave_iterative(evens, odds)
    (2, (1, (4, (3, (6, (8, None))))))
    >>> interleave_iterative(odds, odds)
    (1, (1, (3, (3, None))))
    """
    "*** YOUR CODE HERE ***"
    s = empty_rlist
    s0_len = len_rlist(s0)
    s1_len = len_rlist(s1)
    if s0_len > s1_len:
        for i in range(s0_len-1, s1_len-1, -1):
            s = rlist(getitem_rlist(s0, i), s)
        for i in range(s1_len-1, -1, -1):
            s = rlist(getitem_rlist(s1, i), s)
            s = rlist(getitem_rlist(s0, i), s)
    elif s0_len < s1_len:
        for i in range(s1_len-1, s0_len-1, -1):
            s = rlist(getitem_rlist(s1, i), s)
        for i in range(s0_len-1, -1, -1):
            s = rlist(getitem_rlist(s1, i), s)
            s = rlist(getitem_rlist(s0, i), s)
    else:
        for i in range(s1_len-1, -1, -1):
            s = rlist(getitem_rlist(s1, i), s)
            s = rlist(getitem_rlist(s0, i), s)
    return s

def str_interval(x):
    """Return a string representation of interval x.

    >>> str_interval(interval(-1, 2))
    '-1 to 2'
    """
    return '{0} to {1}'.format(lower_bound(x), upper_bound(x))

def add_interval(x, y):
    """Return an interval that contains the sum of any value in interval x and
    any value in interval y.

    >>> str_interval(add_interval(interval(-1, 2), interval(4, 8)))
    '3 to 10'
    """
    lower = lower_bound(x) + lower_bound(y)
    upper = upper_bound(x) + upper_bound(y)
    return interval(lower, upper)

def mul_interval(x, y):
    """Return the interval that contains the product of any value in x and any
    value in y.

    >>> str_interval(mul_interval(interval(-1, 2), interval(4, 8)))
    '-8 to 16'
    """
    p1 = lower_bound(x) * lower_bound(y)
    p2 = lower_bound(x) * upper_bound(y)
    p3 = upper_bound(x) * lower_bound(y)
    p4 = upper_bound(x) * upper_bound(y)
    return interval(min(p1, p2, p3, p4), max(p1, p2, p3, p4))


# Q3.

def interval(a, b):
    """Construct an interval from a to b."""
    "*** YOUR CODE HERE ***"
    return (a, b)

def lower_bound(x):
    """Return the lower bound of interval x."""
    "*** YOUR CODE HERE ***"
    return x[0] if x[0] < x[1] else x[1]

def upper_bound(x):
    """Return the upper bound of interval x."""
    "*** YOUR CODE HERE ***"
    return x[0] if x[0] > x[1] else x[1]

# Q4.

def div_interval(x, y):
    """Return the interval that contains the quotient of any value in x
    divided by any value in y.

    Division is implemented as the multiplication of x by the reciprocal of y.

    >>> str_interval(div_interval(interval(-1, 2), interval(4, 8)))
    '-0.25 to 0.5'
    """
    "*** YOUR CODE HERE ***"
    reciprocal_y = interval(1/upper_bound(y), 1/lower_bound(y))
    return mul_interval(x, reciprocal_y)

# Q5.

def sub_interval(x, y):
    """Return the interval that contains the difference between any value in x
    and any value in y.

    >>> str_interval(sub_interval(interval(-1, 2), interval(4, 8)))
    '-9 to -2'
    """
    "*** YOUR CODE HERE ***"
    lower = lower_bound(x) - upper_bound(y)
    upper = upper_bound(x) - lower_bound(y)
    return interval(lower, upper)

# Q6.

def make_center_width(c, w):
    """Construct an interval from center and width."""
    return interval(c - w, c + w)

def center(x):
    """Return the center of interval x."""
    return (upper_bound(x) + lower_bound(x)) / 2

def width(x):
    """Return the width of interval x."""
    return (upper_bound(x) - lower_bound(x)) / 2


def make_center_percent(c, p):
    """Construct an interval from center and percentage tolerance.

    >>> str_interval(make_center_percent(2, 50))
    '1.0 to 3.0'
    """
    "*** YOUR CODE HERE ***"
    return make_center_width(2, 2*50/100)

def percent(x):
    """Return the percentage tolerance of interval x.

    >>> percent(interval(1, 3))
    50.0
    """
    "*** YOUR CODE HERE ***"
    return width(x) / center(x) * 100


# Q7.

def quadratic(x, a, b, c):
    """Return the interval that is the range the quadratic defined by a, b,
    and c, for domain interval x.

    This is the less accurate version which treats each instance of t as a
    different value from the interval. See the extra for experts question for
    exploring why this is not _really_ correct and to write a more precise
    version.

    >>> str_interval(quadratic(interval(0, 2), -2, 3, -1))
    '-9 to 5'
    >>> str_interval(quadratic(interval(1, 3), 2, -3, 1))
    '-6 to 16'
    """
    "*** YOUR CODE HERE ***"

# Q8.

def par1(r1, r2):
    return div_interval(mul_interval(r1, r2), add_interval(r1, r2))

def par2(r1, r2):
    one = interval(1, 1)
    rep_r1 = div_interval(one, r1)
    rep_r2 = div_interval(one, r2)
    return div_interval(one, add_interval(rep_r1, rep_r2))


# These two intervals give different results for parallel resistors:
"*** YOUR CODE HERE ***"

# Q9.

def multiple_reference_explanation():
  return """The multiple reference problem..."""

# Q10.

def accurate_quadratic(x, a, b, c):
    """Return the interval that is the range the quadratic defined by a, b,
    and c, for domain interval x.

    >>> str_interval(accurate_quadratic(interval(0, 2), -2, 3, -1))
    '-3 to 0.125'
    >>> str_interval(accurate_quadratic(interval(1, 3), 2, -3, 1))
    '0 to 10'
    """
    "*** YOUR CODE HERE ***"

if __name__ == '__main__':
    from doctest import run_docstring_examples
    run_docstring_examples(reverse_rlist_iterative, globals(), True)
    run_docstring_examples(reverse_rlist_recursive, globals(), True)
    run_docstring_examples(interleave_iterative, globals(), True)
    primes = rlist(2, rlist(3, rlist(5, rlist(7, empty_rlist))))
    reverse_rlist_recursive(primes)
    run_docstring_examples(str_interval, globals(), True)
    run_docstring_examples(add_interval, globals(), True)
    run_docstring_examples(mul_interval, globals(), True)
    run_docstring_examples(div_interval, globals(), True)
    run_docstring_examples(sub_interval, globals(), True)
    run_docstring_examples(make_center_percent, globals(), True)
    run_docstring_examples(percent, globals(), True)



