from math import sqrt
def distance(city1, city2):
	lat_1, lon_1 = get_lat(city_1), get_lon(city_1)
	lat_2, lon_2 = get_lat(city_2), get_lon(city_2)
	return sqrt((lat_1 - lat_2)**2 + (lon_1 - lon_2)**2)


def closer_city(lat, lon, city1, city2):
	city = make_city('origin')
	d1 = distance(city, city1)
	d2 = distance(city, city2)
	if d1 < d2:
		return get_name(city1)
	else:
		return get_name(city2)


from math import pow
def rational_pow(x, e):
    return rational(pow(number(x), 2), pow(denom(x), 2))

def approx_e(iter=100):
    e = rational(0, 1)
    k = 0
    while k < iter:
        e = add_rationals(e, rational(1, factorial(k))) 
        k += 1
    return e

def inverse_rational(x):
	"""Returns the inverse of the given non-zero rational number"""
	return rational(denom(x), number(x))

def div_rationals(x, y):
	"""Returns x / y for given rational x and non-zero rational y"""
	return mul_rationals(x, inverse_rational(y))

def make_unit(catchphrase, damage):
	return (catchphrase, damage)

def get_catchphrase(unit):
	return unit[0]

def get_damage(unit):
	return unit[1]

def battle(first, second):
	"""Simulates a battle between the first and second unit
	>>> zealot = make_unit('My life for Aiur!', 16)
	>>> zergling = make_unit('GRAAHHH!', 5)
	>>> winner = battle(zergling, zealot)
	GRAAHHH!
	My life for Aiur!
	>>> winner is zealot
	True
	"""
	print (get_catchphrase(first))
	print (get_catchphrase(second))
	return first if get_damage(first) > get_damage(second) else second

def pair(x, y):
	"""Return a function that behaves like a two-element tuple"""
	def dispatch(m):
		if m == 0:
			return x
		elif m == 1:
			return y
	return dispatch

def getitem_pair(p, i):
	"""Return the element at index i of pair p"""
	return p(i)

def make_resource_bundle(minerals, gas):
	return pair(minerals, gas)

def get_minerals(bundle):
	return getitem_pair(bundle, 0)

def get_gas(bundle):
	return getitem_pair(bundle, 1)

def make_building(unit, bundle):
	return pair(unit, bundle)

def get_unit(building):
	return getitem_pair(building, 0)

def get_bundle(building):
	return getitem_pair(building, 1)

def build_unit(building, bundle):
	"""Constructs a unit if given the minimum amount of resources.
	Otherwise, prints an error message
	>>> barracks = make_building(make_unit('Go go go!', 6), make_resource_bundle(50, 0))
	>>> marine = build_unit(barracks, make_resource_bundle(20, 20))
	We require more minerals!
	>>> marine = build_unit(barracks, make_resource_bundle(50, 0))
	>>> print(get_catchphrase(marine))
	Go go go!
	"""
	if get_minerals(get_bundle(building)) > get_minerals(bundle):
		print ("We require more minerals!")
	elif get_gas(get_bundle(building)) > get_gas(bundle):
		print ("We require more gas!")
	unit = get_unit(building)
	return make_unit(get_catchphrase(unit), get_damage(unit))

if __name__ == '__main__':
    from doctest import run_docstring_examples
    run_docstring_examples(battle, globals(), True)
    run_docstring_examples(build_unit, globals(), True)







