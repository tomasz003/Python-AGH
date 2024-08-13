def collatz(n):
    yield n
    if n%2==0:
        yield from collatz(n/2)
    elif n!=1:
        yield from collatz(3*n+1)


coll = collatz(34)
while True:
    try:
        print(next(coll),end=' ')
    except StopIteration:
        break