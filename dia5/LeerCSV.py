import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('data.csv')
#url='https://cristian.com/datos'

#print(df.to_string())

#df.plot()
#df.plot(kind='scatter',x='Duration',y='Calories')
df['Duration'].plot(kind='hist')

plt.show()

#JSON
#XML

#API REST:GET,POST,PUT,DELETE
