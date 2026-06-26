#Funcion que decide sobre el valor de la prenda 

def clasificar_prenda(estado):
    valor_prenda=None
    if estado=="REGULAR":
       valor_prenda=10
    return(valor_prenda)
    elif estado=="BUENO":
    valor_prenda=50
    return(valor_prenda)
    elif estado=="OPTIMO":
    valor_prenda=100
    return(valor_prenda)
    else:
    return("El estado de la prenda no es valido")