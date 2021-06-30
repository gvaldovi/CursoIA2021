
#pip install opencv-contrib-python
#pip install notebook

import numpy as np
#range(5,10,2)
#a = np.arange(5)
#a = np.arange(5,20)
a = np.arange(5,20,2)
print(a)

b = np.array([10,20,30,40],dtype=np.float16)
b = np.array([10,20,30,40],dtype='f2')

c = b.astype(np.int32)

print(b.dtype)
print(c.dtype)

#d = np.ones((3,4))
d = np.zeros((3,4,2))
print(d)

e=np.random.random((3,4))
print(e)

f=np.full((5,6),5)
print(f)

print(f.max())

g=np.arange(24).reshape(2,3,4)
print(g)

h=np.array([[10,11,12],[20,21,22],[30,31,32],[40,41,42]])
print(h)

rengs = np.arange(4)
cols = np.array([0,1,2,0])

#(0,0),(1,1),(2,2),(3,0)
#print(h[rengs,cols])
#h[rengs,cols] += 100
#print(h)

filtro = h>21
print(filtro)

i = h[filtro]
print(i)

h[h%2==0] += 100
print(h)

h=np.array([[10,11,12,23],[20,21,22,23],[30,31,32,23],[40,41,42,23],[50,41,42,23]])
print(h)
subh=h[:3,1:3]
print(subh)
print(h*10)
print(h.mean(axis=1))

A = np.random.randint(low=2,high=50,size=(3,3))
B = np.random.randint(low=2,high=50,size=(3,3))
print(A)
print(B)

C=np.vstack((A,B))
print(C)
C=np.hstack((A,B))
print(C)





