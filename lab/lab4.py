def add_ten_iter(x, n):
	total = x
	while n > 0:
		total, n = total + 10, n - 1 
	return total

def add_ten_iter2(x, n):
	i, sum = 1, x
	while i <= n:
		sum += 10 
		i += 1
	return sum

def add_ten_rec(x, n):
	if n == 0:
		return x
	return 10 + add_ten_rec(x, n-1)

def gcd_iter(a, b):
	while b != 0:
		a, b = b, a % b
	return a

def gcd_rec(a, b):
	if b == 0:
		return a
	return gcd_rec(b, a%b)

def func(a, b):
    i = 1
    while i <= a:
        print(i*b)
        i += 1

def func2(a, b):
	if a == 1:
		print (b)
		return 
	func2(a-1, b)
	print (a*b)

def sine(x):
	if abs(x) < 0.0001:
		return x
	return 3*sine(x/3) - 4*pow(sine(x/3), 3)

def count_paths(x, y):
	if x == 1 or y == 1:
		return 1
	return count_paths(x-1, y) + count_paths(x, y-1)

def first(word):
    return word[0]
        
def second(word):
    return word[1]
            
def rest(word):
    return word[1:]
  
def count_hi(phrase):
	if len(phrase) <= 1:
		return 0
	elif first(phrase) == 'h' and second(pharse) == 'i':
		return 1 + count_hi(rest(phrase))
	else:
		return count_hi(rest(phrase))

def is_vowel(char):
    return char == 'a' or char == 'e' or char == 'i' or char =='o' or char == 'u'

def remove_vowels(word):
	if len(word) == 0:
		return ''
	if not is_vowel(first(word)):
		print (first(word),)
	return remove_vowels(rest(word))

def remove_vowels2(word):
    if word == '':
        return ''
    elif is_vowel(first(word)):
        return remove_vowels(rest(word))
    else:
        return first(word) + remove_vowels(rest(word))

def pair_star(phrase):
	if len(phrase) <= 1:
		return phrase
	elif first(phrase) == second(phrase):
		return first(phrase) + '*' + pair_star(rest(phrase))
	else:
		return first(phrase) + pair_star(rest(phrase))

if __name__ == '__main__':
	print (pair_star("hiihhi"))
	print (pair_star("woodlands have squirrels"))
	print (pair_star("h"))
