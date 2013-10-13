class Naturals():
    def __init__(self):
        self.current = 0

    def __next__(self):
        result = self.current
        self.current += 1
        return result

    def __iter__(self):
        return self


class Iter_Combiner():
    def __init__(self, iter1, iter2, combiner):
        self.iter1 = iter(iter1)
        self.iter2 = iter(iter2)
        self.combiner = combiner

    def __next__(self):
        return self.combiner(next(self.iter1), next(self.iter2))

    def __iter__(self):
        return self
        

class Fibonacci_Numbers():
    def __init__(self):
        self.prev = -1
        self.curr = 1

    def __next__(self):
        self.prev, self.curr = self.curr, self.prev + self.curr
        return self.curr

    def __iter__(self):
        return self

def generate_subsets():
    subsets = [[]]
    n = 1
    while True:
        yield subsets
        subsets = subsets + [s + [n] for s in subsets]
        n = n + 1

def perfect_squares():
    x = 0
    while True:
        yield power(x, 2)
        x = x +1

def generate_hailstone(n=10):
    while True:
        if n == 1:
            return 1
        yield n
        if n % 2:
            n = 3 * n + 1
        else:
            n = n % 2

def make_fib_stream():
    return fib_stream_generator(0, 1)

def fib_stream_generator(a, b):
    def compute_rest():
        return fib_stream_generator(b, a+b)
    return Stream(a, compute_rest)

def sub_streams(s1, s2):
    def compute_rest():
        return sub_streams(s1.rest, s2.rest)
    return Stream(s1.first - s2.first, compute_rest)

def converges_to(s, target, max_diff=0.00001, num_values=100):
    count = 0
    deriv = sub_streams(s.rest, s)
    for i in range(num_values):
        if abs(s.first - target) <= max_diff and  
            abs(deriv.first) <= max_diff:
            count += 1
        else:
            count = 0
        if count == 10:
            return True
        deriv = deriv.rest
        s = s.rest
    return False

class Stream(object):
    """A lazily computed recursive list."""
    class empty(object):
        def __repr__(self):
            return 'Stream.empty'
    empty = empty()
    def __init__(self, first, compute_rest=lambda: empty):
        assert callable(compute_rest), 'compute_rest must be callable.'
        self.first = first
        self._compute_rest = compute_rest
        self._rest = None
    @property
    def rest(self):
        """Return the rest of the stream, computing it if necessary."""
        if self._compute_rest is not None:
            self._rest = self._compute_rest()
            self._compute_rest = None
        return self._rest
    def __repr__(self):
        return 'Stream({0}, <...>)'.format(repr(self.first))

def make_integer_stream(first=1):
    def compute_rest():
        return make_integer_stream(first+1)
    return Stream(first, compute_rest)

