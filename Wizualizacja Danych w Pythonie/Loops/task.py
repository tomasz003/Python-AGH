def iter_input():
    return tuple(iter(lambda: input("Number: "), '0'))


print(iter_input())
