
from math import sqrt
import Funciones as f
from Funciones import suma,crear_persona


print(sqrt(9))
print(suma(4,5))

x,y,z=f.obtener_datos()
print(x,y,z)

#p=crear_persona()
print(f.crear_persona()['edad'])


#r=suma(4,5)

f.mensaje('Juan')

print(f.resta())

print(f.suma2(1,2,5,8,9))

f.personas(nombre='Juan',edad=15)

f.combinacion('Manzana',10,20,30,nombre='Juan',edad=15)