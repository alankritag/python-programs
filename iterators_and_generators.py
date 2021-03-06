# return n fibonacci numbers


def fib1():
    x = 0
    y = 1
    while True:
        x, y = y, x+y
        yield x

call = fib1()
l = []
for _ in range(5):
    l.append(call.next())
print "Way 1:", l


def fib2(n):
    x = 0
    y = 1
    for _ in range(n):
        x, y = y, x+y
        yield x

print "Way 2:", list(fib2(5))


class rev_iter():
    '''
    Writing your own iterable
    __iter__ actually returns the iterable
    '''
    def __init__(self, n):
        self.i = 0
        self.n = n

    def __iter__(self):
        return self

    def next(self):
        if self.i < self.n:
            n = self.n
            self.n -= 1
            return n
        else:
            raise StopIteration

ca = rev_iter(5)
print "Own iterable:", ca.next(), ca.next(), ca.next(), ca.next(), ca.next()

# Make this easier using generator
def rev_iter_using_generator(n):
    for _ in range(n):
        yield n
        n -= 1

ca = rev_iter_using_generator(5)
print "Above using generator:", ca.next(), ca.next(), ca.next(), ca.next(), ca.next()

# generator expression like list comprehension
print "List comprehension: ", [x*x for x in range(1, 5)]
print "Generator: ", (x*x for x in range(1, 5))
print "List using generator", list((x*x for x in range(1, 5)))

# python factorial generator
def factorial(n):
    fact = 1
    some_count = 1
    for _ in xrange(n):
        yield fact
        some_count += 1
        fact *= some_count

n = 5
print("First %d factorials are: %s" %(n, list(factorial(n))))


print "*"*80
# use of send in generators
def fibonacci():
    x, y, z = 0, 1, 0
    while z < 4:
        x, y = y, x+y
        z = yield x
        print x, z

ob = fibonacci()
for i in xrange(100):
    print "Yielded value: ", ob.next()
    if i == 5:
        ob.send(i)
