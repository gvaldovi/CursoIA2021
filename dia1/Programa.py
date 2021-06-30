"""
print("Bienvenidos al curos de IA")

#nombre = input("Dame tu nombre:")
num = int(input("Dame un valor:"))
num2 = int(input("Dame un valor2:"))
#num=15

x,y = num,num2

#x=num
#y=num2

print("El valor leido es:",x)
print("El valor leido2 es:",y)
#print("El valor leido es:",num)
#print("El tipo de datos es:",type(num))

if x>5:
    None
elif x>10:
    None
else:
    None

if x>=5:
    print("Mayor a 5")
    print("Mayor a 5")
else:
    print("Menor a 5")


print("Mayor a 5")
"""

#Ciclos
#while, for

i=1
while(i<=5):
    print(i)
    i=i+1

print()

n=10
for i in range(1,n,2):
    print(i,end=" ")

print()

#Listas,Tuplas, Diccionarios

edades = [20,21,15,19,30]
edades2 = (20,21,19)

print(type(edades))
edades.append(25)
edades.pop()
edades.pop()

print(edades)
for i in edades:
    print(i)