import matplotlib.pyplot as plt
import numpy as np

x = np.array([1,3,4,5,6,7,9])
y = np.array([4,7,2,4,7,8,3])

x1 = np.array([1,3,4,5,6,7,9])
y2 = np.array([6,9,4,7,8,9,8])

#plt.plot(x,y,linestyle='dotted')
#plt.bar(x,y,label='Barra',color='g')
#plt.plot(y)
#plt.plot(x,y,x1,y2)
"""
plt.plot(y)
plt.plot(y2)

plt.title('Edades vs Estaturas')
plt.xlabel('Edades')
plt.ylabel('Estaturas')
plt.grid(axis='x')
"""
plt.subplot(2,1,1)
plt.plot(y)
plt.subplot(2,1,2)
plt.plot(y2)

plt.show()
