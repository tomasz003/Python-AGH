# assume we want to create a list of squares, like:
# First method:
squares1 = []
for x in range(10):
    squares1.append(x ** 2)
print(squares1)

# Second method:
squares2 = list(map(lambda x: x**2, range(10)))
# or, equivalently:

squares3 = [x ** 2 for x in range(10)]

# Two lists
combs1 = [(x,y) for x in [1,2,3] for y in [3,1,4] if x!=y]
# and it’s equivalent to:
combs2 = []
for x in [1, 2, 3]:
    for y in [3, 1, 4]:
        if x != y:
            combs2.append((x, y))
print(combs2)
