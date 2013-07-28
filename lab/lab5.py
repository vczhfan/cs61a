def reverse_iter1(tup):
    """Returns the reverse of the given tuple.

    >>> reverse_iter1((1, 2, 3, 4))
    (4, 3, 2, 1)
    """
    "*** YOUR CODE HERE ***"
    l = []
    for i in range(len(tup)-1, -1, -1):
    	l.append(tup[i])
    return (tuple(l))

def reverse_iter2(tup):
    """Returns the reverse of the given tuple.

    >>> reverse_iter2((1, 2, 3, 4))
    (4, 3, 2, 1)
    """
    "*** YOUR CODE HERE ***"
    t = ()
    for i in range(len(tup)-1, -1, -1):
    	t += (tup[i],)
    return (t)
   		
def reverse_recursive(tup):
    """Returns the reverse of the given tuple.

    >>> reverse_recursive((1, 2, 3, 4))
    (4, 3, 2, 1)
    """
    if len(tup) == 0:
    	return () 
    return (tup[-1],) + reverse_recursive(tup[:-1])

def merge_iter1(tup1, tup2):
    """Merges two sorted tuples.

    >>> merge_iter1((1, 3, 5), (2, 4, 6))
    (1, 2, 3, 4, 5, 6)
    >>> merge_iter1((), (2, 4, 6))
    (2, 4, 6)
    >>> merge_iter1((1, 2, 3), ())
    (1, 2, 3)
    """
    "*** YOUR CODE HERE ***"
    tup = ()
    for i in range(len(tup1)):
    	tup += (tup1[i], )
    for i in range(len(tup2)):
    	tup += (tup2[i], )
    return tuple(sorted(tup))

def merge_iter2(tup1, tup2):
    """Merges two sorted tuples.

    >>> merge_iter2((1, 3, 5), (2, 4, 6))
    (1, 2, 3, 4, 5, 6)
    >>> merge_iter2((), (2, 4, 6))
    (2, 4, 6)
    >>> merge_iter2((1, 2, 3), ())
    (1, 2, 3)
    """
    "*** YOUR CODE HERE ***"
    new = ()
    while tup1 and tup2: 
        if tup1[0] < tup2[0]: 
            new += (tup1[0], )
            tup1 = tup1[1:] 
        else: 
            new += (tup2[0], )
            tup2 = tup2[1:]
    if tup1:
        return new + tup1
    if tup2:
        return new + tup2

def merge_recursive(tup1, tup2):
    """Merges two sorted tuples.

    >>> merge_recursive((1, 3, 5), (2, 4, 6))
    (1, 2, 3, 4, 5, 6)
    >>> merge_recursive((), (2, 4, 6))
    (2, 4, 6)
    >>> merge_recursive((1, 2, 3), ())
    (1, 2, 3)
    """
    "*** YOUR CODE HERE ***"
    if not tup1 or not tup2:
        return tup1 + tup2
    if tup1[0] < tup2[0]:
        return (tup1[0], tup2[0]) + merge_recursive(tup1[1:], tup2[1:]) 
    else:
        return (tup2[0], tup1[0]) + merge_recursive(tup1[1:], tup2[1:])

def deep_len(tup):
    """Returns the deep length of the tuple.

    >>> deep_len((1, 2, 3))      # normal tuple
    3
    >>> x = (1, (2, 3), 4)       # deep tuple
    >>> deep_len(x)
    4
    >>> y = ((1, (1, 1)), 1, (1, 1))  # deep tuple
    >>> deep_len(y)
    6
    """
    "*** YOUR CODE HERE ***"
    if not tup:
        return 0
    if type(tup[0]) == tuple:
        return deep_len(tup[0]) + deep_len(tup[1:])
    else:
        return 1 + deep_len(tup[1:])

empty_rlist = None

def rlist(first, rest=empty_rlist):
    return (first, rest)

def first(rlist):
    return rlist[0]

def rest(rlist):
    return rlist[1]

def tup_to_rlist(tup):
    """Converts a tuple to an rlist.

    >>> tup = (1, 2, 3, 4)
    >>> r = tup_to_rlist(tup)
    >>> first(r)
    1
    >>> first(rest(rest(r)))
    3
    >>> r = tup_to_rlist(())
    >>> r is empty_rlist
    True
    """
    "***YOUR CODE HERE ***"
    r = empty_rlist
    for i in range(len(tup)-1, -1, -1):
        r = rlist(tup[i], r)
    return r

def len_rlist(lst):
    """Returns the length of the rlist.

    >>> lst = tup_to_rlist((1, 2, 3, 4))
    >>> len_rlist(lst)
    4
    >>> lst = tup_to_rlist(())
    >>> len_rlist(lst)
    0
    """
    "*** YOUR CODE HERE ***"
    if lst == empty_rlist:
        return 0
    return 1 + len_rlist(rest(lst)) 

def getitem_rlist(i, lst):
    """Returns the ith item in the rlist. If the index exceeds the
    length of the rlist, return 'Error'.

    >>> lst = tup_to_rlist((1, 2, 3, 4))
    >>> getitem_rlist(0, lst)
    1
    >>> getitem_rlist(3, lst)
    4
    >>> getitem_rlist(4, lst)
    'Error'
    """
    "*** YOUR CODE HERE ***"
    if lst == empty_rlist:
        return 'Error'
    if i == 0:
        return first(lst)
    return getitem_rlist(i-1, rest(lst))

if __name__ == '__main__':
    from doctest import run_docstring_examples
    run_docstring_examples(reverse_iter1, globals(), True)
    run_docstring_examples(reverse_iter2, globals(), True)
    run_docstring_examples(reverse_recursive, globals(), True)
    run_docstring_examples(merge_iter1, globals(), True)
    run_docstring_examples(merge_iter2, globals(), True)
    run_docstring_examples(merge_recursive, globals(), True)
    run_docstring_examples(deep_len, globals(), True)
    run_docstring_examples(tup_to_rlist, globals(), True)
    run_docstring_examples(len_rlist, globals(), True)
    run_docstring_examples(getitem_rlist, globals(), True)
