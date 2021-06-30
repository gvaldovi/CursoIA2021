import pandas as pd

#Serie: Columna de una tabla
#DataFrame

a=[1,5,2]

b = pd.Series(a,index=['x','y','z'])
print(b)
print(b['x'])

calorias = {'Lunes':420,'Martes':300,'Miercoles':320}

c=pd.Series(calorias,index=['Lunes','Miercoles'])
print(c)
print(c['Lunes'])

#DataFrame

datos={
    'calorias':[420,300,320],
    'duracion':[50,40,45]
}

d=pd.DataFrame(datos,index=['Lunes','Martes','Miercoles'])
print(d)
print(d.loc[['Lunes','Miercoles']])

#datos.xlsx
#datos.csv