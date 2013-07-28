def remove_all(el, lst):
	"""Removes all instances of el from lst.
	>>> x = [3, 1, 2, 1, 5, 1, 1, 7]
	>>> remove_all(1, x)
	>>> x
	[3, 2, 5, 7]
	"""
	while el in lst:
		lst.remove(el)

def add_this_many(x, y, lst):
	""" Adds y to the end of lst the number of times x occurs in lst.
	>>> lst = [1, 2, 4, 2, 1]
	>>> add_this_many(1, 5, lst)
	>>> lst
	[1, 2, 4, 2, 1, 5, 5]
	"""
	cnt = 0
	for el in lst:
		if el == x:
			cnt += 1
	for _ in range(cnt):
		lst.append(y)

def reverse(lst):
	""" Reverses lst in place.
	>>> x = [3, 2, 4, 5, 1]
	>>> reverse(x)
	>>> x
	[1, 5, 4, 2, 3]
	"""
	i, j = 0, len(lst)-1
	while i <= j:
		lst[i], lst[j] = lst[j], lst[i]
		i, j = i+1, j-1

def rotate1(lst, k):
	""" Return a new list, with the same elements
	of lst, rotated to the right k.
	>>> x = [1, 2, 3, 4, 5]
	>>> rotate1(x, 3)
	[3, 4, 5, 1, 2]
	"""
	new = []
	new[0:] = lst[(len(lst)-k) : ]
	new[k:] = lst[0 : (len(lst)-k)]
	return new

def rotate2(lst, k):
	""" Return a new list, with the same elements
	of lst, rotated to the right k.
	>>> x = [1, 2, 3, 4, 5]
	>>> rotate2(x, 3)
	[3, 4, 5, 1, 2]
	"""
	return lst[-k:] + lst[:-k]

def replace_all(d, x, y):
	"""Replaces all values of x with y.
	>>> d = {1: {2:3, 3:4}, 2:{4:4, 5:3}}
	>>> replace_all(d,3,1)
	>>> d
	{1: {2: 1, 3: 4}, 2: {4: 4, 5: 1}}
	"""
	for k in d.keys():
		if d[k] == x:
			d[k] = y
		elif type(d[k]) == dict:
			replace_all(d[k], x, y)

def rm(d, x):
	"""Removes all pairs with value x.
	>>> d = {1:2, 2:3, 3:2, 4:3}
	>>> rm(d,2)
	>>> d
	{2: 3, 4: 3}
	"""
	indices = []
	for k in d.keys():
		if d[k] == x:
			indices.append(k)
	for k in indices:
		del d[k] 

if __name__ == '__main__':
    from doctest import run_docstring_examples
    run_docstring_examples(remove_all, globals(), True)
    run_docstring_examples(add_this_many, globals(), True)
    run_docstring_examples(reverse, globals(), True)
    run_docstring_examples(rotate2, globals(), True)
    run_docstring_examples(replace_all, globals(), True)
    run_docstring_examples(rm, globals(), True)
