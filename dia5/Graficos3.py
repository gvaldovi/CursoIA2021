import matplotlib.pyplot as plt
import numpy as np

x = np.array([1,3,4,5,6,7,9])
y = np.array([4,7,2,4,7,8,3])

x1 = np.array([1,3,4,5,6,7,9])
y1 = np.array([6,9,4,7,8,9,8])

#plt.scatter(x,y,color='#0000ff')
#plt.scatter(x1,y1)

#x=np.random.normal(170,10,250)
#print(x)

#plt.hist(x)

x = np.array([35,25,25,15])
etiquetas = ['NA','Regulares','Buenos','Sobresalientes']
plt.pie(x,labels=etiquetas,startangle=90,explode=[0.2,0,0,0],shadow=True,autopct='%0.1f%%')
plt.legend(title='Alumnos')

plt.show()