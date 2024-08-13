import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])
for x in arr:
    print(x)

for x in range(0,2):
  for y in arr[x]:
        print(y)
