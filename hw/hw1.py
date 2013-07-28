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
    "*** YOUR CODE HERE ***"
    def next(x):
    	if x % 2 == 0:
    		return x // 2
    	else: 
    		return 3 * x + 1

    cnt = 0
    while True:
    	print (n)
    	cnt += 1
    	if n == 1:
    		break
    	n = next(n)

    return cnt


if __name__ == '__main__':
    from doctest import run_docstring_examples
    run_docstring_examples(hailstone, globals(), True)