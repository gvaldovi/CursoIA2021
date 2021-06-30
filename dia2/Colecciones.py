#Listas (mutables), Tuplas (inmutables): Permitir elementos duplicados
#Conjuntos, Diccionarios: No permite elementos duplicados

cad = ""
cad2 = ''

num = [1,5,6,9,4,7,6,8,9,7,5,4,3,2]
nombres = ['Mirian','Alan','Aldo',"Enrique"]
lista = [1,"Juan",True,1.45,[1,3,5]]

y=[]
x=list()
#x.append(9)

print(lista[4])
print(y)
print(x)

print(nombres[3])
print(nombres[-1])

print(len(num))
l1=num[2:8]
print(l1)

l2=[]
for i in range(2,len(num)):
    l2.append(num[i])

print(l2)

num[2]=50
del num[2]
#del num

print(num[:])
print(num[2:])
print(num[:8])
print(num[-4:])

num.sort()

print(num)

noms = ("Yoelvis","Francisco",'Anmiel','Francisco')

t1=()
t2=tuple()

print(noms)
x=noms[1:]
print(type(x))

#Set
noms2 = {"Eduardo","Jesus",'Eduardo'}
print(noms2)

#Diccionarios

per1 ={}
pers2 = dict()

persona = {
    "nombre":"Juan",
    "edad":20,
    "estatura":1.63
}

print(persona)
print(len(persona))
persona['apellidos'] = "Rodriguez"
print(persona['nombre'])
print(persona['edad'])
print(persona.get('estatura'))

persona.pop('edad')
for e in persona:
    print(persona[e])

for e in persona.values():
    print(e)



