# Use list comprehensions with/without condition
a = [x for x in range(1,9) if x%2==0]
b = [x for x in range(1,9) if x%3==2]

# Unpack lists a,b
c = [*a,*b]
print(f"a={a}\nb={b}\nc={c}")

my_list = [x for x in range(1, 10)]

# b should be a list
[a1, *b1, c1]= my_list
print(f"a1={a1}\nb1={b1}\nc1={c1}")
