#Crear un algoritmo que clasifique el estado de la prenda
#si es regular le asigna un puntaje de 10
#si es bueno le asigna un puntaje de 50
#si es optimo le asigna un puntaje de 100 

estado_prenda=input("Digita el estado de la prenda: ").upper()

valor_prenda=None
if estado_prenda=="REGULAR":
    valor_prenda=10
    print(valor_prenda)
elif estado_prenda=="BUENO":
    valor_prenda=50
    print(valor_prenda)
elif estado_prenda=="OPTIMO":
    valor_prenda=100
    print(valor_prenda)
else:
    print("El estado de la prenda no es valido")