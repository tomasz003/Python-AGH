
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])


#Create a filter array that will return only values higher than 4:
filter_arr=arr>4

newarr = arr[filter_arr]

print(filter_arr)
print(newarr)

#Create a filter array that will return only even elements from the original array:

filter_arr = arr%2==0

newarr = arr[filter_arr]

print(filter_arr)
print(newarr)
