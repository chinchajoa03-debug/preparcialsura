#Funcion que itera sobre una lista de usuarios 

def crear_listado(numero_iteraciones,prenda):
    prendas = []
    for _ in range(numero_iteraciones):
       prendas.append(prenda)
    return(prendas)