# Name: yummy.bian@gmail.com
# Login:
# TA:
# Section:
# Q1.

def pig_latin_original(w):
    """Return the Pig Latin equivalent of a lowercase English word w."""
    if starts_with_a_vowel(w):
        return w + 'ay'
    return pig_latin_original(rest(w) + first(w))

def first(s):
    """Returns the first character of a string."""
    return s[0]

def rest(s):
    """Returns all but the first character of a string."""
    return s[1:]

def starts_with_a_vowel(w):
    """Return whether w begins with a vowel."""
    c = first(w)
    return c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u'

def pig_latin(w, s=set()):
    """Return the Pig Latin equivalent of a lowercase English word w.

    >>> pig_latin('pun')
    'unpay'
    >>> pig_latin('sphynx')
    'sphynxay'
    """
    "*** YOUR CODE HERE ***"
    if starts_with_a_vowel(w):
        return w + 'ay'
    if w in s:
        return w + 'ay'
    else:
        s.add(w)
    return pig_latin((rest(w)+first(w)))

# Q2.

def towers_of_hanoi(n, start, end):
    """Print the moves required to solve the towers of hanoi game if we start
    with n disks on the start pole and want to move them all to the end pole.

    The game is to assumed to have 3 poles (which is traditional).

    >>> towers_of_hanoi(1, 1, 3)
    Move 1 disk from rod 1 to rod 3
    >>> towers_of_hanoi(2, 1, 3)
    Move 1 disk from rod 1 to rod 2
    Move 1 disk from rod 1 to rod 3
    Move 1 disk from rod 2 to rod 3
    >>> towers_of_hanoi(3, 1, 3)
    Move 1 disk from rod 1 to rod 3
    Move 1 disk from rod 1 to rod 2
    Move 1 disk from rod 3 to rod 2
    Move 1 disk from rod 1 to rod 3
    Move 1 disk from rod 2 to rod 1
    Move 1 disk from rod 2 to rod 3
    Move 1 disk from rod 1 to rod 3
    """
    "*** YOUR CODE HERE ***"
    def target(a, b):
        for x in (1, 2, 3):
            if x != a and x != b:
                return x

    if n == 1:
        move_disk(start, end)
        return 
    else:
        towers_of_hanoi(n-1, start, target(start, end))
        move_disk(start, end)
        towers_of_hanoi(n-1, target(start, end), end)

def move_disk(start, end):
    print("Move 1 disk from rod", start, "to rod", end)

# Q3.

def part_wrapper(n):
    def fun(a, num=n, next_func=lambda x: x-1):
        if a == 0:
            return 1
        if a < 0 or num == 0:
            return 0
        return fun(a, next_func(num)) + fun(a - num, num)

    return fun

def part(n):
    """Return the number of partitions of positive integer n.

    >>> part(5)
    7
    >>> part(10)
    42
    >>> part(15)
    176
    >>> part(20)
    627
    """
    "*** YOUR CODE HERE ***"
    return part_wrapper(n)(n)

# Q4.

def summation(n, term):
    """Return the sum of the first n terms of a sequence.
  
    >>> summation(5, lambda x: pow(x, 3))
    225
    """
    total, k = 0, 1
    while k <= n:
        total, k = total + term(k), k + 1
    return total


def interleaved_sum(n, odd_term, even_term):
    """Compute the sum odd_term(1) + even_term(2) + odd_term(3) + ..., up
    to n.

    >>> # 1 + 2^2 + 3 + 4^2 + 5
    ... interleaved_sum(5, lambda x: x, lambda x: x*x)
    29
    """
    "*** YOUR CODE HERE ***"
    def wrapper(is_odd, curr):
        if curr > n:
            return 0
        else:
            if is_odd:
                return odd_term(curr) + wrapper(is_odd, curr+2)  
            else:
                return even_term(curr) + wrapper(is_odd, curr+2)

    return wrapper(is_odd=True, curr=1) + wrapper(is_odd=False, curr=2)

if __name__ == '__main__':
    from doctest import run_docstring_examples
    run_docstring_examples(pig_latin, globals(), True)
    run_docstring_examples(towers_of_hanoi, globals(), True)
    run_docstring_examples(part, globals(), True)
    run_docstring_examples(interleaved_sum, globals(), True)

