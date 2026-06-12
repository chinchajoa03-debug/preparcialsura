#Entradas del sistema 
'''nombre_usuario= None
correo_usuario = None
contraseña_usuario = None
ciudad_usuario = None
edad_usuario = None'''

'''nombre = input ("Digita tu nombre🧟‍♂️: ")
print(f"hola tu nombre es {nombre} bienvenido 👌")

edad = int(input ("Digita tu edad: "))
print(f"{nombre} tu edad es {edad} años" )

suma = edad + 10
print(f"la suma es {suma}")'''

nombre_usuario = input ("Digita tu nombre: ")
correo_usuario = input ("digita tu correo: ")
contraseña_usuario = input ("digita tu contraseña: ")
ciudad_usuario = input ("digita tu ciudad: ")
edad_usuario = int(input ("digita tu edad: "))

CORREO_BD = "prueba@gmail.com"
CONTRASEÑA_BD = "1234"

#Condicional en python 
if(correo_usuario == CORREO_BD):
    print("Bienvenido")
else:
    print("Fallamos")