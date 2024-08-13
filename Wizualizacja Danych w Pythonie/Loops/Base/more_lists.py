vec = [-4, -2, 0, 2, 4]

# create a new list with the values doubled
a = [2*x for x in vec]
print(a)

# filter the list to exclude negative numbers
b = [x for x in vec if x>=0]
print(b)

# apply a function to all the elements
c = [x^2 for x in vec]

# call a method on each element
freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
d = [x.strip(' ') for x in freshfruit]
print(d)

# create a list of 2-tuples like (number, square)
e = [(x, x**2) for x in range(0,6)]
print(e)
