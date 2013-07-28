def add_matrices(x, y):
	return [[x[d1][d2] + y[d1][d2] for d2 in range(len(x[0]))] for d1 in range(len(x))]

def deck():
	return [(suit, value) for suit in ['heart', 'diamond', 'spade', 'club'] for value in range(1, 14)]		

def sort_deck(deck): 
	deck.sort(key=lambda card: card[1]) 
	deck.sort(key=lambda card: card[0])

def build_successors_table(tokens):
    table = {}
    prev = '.'
    for word in tokens:
        if prev in table:
            table[prev].append(word)
        else:
            table[prev] = [word]

        prev = word
    return table

def construct_sent(word, table):
     import random
     result = ''
     while word not in ['.', '!', '?']:
     	result += word + ' '
     	word = random.choice(table[word]) 
    return (result + word)

def shakespeare_tokens(path = 'shakespeare.txt', url = 'http://inst.eecs.berkeley.edu/~cs61a/fa11/shakespeare.txt'):
    """Return the words of Shakespeare's plays as a list"""
    import os
    from urllib.request import urlopen
    if os.path.exists(path):
        return open('shakespeare.txt', encoding='ascii').read().split()
    else:
        shakespeare = urlopen(url)
        return shakespeare.read().decode(encoding='ascii').split()

def sent():
    return construct_sent('The', table)

def make_fib():
    is_first, prev, curr = True, 0, 1
    def fib():
        nonlocal is_first, prev, curr
        if is_first:
            is_first = False
            return 1
        prev, curr = curr, (prev+curr) 
        return curr
    return fib

if __name__ == '__main__':
	# print (add_matrices([[1, 3], [2, 0]], [[-3, 0], [1, 2]]))
	# d = deck()
	# print (d)
	# sort_deck(d)
	# print (d)
	# text = ['We', 'came', 'to', 'investigate', ',', 'catch', 'bad', 'guys', 'and', 'to', 'eat', 'pie', '.']
	# table = build_successors_table(text)
	# print (table)
    # fib = make_fib()
    # for _ in range(10):
    #     print (fib())


	