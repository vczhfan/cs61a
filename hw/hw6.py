# Name:
# Login:
# TA:
# Section:
# Q1.

def divide_by_fact(dividend, n):
    """Recursively divide dividend by the factorial of n.

    >>> divide_by_fact(120, 4)
    5.0
    """
    if n == 1:
    	return dividend
    return divide_by_fact(dividend / n, n - 1)

# Q2.

def group(seq):
    """Divide a sequence of at least 12 elements into groups of 4 or
    5. Groups of 5 will be at the end. Returns a tuple of sequences, each
    corresponding to a group.

    >>> group(range(14))
    (range(0, 4), range(4, 9), range(9, 14))
    >>> group(tuple(range(17)))
    ((0, 1, 2, 3), (4, 5, 6, 7), (8, 9, 10, 11), (12, 13, 14, 15, 16))
    """
    num = len(seq)
    assert num >= 12
    "*** YOUR CODE HERE ***"
    l = ()
    for i in range(0, num//4+1):
        for j in range(0, num//5+1):
            if (i * 4 + j * 5) == num:
                l += tuple(seq[4*n:4*n+4] for n in range(i))
                l += tuple(seq[4*i+5*n:4*i+5*n+5] for n in range(j))
    return l


"""

   ====
    ==
========== <--- spatula underneath this crust
 ========

    ||
    ||
   \||/
    \/

========== }
    ==     } flipped
   ====    }
 ========

"""

# Q3.

def partial_reverse(lst, start):
    """Reverse part of a list in-place, starting with start up to the end of
    the list.

    >>> a = [1, 2, 3, 4, 5, 6, 7]
    >>> partial_reverse(a, 2)
    >>> a
    [1, 2, 7, 6, 5, 4, 3]
    >>> partial_reverse(a, 5)
    >>> a
    [1, 2, 7, 6, 5, 3, 4]
    """
    "*** YOUR CODE HERE ***"
    lst[start:] = lst[-1:start-1:-1]

# Q4.

def index_largest(seq):
    """Return the index of the largest element in the sequence.

    >>> index_largest([8, 5, 7, 3 ,1])
    0
    >>> index_largest((4, 3, 7, 2, 1))
    2
    """
    assert len(seq) > 0
    "*** YOUR CODE HERE ***"
    idx = 0
    for i in range(1, len(seq)):
        if seq[i] > seq[idx]:
            idx = i
    return idx

# Q5.

def pizza_sort(lst, i=0):
    """Perform an in-place pizza sort on the given list, resulting in
    elements in descending order.

    >>> a = [8, 5, 7, 3, 1, 9, 2]
    >>> sort = pizza_sort(a)
    >>> sort(a)
    >>> a
    [9, 8, 7, 5, 3, 2, 1]
    """
    "*** YOUR CODE HERE ***"
    def inner(lst):
        nonlocal i
        if len(lst) == i:
            return None
        idx = index_largest(lst[i:])
        lst[i], lst[idx+i] = lst[idx+i], lst[i]
        i += 1
        inner(lst)
    return inner


# Q6.

from functools import reduce
def make_accumulator():
    """Return an accumulator function that takes a single numeric argument and
    accumulates that argument into total, then returns total.

    >>> acc = make_accumulator()
    >>> acc(15)
    15
    >>> acc(10)
    25
    >>> acc2 = make_accumulator()
    >>> acc2(7)
    7
    >>> acc3 = acc2
    >>> acc3(6)
    13
    >>> acc2(5)
    18
    >>> acc(4)
    29
    """
    "*** YOUR CODE HERE ***"
    lst = []
    def inner(num):
        lst.append(num)
        return reduce(lambda x, y: x + y, lst)
    return inner


# Q7.

def make_accumulator_nonlocal():
    """Return an accumulator function that takes a single numeric argument and
    accumulates that argument into total, then returns total.

    >>> acc = make_accumulator_nonlocal()
    >>> acc(15)
    15
    >>> acc(10)
    25
    >>> acc2 = make_accumulator_nonlocal()
    >>> acc2(7)
    7
    >>> acc3 = acc2
    >>> acc3(6)
    13
    >>> acc2(5)
    18
    >>> acc(4)
    29
    """
    "*** YOUR CODE HERE ***"
    sum = 0
    def inner(num):
        nonlocal sum
        sum += num
        return sum
    return inner


# Q8.

# Old version
def count_change(a, coins=(50, 25, 10, 5, 1)):
    """
    >>> count_change(500, (50, 25, 10, 5, 1))
    59576
    """
    if a == 0:
        return 1
    elif a < 0 or len(coins) == 0:
        return 0
    return count_change(a, coins[1:]) + count_change(a - coins[0], coins)

# Version 2.0
def make_count_change():
    """Return a function to efficiently count the number of ways to make
    change.

    >>> cc = make_count_change()
    >>> cc(500, (50, 25, 10, 5, 1))
    59576
    """
    "*** YOUR CODE HERE **"
    memo = {}
    def inner(*args):
        if args[0] == 0:
            return 1
        elif args[0] < 0 or len(args[1]) == 0:
            return 0
        else:
            if args in memo:
                return memo[args]
            else:
                memo[args] = count_change(args[0], args[1][1:]) + count_change(args[0]-args[1][0], args[1])
                return memo[args]
    return inner


if __name__ == '__main__':
    from doctest import run_docstring_examples
    # run_docstring_examples(divide_by_fact, globals(), True)
    run_docstring_examples(group, globals(), True)
    # run_docstring_examples(partial_reverse, globals(), True)
    # run_docstring_examples(index_largest, globals(), True)
    # run_docstring_examples(pizza_sort, globals(), True)
    # run_docstring_examples(make_accumulator, globals(), True)
    # a = [8, 5, 7, 3, 1, 9, 2]
    # l = pizza_sort(a)
    # print (l)
    # import time
    # start_time = time.time()
    # run_docstring_examples(make_count_change, globals(), True)
    # run_docstring_examples(count_change, globals(), True)
    # print (time.time() - start_time, "seconds")
