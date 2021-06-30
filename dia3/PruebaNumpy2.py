import numpy as np

# 0D
a = np.array(50) 

#1D
b = np.array([1,2,3,4],dtype='f')

#2D
#3x4
c = np.array([[1,2,3,4],[5,6,7,8],[9,0,1,2]])

#3D
d = np.array([[[1,2,3,4],[5,6,7,8]],[[9,0,1,2],[4,5,6,7]]])


e = np.array([1,2,3,4],ndmin=5)

print(a)
print(b)
print(c)
print(d)

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)

print(e)
print('número de dimensiones:',e.ndim)
print(type(a))
print(type(b))

print(b[-3:-1])
print(c[1,-1])
print(d[0,1,2])

print(c[1,1:4])

f=np.array(['Juan','Maria'])
print(b.dtype)

print(b[-3:-1])

g = b.copy()
b[2]=40

print(g)
print(b)

print(c.shape)
print(d.shape)
print(e.shape)

h = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
i = h.reshape(4,3)
print(h)
print(i)
