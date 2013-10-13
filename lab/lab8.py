class Rlist(object):

    class EmptyList(object):
        def __len__(self):
            return 0

    empty = EmptyList()

    def __init__(self, first, rest=empty):
        self.first = first
        self.rest = rest

    def __len__(self):
        "*** YOUR CODE HERE ***"
        return 1 + len(self.rest)

    def __getitem__(self, index):
        "*** YOUR CODE HERE ***"
        if index == 0:
        	return self.first
       	elif self.rest is Rlist.empty:
       		print ('Index out of bounds')
        return self.rest[index-1]

    def __repr__(self):
        "*** YOUR CODE HERE ***"
        if self.rest is Rlist.empty:
        	return 'Rlist({0})'.format(self.first)
        return 'Rlist({0}, {1})'.format(self.first, repr(self.rest))

def rlist_to_list(rlist):
    """Takes an RLIST and returns a Python list with the same
    elements.

    >>> rlist = Rlist(1, Rlist(2, Rlist(3, Rlist(4))))
    >>> rlist_to_list(rlist)
    [1, 2, 3, 4]
    >>> rlist_to_list(Rlist.empty)
    []
    """
    "*** YOUR CODE HERE ***"
    if rlist is Rlist.empty:
    	return []
    return [rlist.first] + rlist_to_list(rlist.rest)

def insert(rlist, value, index):
    if index == 0:
        rlist.rest = Rlist(rlist.first, rlist.rest)
        rlist.first = value
    elif rlist.rest is Rlist.empty:
        print('Index out of bounds')
    else:
        insert(rlist.rest, value, index-1)

def reverse_rec(rlist):
    if rlist.rest is not Rlist.empty:
        second, last = rlist.rest, rlist
        rlist = reverse_rec(second)
        second.rest, last.rest = last, Rlist.empty
    return rlist

def reverse(rlist):
    """Returns an Rlist that is the reverse of the original.

    >>> Rlist(1).rest is Rlist.empty
    True
    >>> rlist = Rlist(1, Rlist(2, Rlist(3)))
    >>> reverse(rlist)
    Rlist(3, Rlist(2, Rlist(1)))
    >>> reverse(Rlist(1))
    Rlist(1)
    """
    new = Rlist(rlist.first)
    while rlist.rest is not Rlist.empty:
        new = Rlist(rlist.rest.first, new)
        rlist = rlist.rest
    return new

def type_tag(x):
    return type_tag.tags[type(x)]

# notice that type_tag is kind of unnecessary here
type_tag.tags = {
    list  : 'list',
    Rlist : 'Rlist',
}

def extend(seq1, seq2):
    """Takes the elements of seq2 and adds them to the end of seq1.

    >>> rlist = Rlist(4, Rlist(5, Rlist(6)))
    >>> lst = [1, 2, 3]
    >>> extend(lst, rlist)
    >>> lst
    [1, 2, 3, 4, 5, 6]
    >>> rlist
    Rlist(4, Rlist(5, Rlist(6)))
    >>> extend(rlist, [7, 8])
    >>> rlist
    Rlist(4, Rlist(5, Rlist(6, Rlist(7, Rlist(8)))))
    >>> extend(lst, [7, 8, 9])
    >>> lst
    [1, 2, 3, 4, 5, 6, 7, 8, 9]
    """
    "*** YOUR CODE HERE ***"
    types = (type_tag(seq1), type_tag(seq2))
    return extend.impl[types](seq1, seq2)


def list_to_rlist(lst):
    if len(lst) == 0:
        return Rlist.empty
    return Rlist(lst.pop(0), list_to_rlist(lst))

def extend_list_list(lst1, lst2):
    lst1.extend(lst2)

def extend_list_rlist(lst, rlist):
    return lst.extend(rlist_to_list(rlist))

def extend_rlist_rlist(rlist1, rlist2):
    if rlist1.rest is Rlist.empty:
        rlist1.rest = rlist2
    else:
        extend_rlist_rlist(rlist1.rest, rlist2)

def extend_rlist_list(rlist, lst):
    l = list_to_rlist(lst)
    extend_rlist_rlist(rlist, l)

extend.impl = {
  ('list', 'list')   : extend_list_list,
  ('list', 'Rlist')  : extend_list_rlist,
  ('Rlist', 'list')  : extend_rlist_list,
  ('Rlist', 'Rlist') : extend_rlist_rlist,
}

if __name__ == '__main__':
    from doctest import run_docstring_examples
    run_docstring_examples(rlist_to_list, globals(), True)
    run_docstring_examples(insert, globals(), True)
    run_docstring_examples(reverse, globals(), True)
    run_docstring_examples(extend, globals(), True)
