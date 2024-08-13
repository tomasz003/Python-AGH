def remove_smaller_than(numbers: list, limit: int):
    yield from (x for x in numbers if x>=limit)