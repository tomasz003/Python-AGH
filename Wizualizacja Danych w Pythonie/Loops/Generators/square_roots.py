import math
def square_roots(numbers: list):
    yield from (math.sqrt(x) for x in numbers if x>=0)