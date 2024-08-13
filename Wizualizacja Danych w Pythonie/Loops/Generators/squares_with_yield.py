def squares(n:int):
    yield from [x**2 for x in range(n+1)]