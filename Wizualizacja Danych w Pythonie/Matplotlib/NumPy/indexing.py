import numpy as np

arr1 = np.arange(128).reshape(8, 16)
#print(arr1)

print('The fifth element from the third row of arr1:', arr1[2,4])

arr2 = np.arange(128).reshape((8, 4, 4))
#print(arr2)

print('The last item in the fifth row and third column of arr2:', arr2[4,2,-1])

print('The last item from each even rows and first column of arr2:', np.array([arr2[0,0,-1], arr2[2,0,-1],arr2[4,0,-1],arr2[6,0,-1]]))