def make_offsetter(num):
	"""
	Returns a function that takes one argument and returns
	num + some offset.
	>>> x = make_offsetter(3)
	>>> y = make_offsetter(8)
	>>> x(2)
	5
	>>> y(-1)
	7
	"""
	return lambda offset: num + offset

def curry2(f):
	return lambda x: lambda y: f(x, y)

def rev_curry2(f):
	"""
	Return a curried version of the given curried function,
	with the arguments reversed.
	>>> f = rev_curry2(curry2(lambda x, y: x / y))
	>>> f(4)(2)
	0.5
	"""
	return lambda x: lambda y: f(y)(x)

def approx_deriv(fn, x, dx=0.00001):
	return (fn(x+dx)-fn(x))/dx

def iter_improve(update, isdone, guess=1, max_iterations=100):
	i = 1
	while not isdone(guess) and i <= max_iterations:
		guess = update(guess)
		i += 1
	return guess

def newtons_method2(fn, guess=1, max_iterations=100):
	def newtons_update(guess):
		return guess - fn(guess) / approx_deriv(fn, guess)
	def newtons_isdone(guess):
		ALLOWED_ERROR_MARGIN = 0.0000001
		return abs(fn(guess)) <= ALLOWED_ERROR_MARGIN
	return iter_improve(newtons_update,
						newtons_isdone,
						max_iterations)

def cube_root(n):
	return newtons_method2(lambda x: pow(x,3) - n)

def newtons_method3(fn, guess=1, max_iterations=100):
	def newtons_update(guess, min_size=0.001):
		dtv = approx_deriv(fn, guess)
		if abs(dtv) < min_sieze:
			return None
		return guess - fn(guess) / dtv

	def newtons_done(guess):
		ALLOWED_ERROR_MARGIN = 0.0000001
		if guess == None:
			return True
		return abs(fn(guess)) <= ALLOWED_ERROR_MARGIN
		
	return iter_improve(newtons_update, 
						newtons_done, 
						guess,
						max_iterations)

if __name__ == '__main__':
    from doctest import run_docstring_examples
    run_docstring_examples(make_offsetter, globals(), True)
    run_docstring_examples(rev_curry2, globals(), True)

