def flatten(our_list):
    for x in our_list:
        if type(x)==list or type(x)==tuple:
            yield from flatten(x)
        else:
            yield x