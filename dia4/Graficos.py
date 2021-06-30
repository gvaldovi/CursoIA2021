import matplotlib
import matplotlib.pyplot as plt
import numpy as np

print(matplotlib.__version__)

x = np.array([1,3,4,5,6,7,9])
y = np.array([4,7,2,4,7,8,3])

#plt.plot(x,y,linestyle='dotted')
plt.bar(x,y,label='Barra',color='g')
plt.show()

