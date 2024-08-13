# enumerate
for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)

# zip
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))

# reversed
for i in reversed(range(1, 10, 2)):
    print(i)

# sorted
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for i in sorted(basket):
    print(i)

# set + sorted
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)):
    print(f)

# do not change the list while looping over it
import math

raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
# not good
for value in raw_data:
    if math.isnan(value):
        del value
print(raw_data)

# now ok
filtered_data = []
for value in raw_data:
    if not math.isnan(value):
        filtered_data.append(value)
print(filtered_data)
