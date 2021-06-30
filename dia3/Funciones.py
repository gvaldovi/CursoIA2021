
#def suma(x,y):
#    return x+y

def resta(x=20,y=10):
    return x-y

def suma2(x,*args):
    total = x
    for valor in args:
        total+=valor
    return total

def personas(**kwargs):
    print(kwargs)

def combinacion(x,*args,**kwargs):
    print(x)
    print(args)
    print(kwargs)


def mensaje(nombre):
    print("Hola ",nombre," bienvenido al curso de IA")
    print('Hola {1} {0}, bienvenido'.format(nombre,0))


def obtener_datos():
    return 'Juan', 15, 1.67

def crear_persona():
    return {'nombre':'Juan','edad':15,'estatura':1.67}

#Funciones Lambdas
#def suma(x,y): return x+y

suma = lambda x,y:x+y
