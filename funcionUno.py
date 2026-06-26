#Funcion para evaluar correos y contraseñas 
def ingresar_usuario(correo,contraseña,nombre,edad,ciudad):

    CORREO_BD = "prueba@gmail.com"
    CONTRASEÑA_BD = "1234"
    if(correo == CORREO_BD and contraseña == CONTRASEÑA_BD):
        return("Bienvenido")
    else:
        return("Fallamos")
    