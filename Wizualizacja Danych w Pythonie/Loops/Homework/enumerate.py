def enumerate(sequence,start=0):
    yield from [(x+start,x) for x in sequence]