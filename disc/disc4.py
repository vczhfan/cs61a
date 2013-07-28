def countdown(n):
	"""
	>>> countdown(3)
	3
	2
	1
	"""
	print (n)
	if n > 1:
		countdown(n-1)

def countup(n):
	"""
	>>> countup(3)
	1
	2
	3
	"""
	if n > 1:
		countup(n-1)
	print (n)

def expt(base, power):
	if power == 1:
		return base	
	return base * expt(base, power-1)

def is_prime(n):
    '''check if integer n is a prime'''
    # range starts with 2 and only needs to go up the squareroot of n
    for x in range(2, int(n**0.5)+1):
        if n % x == 0:
            return False
    return True

def sum_primes_up_to(n):
	if n <= 1: 
		return 0
	elif is_prime(n):
		return n + sum_primes_up_to(n-1)
	else:
		return sum_primes_up_to(n-1)

def sum_filter_up_to(n, pred):
	if n < 1: 
		return 0
	elif pred(n):
		return n + sum_filter_up_to(n-1)
	else:
		return sum_filter_up_to(n-1)

def count_stair_ways(n):
	if n == 1:
		return 1
	elif n == 2:
		return 2
	else: 
		return count_stair_ways(n-1) + count_stair_ways(n-2)

if __name__ == '__main__':
    from doctest import run_docstring_examples
    run_docstring_examples(countdown, globals(), True)
    run_docstring_examples(countup, globals(), True)
    print (expt(2, 3))
    print (expt(3, 2)) 
    print (sum_primes_up_to(7))

