def fib(i=1, j=1):
    yield i
    yield from fib(j, j+i)