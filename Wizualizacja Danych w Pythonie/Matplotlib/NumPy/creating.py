import numpy as np

a = np.array(0)
b = np.array([1,2,3])
c = np.array([[1,2,3],[4,5,6]])
d = np.array([[[1,2,3], [1,2,3]],[[4,5,6], [4,5,6]]])

if __name__ =="__main__":
    print(a.ndim)
    print(b.ndim)
    print((c.ndim,c.size,c.shape))
    print((d.ndim,d.size,d.shape))
