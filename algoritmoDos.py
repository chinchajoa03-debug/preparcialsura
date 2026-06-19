#Necesito crea un programa en python que me permita registrar 5 prendas de vestir 
'''producto_uno = input("digita el nombre del producto uno: ")
producto_dos = input("digita el nombre del producto uno: ")
producto_tres = input("digita el nombre del producto uno: ")
producto_cuatro = input("digita el nombre del producto uno: ")
prodcuto_cinco = input("digita el nombre del producto uno: ")

print(f"los productos registrados son: {producto_uno}, {producto_dos}, {producto_tres}, {producto_cuatro} y {prodcuto_cinco}" )


marca_uno = input("digita la marca uno: ")
marca_dos = input("digita la marca dos: ")
marca_tres = input("digita la marca tres: ")

print(f"las marcas que registrastes son {marca_uno}, {marca_dos}, {marca_tres}" '''



#Necesito crear 100000000 premdas que tengan 
#id
#tipo
#marca
#precio
#estado
import random

prendas = []
for i in range(100):
    prenda = {
        "id":random.randint(1,100),
        "tipo":random.choice(["camisa", "pantalon", "falda", "zapatos"]),
        "marca":random.choice(["nike", "adidas", "puma", "reebok"]),
        "precio":random.choice([25000, 30000, 70000, 42000]),
        "estado":random.choice(["nuevo", "usado", "reparado"])
    }

    prendas.append(prenda)
print(prendas)